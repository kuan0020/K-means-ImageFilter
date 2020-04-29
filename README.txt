````
Tommy Kuan (kuan0020@umn.edu)
Project 1: K-means clustering
````

This is program specifically filters .ppm images to k number of colors. This is done by applying k-means clustering algorithm to get k most-average numbers of color to filter the image. 

There are 3 files in this program:
1) run_k_means.py: 
   This is the main file. Run this code by typing "python3 run_k_means.py" in your terminal at the correct directory. You can follow the instructions given in the prompts to give the parameters to the program. **Note that the program is optimized for the user, there is no need to enter ".ppm" after a file name.**

2) k_means.py
   This file contains the k-means clustering algorithm needed to find the most-average color.

3) image_utils.py
   This file contains the utility functions to read and write to a .ppm file.

Notes:
If you want to run the code quickly keep the k-value below 10, code runtime increases significantly with higher k-values. Make sure you run the code in the right directory, if you are unsure of which directory you are at you can type pwd in terminal to check. However, this code also allows user to filter images from another directory, you just have to type the directory in the prompt. 

Extras:
I included some images that I filtered to test this program. The file format is "imagename_k_[num].ppm" where [num] represents the k-values, and images without "k_[num]" is the original image.
