
import numpy as np
import os
#from naoqi import ALProxy

# The SARSA algorithm can be reached via the below link.
# https://github.com/muratkirtay/ADAPTIVE2019/tree/master/Source



def show_monitor_img(img):
    """ Show the image in fullscreen on the experiment monitor"""
    show_img = 'eog --fullscreen ' + img + ' &'
    # time.sleep(0.1)
    os.system(show_img)

show_monitor_img('/home/anna/MultimodalTrust//Visual/Images/5.png')




