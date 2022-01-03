from grid import *
import os
cv2.CV_LOAD_IMAGE_GRAYSCALE = 0
cv2.CV_LOAD_IMAGE_COLOR = 0
import matplotlib.pyplot as plt



for i in range(0,21):
    filename = '/home/anna/MultimodalTrust/Visual/Imagesv3/%s' % i + '.png'
    gimg = cv2.imread(filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    print(gimg.shape)


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
    bimg = bimg.astype('int64')
    nonz_inds = bimg.nonzero()
    bimg[nonz_inds], bimg[bimg == 0] = -1, 1  # convert 255 to -1 and 0 to 1

    return bimg

for i in range(0,21):
    filename = '/home/anna/MultimodalTrust/Visual/Imagesv3/%s' % i + '.png'
    gimg =bipolarize_pattern_robot_image(filename, (70,70))
    plt.imshow(gimg, cmap = 'Greys')
    savename ='/home/anna/MultimodalTrust/Visual/prebipolar/%s' % i + '.png'
    #plt.savefig(savename)
    #cv2.imwrite(savename, gimg)
    plt.imsave(savename, gimg, cmap = 'Greys')

    plt.show()

# generating the basegrid

ordered_grid_maker(width, length, rsize)

# generating the yellow framed grids

for i in range(0,21):
    make_yellow_frames(width, length, rsize, i)
