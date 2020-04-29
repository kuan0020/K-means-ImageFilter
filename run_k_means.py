"""
Tommy Kuan (kuan0020@umn.edu)
Project: K-means clustering
"""

from k_means import k_means
from image_utils import save_ppm, read_ppm
import os

file_found = False

print("This program specifically filters an user input image (.ppm) into the number of color pallets of choice. It uses K-means clustering algorithm to decide the most-average color to be filter base on the input image.")
print()

while file_found == False:
    try:
        input_filename = input("Enter input image name (w/o .ppm):")
        image = read_ppm(input_filename + ".ppm")
        file_found = True
    except FileNotFoundError:
        print("ERROR: File",input_filename,"does not exist, please input the filename WITHOUT .ppm or check your directory")
        print()
        file_found = False

while True:
    k_num = input("Enter number of colors to filter (whole numbers only):")
    
    if k_num.isnumeric():  
        if '.' not in k_num:
            break
        else:
           print("ERROR: Please enter an integer") 
    else:
        print("ERROR: Please enter an integer")

out_filename = input("Enter output image name (w/o .ppm):")

new_image = k_means(image, int(k_num))
save_ppm(out_filename + ".ppm", new_image)

if os.path.isfile(os.getcwd() + "/" + out_filename + ".ppm"):
    print("Image saved in", os.getcwd() + "/" + out_filename, end=".ppm\n")
elif os.path.isfile(out_filename + ".ppm"):
    print("Image saved in", out_filename, end=".ppm\n")
else:
    print("ERROR: Image process error, please restart the program")


