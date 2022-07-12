from grid import *
import os
import cv2
from wn import *
cv2.CV_LOAD_IMAGE_GRAYSCALE = 0
cv2.CV_LOAD_IMAGE_COLOR = 0
import matplotlib.pyplot as plt




# generating the basegrid
#noise_img = sp_noise(constants.get_gameimages, 4, constants.probabilities[10])

#filename = constants.store_grids + '%s' % 10 + '.png'
#cv2.imwrite(filename, noise_img)


# generating the yellow framed grids

#for i in range(0,constants.length):
 #   make_yellow_frames(i)


def ordered_grid_maker():
    """ Concatenate pattern images into a grid and saves it in a chosen location.
    This script needs to be used before running the Sarsa.

    Returns
    -----------
    image_grid_final: image
    of final grid
    bipolar_grid: matrix
    of final grid
    """

    print('This is generating the grid.')
    bipolar_grid = np.zeros((constants.length,constants.rsize[0]*constants.rsize[0]))#constants.rsize[0]*constants.rsize[0]

    image_h = []
    image_number = 0

    for i in range(constants.length):
        # image directory with image names as ordered ints
        filename = constants.store_grids + '%s' % image_number + '.png'
        print(filename)
        image_number += 1
        bipolar_image = bipolarize_pattern_robot(filename)
        image = cv2.imread(filename, cv2.IMREAD_COLOR)
        img = cv2.resize(image, (200,200))
        white = [255, 255, 255]
        img = cv2.copyMakeBorder(img, 2, 2, 2, 2, cv2.BORDER_CONSTANT, value=white)
        image_h.append(img)
        bipolar_grid[i, :] = bipolar_image
    image_grid_final = cv2.hconcat(image_h)
    print('size grid:', image_grid_final.size)
    filename = constants.store_grids + 'basegrid.png'
    cv2.imwrite(filename, image_grid_final)
    print("The grid has been generated.")
    return image_grid_final, bipolar_grid

ordered_grid_maker()