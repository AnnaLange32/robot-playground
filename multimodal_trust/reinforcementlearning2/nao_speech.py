import sys
sys.path.append("/home/anna/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
import constants
from naoqi import ALProxy
import time

def speech_choose_image(image_number):


	tts = ALProxy("ALTextToSpeech", constants.IP, constants.PORT)
	animation = ALProxy("ALAnimationPlayer", constants.IP, constants.PORT)
	posture = ALProxy("ALRobotPosture", constants.IP, constants.PORT)
	tts.setLanguage("English")

	user_msg = 'I choose image %s' % image_number
	#user_msg2 = "Before starting, I would like to ask a question."
	#user_msg3 = ""
	
	#tts.say(str(user_msg)
	#tts.say(str(user_msg2))
	time.sleep(3)
	tts.say(str(user_msg))


def speech_other(text):

	tts = ALProxy("ALTextToSpeech", constants.IP, constants.PORT)
	animation = ALProxy("ALAnimationPlayer", constants.IP, constants.PORT)
	posture = ALProxy("ALRobotPosture", constants.IP, constants.PORT)
	tts.setLanguage("English")

	# user_msg = 'I choose image %s' % image_number
	# user_msg2 = "Before starting, I would like to ask a question."
	# animation.run("animations/Stand/Gestures/Give_3", _async=True)

	user_msg3 = text

	# tts.say(str(user_msg)
	# tts.say(str(user_msg2))
	time.sleep(3)
	tts.say(str(user_msg3))




