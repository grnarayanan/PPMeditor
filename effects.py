"""
Created on Mon Aug 10 16:38:20 2020

@author: ganes

Effects Module v2.0

Contains various image effects/tools for PPM images. 
"""


import numpy as np


def object_filter(image1, image2, image3, image0):
    '''Removes obstructions from an image
       
       Takes in three versions of an image and produces
       a clean output image file'''
    
    # opens three input files for read and creates output file for write  
    try:
        
        pic1 = open(image1, 'r')
        pic2 = open(image2, 'r')
        pic3 = open(image3, 'r')
        
    except:
        
        print()
        print("One or more input files not found. ", end='')
        
    else:
        
        out = open(image0, 'w')
    
        # verifies that all 3 images are PPM format
        if (pic1.readline().strip() == 'P3' and pic2.readline().strip() == 'P3' and
            pic3.readline().strip() == 'P3'):
            
            # reads dimensions of images
            dims1 = pic1.readline().split()
            dims2 = pic2.readline().split()
            dims3 = pic3.readline().split()
            
            # verifies that dimensiions of all 3 images are same
            if dims1 == dims2 and dims2 == dims3:
                
                # creates a default matrix with dimensions given by the image
                matrix1 = np.array(range(int(dims1[0]) * int(dims1[1]) * 3))
                #matrix1 = matrix1.reshape(int(dims1[0]), int(dims1[1]))
                
                # creates two more identical matrices, one for each image, and
                # one for the output image (matrix0)
                matrix2 = matrix1.copy()
                matrix3 = matrix1.copy()
                matrix0 = matrix1.copy()
                
                # skips past line indicating maximum color value
                pic1.readline()
                pic2.readline()
                pic3.readline()
                
                # reads pixel values of each image into a list
                body1 = pic1.read().split()
                body2 = pic2.read().split()
                body3 = pic3.read().split()
            
                # iterates through each RGB value for each image and adds to 
                # corresponding matrix numpy array
                
                i = 0
                
                for rgb in body1:
                    
                    matrix1[i] = int(rgb)
                    i += 1
                
                i = 0
                
                for rgb in body2:
                    
                    matrix2[i] = int(rgb)
                    i += 1
                
                i = 0
                
                for rgb in body3:
                    
                    matrix3[i] = int(rgb)
                    i += 1
                
                # iterates through output matrix0 numpy array
                for i in range(len(matrix0)):
                    
                    # sets maj to whichever RGB value is a majority
            
                    if matrix2[i] == matrix3[i]:
                        
                        maj = matrix2[i]
                    
                    elif matrix3[i] == matrix1[i]:
                        
                        maj = matrix3[i]
                        
                    else:
                        
                        maj = matrix1[i]
                    
                    # sets output RGB value to maj
                    matrix0[i] = maj
                
                # reshape output matrix0 to image dimensions
                matrix0 = matrix0.reshape(int(dims1[1]), int(dims1[0]) * 3)
                
                # write proper PPM formatting for output file
                out.write('P3' + '\n')
                out.write(dims1[0] + ' ' + dims1[1] + '\n')
                out.write(str(matrix0.max()) + '\n')
                
                # iterate through each RGB value and add new lines when appropriate
                for i in range(len(matrix0)):
                    
                    for j in range(len(matrix0[i])):
                        
                        if j == (len(matrix0[i]) - 1):
                            
                            out.write(str(matrix0[i][j]) + '\n')
                        
                        else:
                            
                            out.write(str(matrix0[i][j]) + ' ')
                
                # close all files            
                pic1.close()
                pic2.close()
                pic3.close()
                out.close()
                
                # indicates successful operation
                return 1


def shades_of_gray(image1, image0):
    '''Converts a color image into grayscale
    
       Takes in an image file and creates a new output image file'''
    
    # opens input file for read and creates output file for write    
    try:
        
        pic = open(image1, 'r')
    
    except: 
        
        print()
        print("Input file not found. ", end='')
    
    else:
    
        out = open(image0, 'w')
        
        # verifies that image is PPM format
        if (pic.readline().strip() == 'P3'):
            
            comment = pic.readline()
            
            if (comment[0] == '#'):
                
                dims = pic.readline().split()
            
            else:
                
                # reads dimensions of image
                dims = comment.split()
                
            # creates a default matrix with dimensions given by the image
            matrix1 = np.array(range(int(dims[0]) * int(dims[1]) * 3))
            
            # creates an identical matrix for output image
            matrix0 = matrix1.copy()
            
            # skips past line indicating maximum color value
            pic.readline()
            
            # reads pixel values of each image into a list
            body = pic.read().split()
            
            # iterates through each RGB value of image and adds to 
            # matrix1 numpy array
            
            i = 0
                
            for rgb in body:
                
                matrix1[i] = int(rgb)
                i += 1
            
            # iterates through every pixel (every 3 RGB values)
            for i in range(0, len(matrix1), 3):
                
                # averages three RGB values in pixel and sets output matrix0 pixel
                # to that RGB value
                avgRGB = (matrix1[i] + matrix1[i+1] + matrix1[i+2]) / 3
                matrix0[i], matrix0[i+1], matrix0[i+2] = avgRGB, avgRGB, avgRGB
            
            # reshape output matrix0 to image dimensions
            matrix0 = matrix0.reshape(int(dims[1]), int(dims[0]) * 3)
                        
            # write proper PPM formatting for output file
            out.write('P3' + '\n')
            out.write(dims[0] + ' ' + dims[1] + '\n')
            out.write(str(matrix0.max()) + '\n')
            
            # iterate through each RGB value and add new lines when appropriate
            for i in range(len(matrix0)):
                
                for j in range(len(matrix0[i])):
                    
                    if j == (len(matrix0[i]) - 1):
                        
                        out.write(str(matrix0[i][j]) + '\n')
                    
                    else:
                        
                        out.write(str(matrix0[i][j]) + ' ')
            
            # close all files                    
            pic.close()
            out.close()
            
            # indicates successful operation
            return 1


def horizontal_flip(image1, image0):
    '''Flips an image horizontally

       Takes in an image file and creates a new output image file'''
    
    try:
        
        pic = open(image1, 'r')
    
    except: 
        
        print()
        print("Input file not found. ", end='')
    
    else:
    
        out = open(image0, 'w')
    
        # verifies that image is PPM format
        if (pic.readline().strip() == 'P3'):
            
            comment = pic.readline()
            
            if (comment[0] == '#'):
                
                dims = pic.readline().split()
            
            else:
                
                # reads dimensions of image
                dims = comment.split()
                
            # creates a default matrix with dimensions given by the image
            matrix1 = np.array(range(int(dims[0]) * int(dims[1]) * 3))
                    
            # skips past line indicating maximum color value
            pic.readline()
            
            # reads pixel values of each image into a list
            body = pic.read().split()
            
            # iterates through each RGB value of image and adds to 
            # matrix1 numpy array        
            i = 0
                
            for rgb in body:
                
                matrix1[i] = int(rgb)
                i += 1        
            
            # creates an identical matrix for output image
            matrix0 = matrix1.copy()
            
            # reshape matrix numpy arrays to image dimensions
            matrix1 = matrix1.reshape(int(dims[1]), int(dims[0]) * 3)
            matrix0 = matrix0.reshape(int(dims[1]), int(dims[0]) * 3)
            
            # iterate through each line of pixels
            for i in range(len(matrix1)):
                
                # iterate through each pixel (every 3 RGB values)
                for j in range(0, len(matrix1[i]), 3):
                    
                    # set last 3 RGB values of output to first 3 from input image, 
                    # preserving order of RGB
                    matrix0[i][len(matrix0[i]) - (j + 3)] = matrix1[i][j]
                    matrix0[i][len(matrix0[i]) - (j + 2)] = matrix1[i][j+1]
                    matrix0[i][len(matrix0[i]) - (j + 1)] = matrix1[i][j+2]
    
            # write proper PPM formatting for output file
            out.write('P3' + '\n')
            out.write(dims[0] + ' ' + dims[1] + '\n')
            out.write(str(matrix0.max()) + '\n')
            
            # iterate through each RGB value and add new lines when appropriate
            for i in range(len(matrix0)):
                
                for j in range(len(matrix0[i])):
                    
                    if j == (len(matrix0[i]) - 1):
                        
                        out.write(str(matrix0[i][j]) + '\n')
                    
                    else:
                        
                        out.write(str(matrix0[i][j]) + ' ')
            
            # close all files            
            pic.close()
            out.close()
            
            # indicates successful operation
            return 1
        

def saturate_blues(image1, image0, boost, region1, region2):
    '''Saturates the blues in an image
    
       Takes in an image file and creates a new output image file'''
    
    # opens input file for read and creates output file for write    
    try:
        
        pic = open(image1, 'r')
    
    except: 
        
        print()
        print("Input file not found. ", end='')
    
    else:
    
        out = open(image0, 'w')
    
        # verifies that image is PPM format
        if (pic.readline().strip() == 'P3'):
            
            comment = pic.readline()
            
            if (comment[0] == '#'):
                
                dims = pic.readline().split()
            
            else:
                
                # reads dimensions of image
                dims = comment.split()
                
            # creates a default matrix with dimensions given by the image
            matrix1 = np.array(range(int(dims[0]) * int(dims[1]) * 3))
            
            # creates an identical matrix for output image
            matrix0 = matrix1.copy()
            
            # skips past line indicating maximum color value
            pic.readline()
            
            # reads pixel values of each image into a list
            body = pic.read().split()
            
            # iterates through each RGB value of image and adds to 
            # matrix1 numpy array
            
            i = 0
                
            for rgb in body:
                
                matrix1[i] = int(rgb)
                i += 1
                
            if (region1 > 1):
                
                region1 = 1
                
            elif (region1 < 0):
                
                region1 = 0
                
            if (region2 > 1):
                
                region2 = 1
                
            elif (region2 < 0):
                
                region2 = 0
                
            if (region1 > region2):
                
                region1, region2 = region2, region1
            
            # iterates through every pixel (every 3 RGB values)
            for i in range(int((region1 * len(matrix1)) / 3) * 3, int((region2 * len(matrix1)) / 3) * 3, 3):
                
                # converting rgb to hsl
                
                r_ = matrix1[i] / 255
                g_ = matrix1[i+1] / 255
                b_ = matrix1[i+2] / 255
                
                cmax = max(r_, g_, b_)
                cmin = min(r_, g_, b_)
                
                delta = cmax - cmin
                
                # hue calculation
                if (delta == 0):
                    
                    h = 0
                
                elif (cmax == r_):
                    
                    h = 60 * (((g_ - b_) / delta) % 6)
                
                elif (cmax == g_):
                    
                    h = 60 * (((b_ - r_) / delta) + 2)
                
                elif (cmax == b_):
                    
                    h = 60 * (((r_ - g_) / delta) + 4)
                
                else:
                    
                    h = 0
                
                # lightness calculation
                l = (cmax + cmin) / 2
                
                # saturation calculation
                if (delta == 0):
                    
                    s = 0
                
                else:
                    
                    s = delta / (1 - abs(2*l - 1))
                    
                # saturation boost in blue-cyan range
                if (h >= 201 and h <= 240): 
                    
                    s = ((boost / 100) + 1) * s
                    
                    if (s > 1):
                        
                        s = 1
                
                    # conversion back to rgb
                    c = (1 - abs(2*l - 1)) * s
                    
                    x = c * (1 - abs(((h / 60) % 2) - 1))
                    
                    m = l - (c / 2)
                    
                    if (h >= 0 and h < 60):
                        
                        r_ = c
                        g_ = x
                        b_ = 0
                    
                    elif (h >= 60 and h < 120):
                        
                        r_ = x
                        g_ = c
                        b_ = 0
                    
                    elif (h >= 120 and h < 180):
                        
                        r_ = 0
                        g_ = c
                        b_ = x
                    
                    elif (h >= 180 and h < 240):
                        
                        r_ = 0
                        g_ = x
                        b_ = c
                        
                    elif (h >= 240 and h < 300):
                        
                        r_ = x
                        g_ = 0
                        b_ = c
                    
                    elif (h >= 300 and h < 360):
                        
                        r_ = c
                        g_ = 0
                        b_ = x
                    
                    else:
                        
                        r_ = 0
                        g_ = 0
                        b_ = 0
                    
                    # sets output image pixel to newly boosted pixel
                    matrix0[i], matrix0[i+1], matrix0[i+2] = (r_ + m) * 255, (g_ + m) * 255, (b_ + m) * 255
                
                else:
                    
                    # sets output image pixel to original, unmodified pixel
                    matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            # fills remaining output pixels to original pixel
            for i in range(0, int((region1 * len(matrix1)) / 3) * 3, 3):
                
                matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            for i in range(int((region2 * len(matrix1)) / 3) * 3, len(matrix1), 3):
                
                matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            # reshape output matrix0 to image dimensions
            matrix0 = matrix0.reshape(int(dims[1]), int(dims[0]) * 3)
                        
            # write proper PPM formatting for output file
            out.write('P3' + '\n')
            out.write(dims[0] + ' ' + dims[1] + '\n')
            out.write(str(matrix0.max()) + '\n')
            
            # iterate through each RGB value and add new lines when appropriate
            for i in range(len(matrix0)):
                
                for j in range(len(matrix0[i])):
                    
                    if j == (len(matrix0[i]) - 1):
                        
                        out.write(str(matrix0[i][j]) + '\n')
                    
                    else:
                        
                        out.write(str(matrix0[i][j]) + ' ')
            
            # close all files                    
            pic.close()
            out.close()
            
            # indicates successful operation
            return 1


def saturate_greens(image1, image0, boost, region1, region2):
    '''Saturates the greens in an image
    
       Takes in an image file and creates a new output image file'''
    
    # opens input file for read and creates output file for write    
    try:
        
        pic = open(image1, 'r')
    
    except: 
        
        print()
        print("Input file not found. ", end='')
    
    else:
    
        out = open(image0, 'w')
    
        # verifies that image is PPM format
        if (pic.readline().strip() == 'P3'):
            
            comment = pic.readline()
            
            if (comment[0] == '#'):
                
                dims = pic.readline().split()
            
            else:
                
                # reads dimensions of image
                dims = comment.split()
                
            # creates a default matrix with dimensions given by the image
            matrix1 = np.array(range(int(dims[0]) * int(dims[1]) * 3))
            
            # creates an identical matrix for output image
            matrix0 = matrix1.copy()
            
            # skips past line indicating maximum color value
            pic.readline()
            
            # reads pixel values of each image into a list
            body = pic.read().split()
            
            # iterates through each RGB value of image and adds to 
            # matrix1 numpy array
            
            i = 0
                
            for rgb in body:
                
                matrix1[i] = int(rgb)
                i += 1
                
            if (region1 > 1):
                
                region1 = 1
                
            elif (region1 < 0):
                
                region1 = 0
                
            if (region2 > 1):
                
                region2 = 1
                
            elif (region2 < 0):
                
                region2 = 0
                
            if (region1 > region2):
                
                region1, region2 = region2, region1
            
            # iterates through every pixel (every 3 RGB values)
            for i in range(int((region1 * len(matrix1)) / 3) * 3, int((region2 * len(matrix1)) / 3) * 3, 3):
                
                # converting rgb to hsl
                
                r_ = matrix1[i] / 255
                g_ = matrix1[i+1] / 255
                b_ = matrix1[i+2] / 255
                
                cmax = max(r_, g_, b_)
                cmin = min(r_, g_, b_)
                
                delta = cmax - cmin
                
                # hue calculation
                if (delta == 0):
                    
                    h = 0
                
                elif (cmax == r_):
                    
                    h = 60 * (((g_ - b_) / delta) % 6)
                
                elif (cmax == g_):
                    
                    h = 60 * (((b_ - r_) / delta) + 2)
                
                elif (cmax == b_):
                    
                    h = 60 * (((r_ - g_) / delta) + 4)
                
                else:
                    
                    h = 0
                
                # lightness calculation
                l = (cmax + cmin) / 2
                
                # saturation calculation
                if (delta == 0):
                    
                    s = 0
                
                else:
                    
                    s = delta / (1 - abs(2*l - 1))
                    
                # saturation boost in yellow-green-cyan range
                if (h >= 61 and h <= 169): 
                    
                    s = ((boost / 100) + 1) * s
                    
                    if (s > 1):
                        
                        s = 1
                
                    # conversion back to rgb
                    c = (1 - abs(2*l - 1)) * s
                    
                    x = c * (1 - abs(((h / 60) % 2) - 1))
                    
                    m = l - (c / 2)
                    
                    if (h >= 0 and h < 60):
                        
                        r_ = c
                        g_ = x
                        b_ = 0
                    
                    elif (h >= 60 and h < 120):
                        
                        r_ = x
                        g_ = c
                        b_ = 0
                    
                    elif (h >= 120 and h < 180):
                        
                        r_ = 0
                        g_ = c
                        b_ = x
                    
                    elif (h >= 180 and h < 240):
                        
                        r_ = 0
                        g_ = x
                        b_ = c
                        
                    elif (h >= 240 and h < 300):
                        
                        r_ = x
                        g_ = 0
                        b_ = c
                    
                    elif (h >= 300 and h < 360):
                        
                        r_ = c
                        g_ = 0
                        b_ = x
                    
                    else:
                        
                        r_ = 0
                        g_ = 0
                        b_ = 0
                    
                    # sets output image pixel to newly boosted pixel
                    matrix0[i], matrix0[i+1], matrix0[i+2] = (r_ + m) * 255, (g_ + m) * 255, (b_ + m) * 255
                
                else:
                    
                    # sets output image pixel to original, unmodified pixel
                    matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            # fills remaining output pixels to original pixel
            for i in range(0, int((region1 * len(matrix1)) / 3) * 3, 3):
                
                matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            for i in range(int((region2 * len(matrix1)) / 3) * 3, len(matrix1), 3):
                
                matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            # reshape output matrix0 to image dimensions
            matrix0 = matrix0.reshape(int(dims[1]), int(dims[0]) * 3)
                        
            # write proper PPM formatting for output file
            out.write('P3' + '\n')
            out.write(dims[0] + ' ' + dims[1] + '\n')
            out.write(str(matrix0.max()) + '\n')
            
            # iterate through each RGB value and add new lines when appropriate
            for i in range(len(matrix0)):
                
                for j in range(len(matrix0[i])):
                    
                    if j == (len(matrix0[i]) - 1):
                        
                        out.write(str(matrix0[i][j]) + '\n')
                    
                    else:
                        
                        out.write(str(matrix0[i][j]) + ' ')
            
            # close all files                    
            pic.close()
            out.close()
            
            # indicates successful operation
            return 1
        

def saturate_reds(image1, image0, boost, region1, region2):
    '''Saturates the reds in an image
    
       Takes in an image file and creates a new output image file'''
    
    # opens input file for read and creates output file for write    
    try:
        
        pic = open(image1, 'r')
    
    except: 
        
        print()
        print("Input file not found. ", end='')
    
    else:
    
        out = open(image0, 'w')
    
        # verifies that image is PPM format
        if (pic.readline().strip() == 'P3'):
            
            comment = pic.readline()
            
            if (comment[0] == '#'):
                
                dims = pic.readline().split()
            
            else:
                
                # reads dimensions of image
                dims = comment.split()
                
            # creates a default matrix with dimensions given by the image
            matrix1 = np.array(range(int(dims[0]) * int(dims[1]) * 3))
            
            # creates an identical matrix for output image
            matrix0 = matrix1.copy()
            
            # skips past line indicating maximum color value
            pic.readline()
            
            # reads pixel values of each image into a list
            body = pic.read().split()
            
            # iterates through each RGB value of image and adds to 
            # matrix1 numpy array
            
            i = 0
                
            for rgb in body:
                
                matrix1[i] = int(rgb)
                i += 1
                
            if (region1 > 1):
                
                region1 = 1
                
            elif (region1 < 0):
                
                region1 = 0
                
            if (region2 > 1):
                
                region2 = 1
                
            elif (region2 < 0):
                
                region2 = 0
                
            if (region1 > region2):
                
                region1, region2 = region2, region1
            
            # iterates through every pixel (every 3 RGB values)
            for i in range(int((region1 * len(matrix1)) / 3) * 3, int((region2 * len(matrix1)) / 3) * 3, 3):
                
                # converting rgb to hsl
                
                r_ = matrix1[i] / 255
                g_ = matrix1[i+1] / 255
                b_ = matrix1[i+2] / 255
                
                cmax = max(r_, g_, b_)
                cmin = min(r_, g_, b_)
                
                delta = cmax - cmin
                
                # hue calculation
                if (delta == 0):
                    
                    h = 0
                
                elif (cmax == r_):
                    
                    h = 60 * (((g_ - b_) / delta) % 6)
                
                elif (cmax == g_):
                    
                    h = 60 * (((b_ - r_) / delta) + 2)
                
                elif (cmax == b_):
                    
                    h = 60 * (((r_ - g_) / delta) + 4)
                
                else:
                    
                    h = 0
                
                # lightness calculation
                l = (cmax + cmin) / 2
                
                # saturation calculation
                if (delta == 0):
                    
                    s = 0
                
                else:
                    
                    s = delta / (1 - abs(2*l - 1))
                    
                # saturation boost in pink-red range
                if ((h >= 331 and h <= 359) or (h >= 0 and h <= 10)): 
                    
                    s = ((boost / 100) + 1) * s
                    
                    if (s > 1):
                        
                        s = 1
                
                    # conversion back to rgb
                    c = (1 - abs(2*l - 1)) * s
                    
                    x = c * (1 - abs(((h / 60) % 2) - 1))
                    
                    m = l - (c / 2)
                    
                    if (h >= 0 and h < 60):
                        
                        r_ = c
                        g_ = x
                        b_ = 0
                    
                    elif (h >= 60 and h < 120):
                        
                        r_ = x
                        g_ = c
                        b_ = 0
                    
                    elif (h >= 120 and h < 180):
                        
                        r_ = 0
                        g_ = c
                        b_ = x
                    
                    elif (h >= 180 and h < 240):
                        
                        r_ = 0
                        g_ = x
                        b_ = c
                        
                    elif (h >= 240 and h < 300):
                        
                        r_ = x
                        g_ = 0
                        b_ = c
                    
                    elif (h >= 300 and h < 360):
                        
                        r_ = c
                        g_ = 0
                        b_ = x
                    
                    else:
                        
                        r_ = 0
                        g_ = 0
                        b_ = 0
                    
                    # sets output image pixel to newly boosted pixel
                    matrix0[i], matrix0[i+1], matrix0[i+2] = (r_ + m) * 255, (g_ + m) * 255, (b_ + m) * 255
                
                else:
                    
                    # sets output image pixel to original, unmodified pixel
                    matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            # fills remaining output pixels to original pixel
            for i in range(0, int((region1 * len(matrix1)) / 3) * 3, 3):
                
                matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            for i in range(int((region2 * len(matrix1)) / 3) * 3, len(matrix1), 3):
                
                matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            # reshape output matrix0 to image dimensions
            matrix0 = matrix0.reshape(int(dims[1]), int(dims[0]) * 3)
                        
            # write proper PPM formatting for output file
            out.write('P3' + '\n')
            out.write(dims[0] + ' ' + dims[1] + '\n')
            out.write(str(matrix0.max()) + '\n')
            
            # iterate through each RGB value and add new lines when appropriate
            for i in range(len(matrix0)):
                
                for j in range(len(matrix0[i])):
                    
                    if j == (len(matrix0[i]) - 1):
                        
                        out.write(str(matrix0[i][j]) + '\n')
                    
                    else:
                        
                        out.write(str(matrix0[i][j]) + ' ')
            
            # close all files                    
            pic.close()
            out.close()
            
            # indicates successful operation
            return 1


def saturate_custom(image1, image0, lower, upper, boost, region1, region2):
    '''Saturates the blues in an image
    
       Takes in an image file and creates a new output image file'''
    
    # opens input file for read and creates output file for write    
    try:
        
        pic = open(image1, 'r')
    
    except: 
        
        print()
        print("Input file not found. ", end='')
    
    else:
    
        out = open(image0, 'w')
    
        # verifies that image is PPM format
        if (pic.readline().strip() == 'P3'):
            
            comment = pic.readline()
            
            if (comment[0] == '#'):
                
                dims = pic.readline().split()
            
            else:
                
                # reads dimensions of image
                dims = comment.split()
                
            # creates a default matrix with dimensions given by the image
            matrix1 = np.array(range(int(dims[0]) * int(dims[1]) * 3))
            
            # creates an identical matrix for output image
            matrix0 = matrix1.copy()
            
            # skips past line indicating maximum color value
            pic.readline()
            
            # reads pixel values of each image into a list
            body = pic.read().split()
            
            # iterates through each RGB value of image and adds to 
            # matrix1 numpy array
            
            i = 0
                
            for rgb in body:
                
                matrix1[i] = int(rgb)
                i += 1
                
            if (region1 > 1):
                
                region1 = 1
                
            elif (region1 < 0):
                
                region1 = 0
                
            if (region2 > 1):
                
                region2 = 1
                
            elif (region2 < 0):
                
                region2 = 0
                
            if (region1 > region2):
                
                region1, region2 = region2, region1
            
            # iterates through every pixel (every 3 RGB values)
            for i in range(int((region1 * len(matrix1)) / 3) * 3, int((region2 * len(matrix1)) / 3) * 3, 3):
                
                # converting rgb to hsl
                
                r_ = matrix1[i] / 255
                g_ = matrix1[i+1] / 255
                b_ = matrix1[i+2] / 255
                
                cmax = max(r_, g_, b_)
                cmin = min(r_, g_, b_)
                
                delta = cmax - cmin
                
                # hue calculation
                if (delta == 0):
                    
                    h = 0
                
                elif (cmax == r_):
                    
                    h = 60 * (((g_ - b_) / delta) % 6)
                
                elif (cmax == g_):
                    
                    h = 60 * (((b_ - r_) / delta) + 2)
                
                elif (cmax == b_):
                    
                    h = 60 * (((r_ - g_) / delta) + 4)
                
                else:
                    
                    h = 0
                
                # lightness calculation
                l = (cmax + cmin) / 2
                
                # saturation calculation
                if (delta == 0):
                    
                    s = 0
                
                else:
                    
                    s = delta / (1 - abs(2*l - 1))
                    
                # saturation boost in a custom range
                if (h >= lower and h <= upper): 
                    
                    s = ((boost / 100) + 1) * s
                    
                    if (s > 1):
                        
                        s = 1
                
                    # conversion back to rgb
                    c = (1 - abs(2*l - 1)) * s
                    
                    x = c * (1 - abs(((h / 60) % 2) - 1))
                    
                    m = l - (c / 2)
                    
                    if (h >= 0 and h < 60):
                        
                        r_ = c
                        g_ = x
                        b_ = 0
                    
                    elif (h >= 60 and h < 120):
                        
                        r_ = x
                        g_ = c
                        b_ = 0
                    
                    elif (h >= 120 and h < 180):
                        
                        r_ = 0
                        g_ = c
                        b_ = x
                    
                    elif (h >= 180 and h < 240):
                        
                        r_ = 0
                        g_ = x
                        b_ = c
                        
                    elif (h >= 240 and h < 300):
                        
                        r_ = x
                        g_ = 0
                        b_ = c
                    
                    elif (h >= 300 and h < 360):
                        
                        r_ = c
                        g_ = 0
                        b_ = x
                    
                    else:
                        
                        r_ = 0
                        g_ = 0
                        b_ = 0
                    
                    # sets output image pixel to newly boosted pixel
                    matrix0[i], matrix0[i+1], matrix0[i+2] = (r_ + m) * 255, (g_ + m) * 255, (b_ + m) * 255
                
                else:
                    
                    # sets output image pixel to original, unmodified pixel
                    matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            # fills remaining output pixels to original pixel
            for i in range(0, int((region1 * len(matrix1)) / 3) * 3, 3):
                
                matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            for i in range(int((region2 * len(matrix1)) / 3) * 3, len(matrix1), 3):
                
                matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            # reshape output matrix0 to image dimensions
            matrix0 = matrix0.reshape(int(dims[1]), int(dims[0]) * 3)
                        
            # write proper PPM formatting for output file
            out.write('P3' + '\n')
            out.write(dims[0] + ' ' + dims[1] + '\n')
            out.write(str(matrix0.max()) + '\n')
            
            # iterate through each RGB value and add new lines when appropriate
            for i in range(len(matrix0)):
                
                for j in range(len(matrix0[i])):
                    
                    if j == (len(matrix0[i]) - 1):
                        
                        out.write(str(matrix0[i][j]) + '\n')
                    
                    else:
                        
                        out.write(str(matrix0[i][j]) + ' ')
            
            # close all files                    
            pic.close()
            out.close()
            
            # indicates successful operation
            return 1


def color_shift(image1, image0, lower, upper, shift, region1, region2):
    '''Shift a specific range of colors in an image
    
       Takes in an image file and creates a new output image file'''
    
    # opens input file for read and creates output file for write    
    try:
        
        pic = open(image1, 'r')
    
    except: 
        
        print()
        print("Input file not found. ", end='')
    
    else:
    
        out = open(image0, 'w')
    
        # verifies that image is PPM format
        if (pic.readline().strip() == 'P3'):
            
            comment = pic.readline()
            
            if (comment[0] == '#'):
                
                dims = pic.readline().split()
            
            else:
                
                # reads dimensions of image
                dims = comment.split()
                
            # creates a default matrix with dimensions given by the image
            matrix1 = np.array(range(int(dims[0]) * int(dims[1]) * 3))
            
            # creates an identical matrix for output image
            matrix0 = matrix1.copy()
            
            # skips past line indicating maximum color value
            pic.readline()
            
            # reads pixel values of each image into a list
            body = pic.read().split()
            
            # iterates through each RGB value of image and adds to 
            # matrix1 numpy array
            
            i = 0
                
            for rgb in body:
                
                matrix1[i] = int(rgb)
                i += 1
            
            if (region1 > 1):
                
                region1 = 1
                
            elif (region1 < 0):
                
                region1 = 0
                
            if (region2 > 1):
                
                region2 = 1
                
            elif (region2 < 0):
                
                region2 = 0
                
            if (region1 > region2):
                
                region1, region2 = region2, region1
            
            # iterates through every pixel (every 3 RGB values)
            for i in range(int((region1 * len(matrix1)) / 3) * 3, int((region2 * len(matrix1)) / 3) * 3, 3):
                
                # converting rgb to hsl
                
                r_ = matrix1[i] / 255
                g_ = matrix1[i+1] / 255
                b_ = matrix1[i+2] / 255
                
                cmax = max(r_, g_, b_)
                cmin = min(r_, g_, b_)
                
                delta = cmax - cmin
                
                # hue calculation
                if (delta == 0):
                    
                    h = 0
                
                elif (cmax == r_):
                    
                    h = 60 * (((g_ - b_) / delta) % 6)
                
                elif (cmax == g_):
                    
                    h = 60 * (((b_ - r_) / delta) + 2)
                
                elif (cmax == b_):
                    
                    h = 60 * (((r_ - g_) / delta) + 4)
                
                else:
                    
                    h = 0
                
                # lightness calculation
                l = (cmax + cmin) / 2
                
                # saturation calculation
                if (delta == 0):
                    
                    s = 0
                
                else:
                    
                    s = delta / (1 - abs(2*l - 1))
                    
                # color shift in a custom range
                if (h >= lower and h <= upper): 
                        
                    if ((shift + h) > 359):
                        
                        h = h + shift
                        h = h - 359
                        
                    else:
                        
                        h = h + shift
                
                    # conversion back to rgb
                    c = (1 - abs(2*l - 1)) * s
                    
                    x = c * (1 - abs(((h / 60) % 2) - 1))
                    
                    m = l - (c / 2)
                    
                    if (h >= 0 and h < 60):
                        
                        r_ = c
                        g_ = x
                        b_ = 0
                    
                    elif (h >= 60 and h < 120):
                        
                        r_ = x
                        g_ = c
                        b_ = 0
                    
                    elif (h >= 120 and h < 180):
                        
                        r_ = 0
                        g_ = c
                        b_ = x
                    
                    elif (h >= 180 and h < 240):
                        
                        r_ = 0
                        g_ = x
                        b_ = c
                        
                    elif (h >= 240 and h < 300):
                        
                        r_ = x
                        g_ = 0
                        b_ = c
                    
                    elif (h >= 300 and h < 360):
                        
                        r_ = c
                        g_ = 0
                        b_ = x
                    
                    else:
                        
                        r_ = 0
                        g_ = 0
                        b_ = 0
                    
                    # sets output image pixel to newly boosted pixel
                    matrix0[i], matrix0[i+1], matrix0[i+2] = (r_ + m) * 255, (g_ + m) * 255, (b_ + m) * 255
                
                else:
                    
                    # sets output image pixel to original, unmodified pixel
                    matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            # fills remaining output pixels to original pixel
            for i in range(0, int((region1 * len(matrix1)) / 3) * 3, 3):
                
                matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            for i in range(int((region2 * len(matrix1)) / 3) * 3, len(matrix1), 3):
                
                matrix0[i], matrix0[i+1], matrix0[i+2] = matrix1[i], matrix1[i+1], matrix1[i+2]
            
            # reshape output matrix0 to image dimensions
            matrix0 = matrix0.reshape(int(dims[1]), int(dims[0]) * 3)
                        
            # write proper PPM formatting for output file
            out.write('P3' + '\n')
            out.write(dims[0] + ' ' + dims[1] + '\n')
            out.write(str(matrix0.max()) + '\n')
            
            # iterate through each RGB value and add new lines when appropriate
            for i in range(len(matrix0)):
                
                for j in range(len(matrix0[i])):
                    
                    if j == (len(matrix0[i]) - 1):
                        
                        out.write(str(matrix0[i][j]) + '\n')
                    
                    else:
                        
                        out.write(str(matrix0[i][j]) + ' ')
            
            # close all files                    
            pic.close()
            out.close()
            
            # indicates successful operation
            return 1

        
def negative(image1, image0):
    '''Inverts a color image to negative
    
       Takes in an image file and creates a new output image file'''
    
    # opens input file for read and creates output file for write    
    try:
        
        pic = open(image1, 'r')
    
    except: 
        
        print()
        print("Input file not found. ", end='')
    
    else:
    
        out = open(image0, 'w')
    
        # verifies that image is PPM format
        if (pic.readline().strip() == 'P3'):
            
            comment = pic.readline()
            
            if (comment[0] == '#'):
                
                dims = pic.readline().split()
            
            else:
                
                # reads dimensions of image
                dims = comment.split()
                
            # creates a default matrix with dimensions given by the image
            matrix1 = np.array(range(int(dims[0]) * int(dims[1]) * 3))
            
            # creates an identical matrix for output image
            matrix0 = matrix1.copy()
            
            # skips past line indicating maximum color value
            pic.readline()
            
            # reads pixel values of each image into a list
            body = pic.read().split()
            
            # iterates through each RGB value of image and adds to 
            # matrix1 numpy array
            
            i = 0
                
            for rgb in body:
                
                matrix1[i] = int(rgb)
                i += 1
            
            # iterates through every pixel (every 3 RGB values)
            for i in range(0, len(matrix1), 3):
                
                # inverts each pixel            
                r = 255 - matrix1[i]
                g = 255 - matrix1[i+1]
                b = 255 - matrix1[i+2]
                
                if (r < 0):
                    
                    r = 0
                
                if (g < 0):
                    
                    g = 0
                
                if (b < 0):
                    
                    b = 0
                
                # sets output pixel to inverted pixel
                matrix0[i], matrix0[i+1], matrix0[i+2] = r, g, b
            
            # reshape output matrix0 to image dimensions
            matrix0 = matrix0.reshape(int(dims[1]), int(dims[0]) * 3)
                        
            # write proper PPM formatting for output file
            out.write('P3' + '\n')
            out.write(dims[0] + ' ' + dims[1] + '\n')
            out.write(str(matrix0.max()) + '\n')
            
            # iterate through each RGB value and add new lines when appropriate
            for i in range(len(matrix0)):
                
                for j in range(len(matrix0[i])):
                    
                    if j == (len(matrix0[i]) - 1):
                        
                        out.write(str(matrix0[i][j]) + '\n')
                    
                    else:
                        
                        out.write(str(matrix0[i][j]) + ' ')
            
            # close all files                    
            pic.close()
            out.close()
            
            # indicates successful completion of operation
            return 1


def rotate(image1, image0):
    '''Rotates an image 90, 180, 270 degrees

       Takes in an image file and creates a new output image file'''
    
    try:
        
        pic = open(image1, 'r')
    
    except: 
        
        print()
        print("Input file not found. ", end='')
    
    else:
    
        out = open(image0, 'w')
    
        # verifies that image is PPM format
        if (pic.readline().strip() == 'P3'):
            
            comment = pic.readline()
            
            if (comment[0] == '#'):
                
                dims = pic.readline().split()
            
            else:
                
                # reads dimensions of image
                dims = comment.split()
                
            # creates a default matrix with dimensions given by the image
            matrix1 = np.array(range(int(dims[0]) * int(dims[1]) * 3))
                    
            # skips past line indicating maximum color value
            pic.readline()
            
            # reads pixel values of each image into a list
            body = pic.read().split()
            
            # iterates through each RGB value of image and adds to 
            # matrix1 numpy array        
            i = 0
                
            for rgb in body:
                
                matrix1[i] = int(rgb)
                i += 1        
            
            # creates an identical matrix for output image
            matrix0 = matrix1.copy()
            
            # reshape matrix numpy arrays to image dimensions
            matrix1 = matrix1.reshape(int(dims[1]), int(dims[0]) * 3)
            matrix0 = matrix0.reshape(int(dims[0]), int(dims[1]) * 3)
            
            # iterate through each line of pixels
            for i in range(len(matrix1)):
                
                # iterate through each pixel (every 3 RGB values)
                for j in range(0, len(matrix1[i]), 3):
                    
                    # set row of original image to column of output image,
                    # working backwards
                    matrix0[int(j/3)][(len(matrix0[0])-1)-(3*i)-2] = matrix1[i][j]
                    matrix0[int(j/3)][(len(matrix0[0])-1)-(3*i)-1] = matrix1[i][j+1]
                    matrix0[int(j/3)][(len(matrix0[0])-1)-(3*i)] = matrix1[i][j+2]
    
            # write proper PPM formatting for output file
            out.write('P3' + '\n')
            out.write(dims[1] + ' ' + dims[0] + '\n')
            out.write(str(matrix0.max()) + '\n')
            
            # iterate through each RGB value and add new lines when appropriate
            for i in range(len(matrix0)):
                
                for j in range(len(matrix0[i])):
                    
                    if j == (len(matrix0[i]) - 1):
                        
                        out.write(str(matrix0[i][j]) + '\n')
                    
                    else:
                        
                        out.write(str(matrix0[i][j]) + ' ')
            
            # close all files            
            pic.close()
            out.close()
            
            # indicates successful operation
            return 1
        
