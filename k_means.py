"""
Tommy Kuan (kuan0020@umn.edu)
Project: K-means clustering
"""

from image_utils import*

mean_list = []

def distance(colr1, colr2):
    """[Calculate how close is the colr1 to colr2 or vice versa]
    
    Arguments:
        colr1 {[tuple]} -- [Size 3 tuple with (r,g,b)]
        colr2 {[tuple]} -- [Size 3 tuple with (r,g,b)]
    
    Returns:
        [float/int] -- [The "distance" between two input colors]
    """
    dist = ( (colr1[0] - colr2[0])**2 + (colr1[1] - colr2[1])**2 + (colr1[2] - colr2[2])**2 )**0.5
    return dist

def k_means(image, k):
    """[K-means algorithm: k represent the number of nodes/cluster in the data. This function first make random guesses for k number
        of nodes and then by looping and updating the nodes base on k-number of the most-average color in the image list of list. 
        In the end, when the pixels are all assigned to its cluster's color base on their closeness to that color, this function
        outputs a new image list of list that is filtered to k-number of colors only]
    
    Arguments:
        image {[list of list]} -- [2D list that contains the color (r,g,b) info for every pixels in the input image]
        k {[int]} -- [number of nodes/clusters, or in this case, number of most-average colors]
    
    Returns:
        [list of list] -- [final assigned list of list (filtered image)]
    """
    
    global mean_list
    mean_list = [None]*k
    col, row = get_width_height(image)
    
    # Set up assignment list of list with the same size as image
    assignments = []
    for columnNum in range(col):
        height = [BLACK] * row
        assignments.append(height)
    
    # Distance list to compare the distance between each pixel with each mean list color
    # Each element[i] will contain that pixel's closeness to mean list color[i]
    dist = [None]*k
    
    # Initializing first random mean list
    for x in range(k):
        mean_list[x] = random_color()
    
    # Loops through every pixel in the image and calculate the closeness between each pixels to mean list[i] and assign to dist[i]
    # closest_noc finds the closest color to one of the color in mean list and assign that pixel's position to assignments[][]
    for x in range(row):
        for y in range(col):
            for noc in range(k):
                dist[noc] = distance(image[y][x], mean_list[noc])
            closest_noc = dist.index(min(dist))
            assignments[y][x] = mean_list[closest_noc]
    
    new_mean = []
    
    # This is a do-while loop that will continously update mean list and assignment[][] until 
    # 1) assignment[][] stops changing, which is when it is at its most-average colors for each pixels
    # 2) new_mean[] has no duplicates. Sometimes random start can give you a duplicate after averaging the colors.
    while True:
        old_assignments = assignments.copy()
        new_mean = update_means(assignments, image, k)
        assignments = update_assignments(image, new_mean, k)
        
        if assignments == old_assignments and len(new_mean) == len(set(new_mean)):
            break
        
    return assignments


def average_color(color_list, color_count):
    """[Calculate the average color (element based)]
    
    Arguments:
        color_list {[tuple]} -- [color list with tuples(r,g,b)]
        color_count {[int]} -- [number of colors in color list ]
    
    Returns:
        [tuple] -- [average (r,g,b) tuple of color]
    """
    avg_r = sum([col[0] for col in color_list]) // color_count
    avg_g = sum([col[1] for col in color_list]) // color_count
    avg_b = sum([col[2] for col in color_list]) // color_count
    
    avg_color = (avg_r, avg_g, avg_b)
    return avg_color
    
def update_means(assignments, image, k):
    """[Updates the mean list base on the most average color in assignments[]]
    
    Arguments:
        assignments {[list of list]} -- [Colors assigned to each pixel in the size of the input image]
        image {[list of list]} -- [2D list that contains the color (r,g,b) info for every pixels in the input image]
        k {[int]} -- [number of nodes/clusters, or in this case, number of most-average colors]
    
    Returns:
        [list] -- [Updated mean list[]]
    """
    global mean_list
    col, row = get_width_height(image)
    color_count = [0]*k
    temp = []

    # Get the average color for each pixels in assignments[][] that is assigned to mean list[i], replace mean list[i] 
    # with the new average color
    for noc in range(k):
        for x in range(row):
            for y in range(col):
                if assignments[y][x] == mean_list[noc]:
                    temp.append(image[y][x])
                    color_count[noc] = color_count[noc] + 1
        if color_count[noc] == 0:
            mean_list[noc] = (0,0,0)
        else:
            mean_list[noc] = average_color(temp, color_count[noc])
        temp = []
    
    # If by chance there is a duplicate color in mean list (of course both same color is also an average), this code deletes the duplicate.
    # This allows the program to recalculate another color that is average in the input image
    for x in range(len(mean_list)):
        for y in range(x + 1, len(mean_list)):
            if mean_list[x] == mean_list[y]:
                mean_list.pop(y)
                mean_list.append((0,0,0))
                
    return mean_list.copy()

def update_assignments(image, means, k):
    """[Updates the assignment[][] base on the pixels' closeness to mean list[i]]
    
    Arguments:
        image {[list of list]} -- [2D list that contains the color (r,g,b) info for every pixels in the input image]
        means {[list]} -- [List of the current most average colors]
        k {[int]} -- [number of nodes/clusters, or in this case, number of most-average colors]
    
    Returns:
        [list of list] -- [updated assignments[][] that has the most average color assigned to each pixels]
    """
    dist = [None]*k
    col, row = get_width_height(image)
    
    # Initialize assignments to the same size as image
    assignments = []
    for columnNum in range(col):
        height = [BLACK] * row
        assignments.append(height)
    
    # Assigns the closest color from mean list to assignments[][]
    for x in range(row):
        for y in range(col):
            for noc in range(k):
                dist[noc] = distance(image[y][x], means[noc])
            closest_noc = dist.index(min(dist))
            assignments[y][x] = means[closest_noc]
    return assignments

