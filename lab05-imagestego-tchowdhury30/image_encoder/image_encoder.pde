import java.util.Arrays;

 //for code that runs one time place all code in setup.
 void setup(){
   size(1200,600);

   String messageToEncode = "The message is encoded using LSBSteganography only when the red/blue values end in 000.";
   PImage img = loadImage("cat.png");

   //to check size for display purposes, if you want to display the image
   //in a processing window
   //println(img.width,img.height);

   //load the image into an array of pixels.
   img.loadPixels();
   //you can use img.pixels[index] to access this array


   //STEP ONE
   //convert the string into an array of ints in the range 0-3
   
   int[]parts = new int[messageToEncode.length() * 4]; 
   int k = 0;
   int lengt33 = messageToEncode.length() * 4;
   for (int i = 0; i < messageToEncode.length(); i++ ){
     int a = messageToEncode.charAt(i);
     int b = 3;
     int loop = 0;
     int tempArray[] = new int[4];
     while (loop < 4) {
       int temp = a & b;
       tempArray[loop] = temp;
       a = a >> 2;
       loop++;
     }
     loop = 0;
     while (loop < 4 && k < lengt33) {
       parts[k] = tempArray[3 - loop];
       k++;
       loop++;
     }
   }
   println(Arrays.toString(parts));
   //println(parts.length);

   //add those values to the correct pixels!
   //when the red and blue end in 000, modify the last 2 bits of green.
   //when no more message is left to encode, change the end of the red+blue from 000 to 001.

   int numPixels = img.width * img.height;
   int counter = 0;
   for (int i = 0; i < numPixels; i++) {
     color c = img.pixels[i];
     int r = (int)red(c);
     int g = (int)green(c);
     int b = (int)blue(c);
     
     //println(r,g,b);
    
     int redLast = ((r & 4) + (r & 2) + (r & 1));
     int blueLast = ((b & 4) + (b & 2) + (b & 1));
     
     if (redLast == 0 && blueLast == 0) {
       if (counter < lengt33) {
         int twofiveteo = 252;
         int newG =  g & twofiveteo;
         newG = parts[counter] | newG;
         color newColor = color(r, newG, b);
         println(g, parts[counter], newG);
         img.pixels[i] = newColor;
         counter++;
       } else {
         int one = 1;
         int newR = r ^ one;
         int newB = b ^ one;
         color newColor = color(newR, g, newB);
         img.pixels[i] = newColor;
       }
     }    
   }
   
   //println(counter);
   //write the pixel array to the image.
   img.updatePixels(); 
   //save the image to disk.
   img.save("modifiedCat.png");
   exit();
 }
 
