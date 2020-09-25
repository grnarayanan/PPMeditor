"""
Created on Mon Aug 10 16:38:20 2020

@author: ganes

Effects Application v2.0

Editor program allows user to pick a desired effect, 
provide input files, and develops an output image. 
"""


from .effects import object_filter, shades_of_gray, horizontal_flip
from .effects import saturate_blues, saturate_greens, saturate_reds
from .effects import saturate_custom, color_shift, negative, rotate


def main():
    
    # welcome message and prompt user for effect
    print()
    print("\033[1mPortable Pixmap (PPM) Image Editor!\033[0m")
    print()
    print("\033[4mList of effects available:\033[0m")
    print("1) object_filter")
    print("2) shades_of_gray")
    print("3) horizontal_flip")
    print("4) saturate_blues")
    print("5) saturate_greens")
    print("6) saturate_reds")
    print("7) saturate_custom")
    print("8) color_shift")
    print("9) negative")
    print("10) rotate_90")
    
    choice = None
    run = 0
    
    while ((type(choice) != int) or (choice != 1 and choice != 2 and 
            choice != 3 and choice != 4 and choice != 5 and choice != 6 and 
            choice != 7 and choice != 8 and choice != 9 and choice != 10)):
        
        try:
            
            choice = int(input("Enter a number: "))
            
            # reask for input if invalid selection
            while (choice != 1 and choice != 2 and choice != 3 and 
                   choice != 4 and choice != 5 and choice != 6 and choice != 7 
                   and choice != 8 and choice != 9 and choice != 10):
                
                print("Invalid choice. Please try again.")
                choice = int(input("Enter a number: "))
                
        except:
            
            choice = int(input("Invalid choice. Please enter an integer 1-10: "))

    # if object_filter chosen, ask for 3 input files and 1 output file
    # then execute function    
    if choice == 1:
        
        infile1 = input("Enter 1st input file name: ")
        infile2 = input("Enter 2nd input file name: ")
        infile3 = input("Enter 3rd input file name: ")
        name = input("Enter name of output file: ")
        
        infile1 = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile1
        infile2 = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile2
        infile3 = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile3
        outfile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + name
        
        run = object_filter(infile1, infile2, infile3, outfile)
    
    # if shades_of_gray chosen, ask for 1 input file and 1 output file
    # then execute function
    if choice == 2:
        
        infile = input("Enter an input file name: ")
        name = input("Enter name of output file: ")
        
        infile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile
        outfile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + name
        
        run = shades_of_gray(infile, outfile)
    
    # if horizontal_flip chosen, ask for 1 input file and 1 output file
    # then execute function    
    if choice == 3:
        
        infile = input("Enter an input file name: ")
        name = input("Enter name of output file: ")
        
        infile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile
        outfile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + name
        
        run = horizontal_flip(infile, outfile)
    
    # if saturate_blues chosen, ask for 1 input file and 1 output file
    # then execute function    
    if choice == 4:
        
        infile = input("Enter an input file name: ")
        name = input("Enter name of output file: ")
        
        infile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile
        outfile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + name
        
        try:
            
            sat = int(input("Saturation boost %: "))
            region = float(input("Region: "))
        
        except: 
            
            print()
            print("Invalid entry for one or more fields. ", end='')
        
        else:
            
            run = saturate_blues(infile, outfile, sat, region)

    # if saturate_greens chosen, ask for 1 input file and 1 output file
    # then execute function    
    if choice == 5:
        
        infile = input("Enter an input file name: ")
        name = input("Enter name of output file: ")
        
        infile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile
        outfile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + name
        
        try:
            
            sat = int(input("Saturation boost %: "))
            region = float(input("Region: "))
        
        except: 
            
            print()
            print("Invalid entry for one or more fields. ", end='')
        
        else:
            
            run = saturate_greens(infile, outfile, sat, region)
    
    # if saturate_reds chosen, ask for 1 input file and 1 output file
    # then execute function    
    if choice == 6:
        
        infile = input("Enter an input file name: ")
        name = input("Enter name of output file: ")
        
        infile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile
        outfile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + name
        
        try:
            
            sat = int(input("Saturation boost %: "))
            region = float(input("Region: "))
        
        except: 
            
            print()
            print("Invalid entry for one or more fields. ", end='')
        
        else:
            
            run = saturate_reds(infile, outfile, sat, region)

    # if saturate_custom chosen, ask for 1 input file and 1 output file
    # then execute function    
    if choice == 7:
        
        infile = input("Enter an input file name: ")
        name = input("Enter name of output file: ")
        
        infile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile
        outfile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + name
        
        try: 
            
            low = int(input("Lower bound: "))
            up = int(input("Upper bound: "))
            sat = int(input("Saturation boost %: "))
            region = float(input("Region: "))
        
        except: 
            
            print()
            print("Invalid entry for one or more fields. ", end='')
        
        else:
        
            run = saturate_custom(infile, outfile, low, up, sat, region)
    
    # if color_shift chosen, ask for 1 input file and 1 output file
    # then execute function    
    if choice == 8:
        
        infile = input("Enter an input file name: ")
        name = input("Enter name of output file: ")
        
        infile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile
        outfile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + name
        
        try: 
            
            low = int(input("Lower bound: "))
            up = int(input("Upper bound: "))
            shift = int(input("Color shift: "))
            region1 = float(input("Boundary 1: "))
            region2 = float(input("Boundary 2: "))
        
        except: 
            
            print()
            print("Invalid entry for one or more fields. ", end='')
        
        else:
            
            run = color_shift(infile, outfile, low, up, shift, region1, region2)
    
    # if negative chosen, ask for 1 input file and 1 output file
    # then execute function    
    if choice == 9:
        
        infile = input("Enter an input file name: ")
        name = input("Enter name of output file: ")
        
        infile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile
        outfile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + name
        
        run = negative(infile, outfile)
        
    # if rotate chosen, ask for 1 input file and 1 output file
    # then execute function    
    if choice == 10:
        
        infile = input("Enter an input file name: ")
        name = input("Enter name of output file: ")
        
        infile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + infile
        outfile = "C:\\Users\\ganes\\Documents\\Personal\\Projects\\PPMe\\images\\" + name
        
        run = rotate(infile, outfile)
                
    # print that output file has successfully been created
    if (run == 1):
        
        print()
        print(name + " created.")        
  
    else:
        
        print("Operation cancelled.")
          
main()
 