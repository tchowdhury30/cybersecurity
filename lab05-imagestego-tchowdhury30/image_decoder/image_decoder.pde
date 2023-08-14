import java.util.Arrays;

 //for code that runs one time place all code in setup.
 void setup(){
   size(1200,600);
   PImage img = loadImage("modifiedCat.png");
   img.loadPixels();
   int[]temp = new int[img.width * img.height];
   int numPixels = img.width * img.height;
   int counter = 0;
   for (int i = 0; i < numPixels; i++) {
     color c = img.pixels[i];
     int r = (int)red(c);
     int g = (int)green(c);
     int b = (int)blue(c);
    
     int redLast = (r & 7);
     int blueLast = (b & 7);
     
     if (redLast == 0 && blueLast == 0) {
       int little = g & 3;
       //println(g, little);
       temp[counter] = little;
       counter++;
     }
   }
   
   //println(counter);
   //println(Arrays.toString(temp));
   int[]parts = new int[counter];
   for (int i = 0; i < counter; i++) {
     parts[i] = temp[i];
   }
   
  //println(Arrays.toString(parts)); 
    String decodedMessage = "";
    int leng = parts.length;
    if (leng % 4 == 0) {
     for (int k = 0; k < leng/4; k++) {
       int a = 0;
       for (int l = 0; l < 4; l++) {
         a = a << 2;
         a += parts[k * 4 + l];
       }
       decodedMessage += (char)a;
     }
     println(decodedMessage);
   } 
   exit();
   
   
   
   
   
   
   
   
   
 }
 
