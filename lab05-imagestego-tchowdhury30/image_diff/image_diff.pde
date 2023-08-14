import java.util.Arrays;

void setup() {
  size(1200, 600);
  
  PImage ImgA = loadImage("cat.png");
  PImage ImgB = loadImage("modifiedCat.png");
  
  ImgA.loadPixels();
  ImgB.loadPixels();
  
  for (int i = 0; i < ImgB.width; i++) {
    for (int j = 0; j < ImgB.height; j++) {
      int pixelIndex = j * ImgB.width + i;
      int c = ImgB.pixels[pixelIndex];
      int r = (c >> 16) & 255;
      int g = (c >> 8) & 255;
      int b = c & 255;
      
       // Get the color of the corresponding pixel in the original image
      int originalColor = ImgA.get(i, j);
      int originalR = (originalColor >> 16) & 0xFF;
      int originalG = (originalColor >> 8) & 0xFF;
      int originalB = originalColor & 0xFF;
      
      if ((r&7) == 0 && (b&7) == 0) {
        //When the modified pixel contains encoded data (triple 000's on blue and red) output a green pixel.
        stroke(0, 255, 0);
        point(i, j);
        
      } else if ( (r != originalR) || (b != originalB) ) {  
        //When the modified pixel is a dummy pixel (the pixel is difffernt than original) output a purple pixel (255,0,255).
        stroke(255, 0, 255);
        point(i, j);
        
      } else if (r == originalR && g == originalG && b == originalB) {
        //When the pixel is the same as the original , display the original color
        stroke(originalColor);
        point(i, j);
        
      }
      
    }
  }
  
}
