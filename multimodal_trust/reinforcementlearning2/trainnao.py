from grid import *  # contains code relating to the images and grids to be displayed
from nao_imagecapture import *  # contains code to capture Nao vision
import time
from PIL import Image
import constants
'''This script trains the Hopfield Network. Nao needs to be placed in from of an external monitor.
 The training images will be displayed on the external monitor. '''

cv2.CV_LOAD_IMAGE_GRAYSCALE = 0
cv2.CV_LOAD_IMAGE_COLOR = 0

# capture images for training of the Hopfield Net

for nimage in range(0, constants.ntrainimgs):
    display_image(constants.get_trainimgs, nimage, constants.time2)
    time.sleep(constants.time1)
    result, image = capture_robot_camera_nao(constants.IP, constants.PORT)
    img = Image.fromarray(image)
    img_res = img.crop((constants.left, constants.top, constants.right, constants.bottom))
    filename = constants.store_trainimgs + '%s' % nimage + '.png'
    img_res.save(filename)

# bipolarise the training images and format them ready to be passed in the Hopfield net

train_imgs = bipolarize_pattern_robot_train(constants.store_trainimgs, constants.ntrainimgs)

np.save('/home/anna/MultimodalTrust/training/train_imgs.npy', train_imgs)
