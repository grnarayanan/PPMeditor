Portable Pixmap (PPM) Editor

Welcome to the PPM Editor! This module is a PPM image editor.
The editor includes 10 different effects: 
The user provides an input file and the editor produces an output image. 

*Note: The editor is only compatible with the P3 PPM Image format (P6 is incompatible).

Detailed information about each of the effects is given below. 

1) Object Filter
Using three copies of the same image with obstructions in different locations, filter creates
a new image sans obstructions.  

2) Shades of Gray
Creates a grayscale image.  

3) Horizontal Flip
Flips an image across the vertical axis. 

4) Saturate Blues
Changes the saturation of the blue-cyan color range. Boost value must be in decimal form (to reduce saturation,
provide a decimal less than 1, and to boost a decimal greater than 1). Customizable based on a given
region* by the user. 

5) Saturate Greens
Changes the saturation of the yellow-green-cyan color range. Boost value must be in decimal form (to reduce saturation,
provide a decimal less than 1, and to boost a decimal greater than 1). Customizable based on a given
region* by the user. 

6) Saturate Reds
Changes the saturation of the pink-red color range. Boost value must be in decimal form (to reduce saturation,
provide a decimal less than 1, and to boost a decimal greater than 1). Customizable based on a given
region* by the user. 

7) Saturate Custom
Changes the saturation based on a user given custom range, with lower and upper bound values given in hue. Boost value 
must be in decimal form (to reduce saturation, provide a decimal less than 1, and to boost a decimal greater than 1). 
Customizable based on a given region* by the user.   

8) Color Shift
Shifts a given color range by a fixed value given by the user. All values given in hue. A negative shift value will
shift the colors towards 0 degrees hue. Customizable based on a given region* by the user. 

9) Negative
Creates a negative image. 

10) Rotate
Rotates an image by 90 degrees. To rotate an image 180 or 270 degrees, rerun with the output image from previous rotation. 


*Region measured vertically from the top of the image. First value is the how far down the region selection should start, and 
the second value is the end. Values are given by fractional portions of the image. Ie. region1 = 1/3, region2 = 2/3 would select
the middle 1/3 of the image. 


