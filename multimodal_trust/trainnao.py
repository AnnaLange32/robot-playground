from grid import *  # contains code relating to the images and grids to be displayed
from nao_imagecapture import *  # contains code to capture Nao vision
import time
from PIL import Image
import constants
from recaudio import audio_pepper
import constants
from audio import *

'''This script trains the Hopfield Network. The palying Nao needs to be placed in front of an external monitor. 
 The training images will be displayed on the external monitor. The speaking Nao needs to be equipped with a micro and
 placed near the playing Nao. The speaking Nao will say each word once. The images and sound will be cncatenated and saved.'''

cv2.CV_LOAD_IMAGE_GRAYSCALE = 0
cv2.CV_LOAD_IMAGE_COLOR = 0

# capture images for training of the Hopfield Net

for nimage in range(0, constants.ntrainimgs):
    display_image(constants.get_trainimgs, nimage, constants.time2)
    time.sleep(constants.time1)
    result, image = capture_robot_camera_nao(constants.IP, constants.PORT)
    img = Image.fromarray(image)
    img_res = img.crop((constants.left, constants.top, constants.right, constants.bottom))
    filename = constants.store_vtrainimgs + '%s' % nimage + '.png'
    img_res.save(filename)

time.sleep(1)

for nimage in (0,0,1,2,3,4):
#    time.sleep(constants.time1)
#    audio_pepper(constants.store_audio, nimage)
#    preprocess_audio_data(constants.store_audio, nimage)
     concat_audio_visual(constants.store_audio, constants.store_vtrainimgs, constants.store_vatrainimgs, nimage)

#bipolarise the training images and format them ready to be passed in the Hopfield net

train_imgs = bipolarize_pattern_robot_train(constants.store_vatrainimgs, constants.ntrainimgs)


np.save('/home/anna/nao_trust_2/multimodal_trust/store_train_audioimg/train_imgs.npy', train_imgs)
