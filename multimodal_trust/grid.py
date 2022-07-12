import cv2
import numpy as np
import os
import time
import constants
import matplotlib.pyplot as plt

'''This script contains several functions for displaying the grids and images and preprocessing them.'''

cv2.CV_LOAD_IMAGE_GRAYSCALE = 0
cv2.CV_LOAD_IMAGE_COLOR = 0

def bipolarize_pattern_robot(pattern_name):

    """ Convert percieved patterns images into Bipolarized (-1, 1) inputs.
    Parameters
    -----------
    pattern_name: filename
    location where the image is located
    Return
    -------
    images in format for Hopfield Network"""

    gimg = cv2.imread(pattern_name, cv2.CV_LOAD_IMAGE_GRAYSCALE)

    rimg = cv2.resize(gimg, constants.rsize)
    bimg = cv2.threshold(rimg, 125, 255, cv2.THRESH_BINARY)[1]

    # uncomment the below lines to see the binary images
    # cv2.imshow("bin robo", bimg)
    # cv2.imshow("gray robot", gimg)
    # cv2.imshow("grsize", rimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # convert 255 to -1 and 0 to 1
    bimg = bimg.astype('int64')
    nonz_inds = bimg.nonzero()
    bimg[nonz_inds], bimg[bimg == 0] = -1, 1  # convert 255 to -1 and 0 to 1

    return bimg.flatten()



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
    bipolar_grid = np.zeros((constants.length, constants.rsize[0]*constants.rsize[0]))
    image_h = []
    image_number = 0

    for i in range(constants.length):
        # image directory with image names as ordered ints
        filename = constants.store_grids + '%s' % image_number + '.png'
        print(filename)
        image_number += 1
        bipolar_image = bipolarize_pattern_robot(filename)
        image = cv2.imread(filename, cv2.IMREAD_COLOR)
        img = cv2.resize(image, constants.rsize)
        white = [255, 255, 255]
        img = cv2.copyMakeBorder(img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=white)
        image_h.append(img)
        bipolar_grid[i, :] = bipolar_image
    image_grid_final = cv2.hconcat(image_h)
    print('size grid:', image_grid_final.size)
    filename = constants.store_grids + 'basegrid.png'
    cv2.imwrite(filename, image_grid_final)
    print("The grid has been generated.")
    return image_grid_final, bipolar_grid


def make_yellow_frames(yellow_number):

    """ Concatenate pattern images into grid, with a yellow frame around each image once
     and saves them in a specified location. Needs to be run before Sarsa.

    Parameters
    -----------
    yellow_number: number of image that should be framed in yellow
    """
    image_h = []
    image_number = 0

    for i in range(constants.length):

        # image directory with image names as ordered ints
        filename = constants.store_grids + '%s' % image_number + '.png'
        image = cv2.imread(filename, cv2.IMREAD_COLOR)
        rimg = cv2.resize(image, constants.rsize)
        if image_number == yellow_number:
            yellow = [130, 255, 255]
            rimg = cv2.copyMakeBorder(rimg, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=yellow)
        else:
            white = [255, 255, 255]
            rimg = cv2.copyMakeBorder(rimg, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=white)
        image_h.append(rimg)
        image_number += 1
        image_number = int(image_number)
    image_grid_final = cv2.hconcat(image_h)
    filename = constants.store_grids + 'yellowgrid%s.png' % yellow_number
    cv2.imwrite(filename, image_grid_final)
    return image_grid_final


def display_image(path, image_name, timewait):
    """Displays the chosen image in full screen
    Parameters
    ----------
    path: filename
    location where the image is located
    image_number: output from the Hopfield, the number of the image to be displayed.

    """
    # image directory with image names as ordered ints
    filename = path + '%s' % image_name + '.png'
    print(filename)
    # chosen_image = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
    show_img = 'eog --fullscreen ' + filename + ' &'
    time.sleep(timewait)  # this is used for training don't change
    os.system(show_img)



def display_grid(image_name):
    """Displays the chosen image in full screen
    Parameters
    ----------
    image_number: output from the Hopfield, the number of the image to be displayed.

    """
    # image directory with image names as ordered ints
    filename = constants.store_grids + '%s' % image_name + '.png'
    print(filename)
    # chosen_image = cv2.imread(filename, cv2.CV_LOAD_IMAGE_COLOR)
    show_img = 'eog --fullscreen ' + filename + ' &'
    # time.sleep(0.1)
    os.system(show_img)



# image_grid, order, bipolar_grid_output = random_grid_maker(grid_width=3, grid_length=7, image_size=(30, 30))
# cv2.imshow("Grid", image_grid)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# display_image(order, 2, 0)3,7,(200,200)


def bipolarize_pattern_robot_train(path, no_imgs):

    """ Convert list of pattern images for training into Bipolarized (-1, 1) inputs.
    Parameters
    -----------
    path: filename
    location where the image is located
    no_imgs: integer
    amount of training images
    rsize: tuple
    size of the individual image

    Return
    -------
    images in format for Hopfield Network"""

    print('This is generating the training images.')
    images = np.zeros((constants.rsize[0] * constants.rsize[1], no_imgs))
    for j in range(no_imgs):
        # image directory with image names as ordered ints
        filename = path + '%s' % j + '.png'
        image = cv2.imread(filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        print(image.shape)
        rimg = cv2.resize(image, constants.rsize, interpolation = cv2.INTER_AREA)
        bimg = cv2.threshold(rimg, 125, 255, cv2.THRESH_BINARY)[1]
        # convert 255 to -1 and 0 to 1
        bimg = bimg.astype('int64')
        nonz_inds = bimg.nonzero()
        bimg[nonz_inds], bimg[bimg == 0] = -1, 1  # convert 255 to -1 and 0 to 1
        # plt.imshow(bimg, cmap='Greys')
        # plt.show()
        savename = path + 'check%s.png' % j

        plt.imsave(savename, bimg, cmap='Greys')
        images[:, j] = bimg.flatten()

    return images