#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>

void hexdump(char* file) {
  FILE *fp;
  int c;

  fp = fopen(file,"r");
   if(fp == NULL) {
      perror("Error in opening file 1");
      exit(0);
    }

    while ((c = fgetc(fp)) != EOF) {
       printf("%02x ", c);

       if (ferror(fp)) {
         exit(0);
       } else if (feof(fp)) {
         fclose(fp);
       }
  }
}

void encode(char* input, char* keyfile, char* output) {
  FILE *in, *key;
  int c, k, i = 0;

  in = fopen(input,"r");
  if(in == NULL) {
     perror("Error in opening file");
     exit(0);
   }

   key = fopen(keyfile,"r");
   if(key == NULL) {
      perror("Error in opening file");
      exit(0);
    }

    if (fseek(key, 0, SEEK_END) < 0) {
        fclose(key);
        exit(0);
    }

    int keylen = ftell(key);
    char keybuf[keylen];

    rewind(key);
    while ( (k = fgetc(key)) != EOF) {
      keybuf[i] = k;
      //printf("%02x ", keybuf[i]);
      i++;
    }

    fclose(key);

    int out = open(output ,O_WRONLY ,0777);
    if(out==-1){
      printf("%s\n",strerror(errno));
      exit(errno);
    }

    i = 0;
    while ((c = fgetc(in)) != EOF) {
      if (c == 0) {
      } else {
        //printf("%02x XOR %02x\n", c, keybuf[i]);
        c = c ^ keybuf[i];
        i++;
        if (i >= keylen) {
          i = 0;
        }

        write(out, &c, sizeof(c));
        //printf("%02x ", c);
      }

      if (ferror(in)) {
        exit(0);
      } else if (feof(in)) {
        fclose(in);
      }

    }
}

void decode(char* input, char* keyfile) {
  FILE *in, *key;
  int c, k, i = 0;

  in = fopen(input,"r");
  if(in == NULL) {
     perror("Error in opening file");
     exit(0);
   }

   key = fopen(keyfile,"r");
   if(key == NULL) {
      perror("Error in opening file");
      exit(0);
    }
    if (fseek(key, 0, SEEK_END) < 0) {
        fclose(key);
        exit(0);
    }

    int keylen = ftell(key);
    char keybuf[keylen];

    rewind(key);

    while ( (k = fgetc(key)) != EOF) {
      keybuf[i] = k;
      //printf("%02x ", keybuf[i]);
      i++;
    }

    fclose(key);

    i = 0;
    while ((c = fgetc(in)) != EOF) {
      if (c == 0) {
      } else {
        //printf("%02x XOR %02x\n", c, keybuf[i]);
        c = c ^ keybuf[i];
        i++;
        if (i >= keylen) {
          i = 0;
        }
        //printf("%02x ", c);
        printf("%c", c);
      }

      if (ferror(in)) {
        exit(0);
      } else if (feof(in)) {
        fclose(in);
      }

    }
}

int main(int argc, char *argv[]) {
  if ( strcmp(argv[1], "hex") == 0) {
    hexdump(argv[2]);
  } else if ( strcmp(argv[1], "encode") == 0) {
    encode(argv[2], argv[3], argv[4]);
  } else if ( strcmp(argv[1], "decode") == 0) {
    decode(argv[2], argv[3]);
  }
}
