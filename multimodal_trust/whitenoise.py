# importing the libraries
import cv2
import numpy as np
import random
import matplotlib.pyplot as plt
import constants

cv2.CV_LOAD_IMAGE_GRAYSCALE = 0
cv2.CV_LOAD_IMAGE_COLOR = 0


'''This script contains the functions for adding the noise to the game images.'''

def sp_noise(image_path, image_number,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''
    filename = image_path + '%s' % image_number + '.png'
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    #image = cv2.resize(image, constants.rsize) # if this is added the image will be the size of the finally processed
    # image so the noise percentage will be adapted to this size
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob/2
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob/2:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output

def sp_noise_game(image,prob):
    '''
    Add salt and pepper noise to image
    prob: Probability of the noise
    '''

    #image = cv2.resize(image, constants.rsize) # if this is added the image will be the size of the finally processed
    # image so the noise percentage will be adapted to this size
    output = np.zeros(image.shape,np.uint8)
    thres = 1 - prob/2
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            rdn = random.random()
            if rdn < prob/2:
                output[i][j] = 0
            elif rdn > thres:
                output[i][j] = 255
            else:
                output[i][j] = image[i][j]
    return output


def bipolarize_pattern_robot_image(pattern_name, rsize):
    """ Convert percieved patterns images into Bipolarized (-1, 1) inputs. """

    # the ROI coordinates of the percieved patterns.
     # crop_y1, crop_y2 = 232, 452
    # crop_x1, crop_x2 = 238, 464

    gimg = cv2.imread(pattern_name, cv2.CV_LOAD_IMAGE_GRAYSCALE)

    # roi_image = gimg[crop_y1:crop_y2, crop_x1:crop_x2]
    # check for images have the same size
    print(gimg.shape)
    print(pattern_name)
    rimg = cv2.resize(gimg, rsize)
    bimg = cv2.threshold(rimg, 125, 255, cv2.THRESH_BINARY)[1]

    # uncomment the below lines to see the binary images
    # cv2.imshow("bin robo", bimg)
    # cv2.imshow("gray robot", gimg)
    # cv2.imshow("grsize", rimg)
    # cv2.waitKey(0)
    # cv2.destroyAllWindows()

    # convert 255 to -1 and 0 to 1
    #bimg = bimg.astype('int64')
    #nonz_inds = bimg.nonzero()
    #bimg[nonz_inds], bimg[bimg == 0] = 1, -1  # convert 255 to -1 and 0 to 1
    return bimg


def apply_noise(state_no):

    img_no = random.randint(0,4)

    # apply noise
    for i in constants.state_numbers:
        if state_no = i:
            image =  sp_noise(img_no, constants.probabilities[i])
    return image
