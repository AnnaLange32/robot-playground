import sys
sys.path.append("/home/anna/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")

from naoqi import ALProxy
import time
import numpy as np
from PIL import Image


def capture_robot_camera_nao(NAO_IP, PORT):
    """ Capture images from Nao's TOP camera. Note that the Nao's
        camera resolution is lower than the Pepper robot.
        Remember you need to subscribe and unsubscribe respectively
        see, https://ai-coordinator.jp/pepper-ssd#i-3
    """
    SubID = "NAO"
    videoDevice_nao = ALProxy('ALVideoDevice', NAO_IP, PORT)
    # subscribe top camera, Image of 320*240px
    AL_kTopCamera, AL_kQVGA, Frame_Rates = 0, 1, 5  # 2.5  #10
    AL_kBGRColorSpace = 13  # Buffer contains triplet on the format 0xRRGGBB, equivalent to three unsigned char
    captureDevice_nao = videoDevice_nao.subscribeCamera(SubID, AL_kTopCamera, AL_kQVGA, AL_kBGRColorSpace,      Frame_Rates)

    width, height = 320, 240
    image = np.zeros((height, width, 3), np.uint8)
    result = videoDevice_nao.getImageRemote(captureDevice_nao)

    if result == None:
        print "Camera problem."
    elif result[6] == None:
        print "No image. "
    else:
        # translate value to mat
        values = map(ord, list(result[6]))
        i = 0
        for y in range(0, height):
            for x in range(0, width):
                image.itemset((y, x, 0), values[i + 0])
                image.itemset((y, x, 1), values[i + 1])
                image.itemset((y, x, 2), values[i + 2])
                i += 3

    # unsubscribe from the camera
    videoDevice_nao.unsubscribe(captureDevice_nao)
    return result[6], image

result, image = capture_robot_camera_nao("130.149.244.203", 9559)
img = Image.fromarray(image)
img.save('/home/anna/MultimodalTrust/naocam/naocapture.png')
left = 68
top = 40
right = 260
bottom = 231
img_res = img.crop((left, top, right, bottom)) 
img_res.save('/home/anna/MultimodalTrust/naocam/naocapture2.png')
#im = Image.open('/home/anna/MultimodalTrust/outputs/output_naocapture.png')



