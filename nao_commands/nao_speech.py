import sys
sys.path.append("/home/anna/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")

from naoqi import ALProxy
import time

def main():


	IP, PORT = "130.149.244.203", 9559 
	tts = ALProxy("ALTextToSpeech", IP, PORT)
	animation = ALProxy("ALAnimationPlayer", IP, PORT)
	posture = ALProxy("ALRobotPosture", IP, PORT)
	tts.setLanguage("English")

	user_msg = "Hello. I am Nao. We will start the experiment soon."
	#user_msg2 = "Before starting, I would like to ask a question."
	#animation.run("animations/Stand/Gestures/Give_3", _async=True)

	user_msg3 = "When I first met my spottie ottie dopalicious angel."
	
	#tts.say(str(user_msg)
	#tts.say(str(user_msg2))
	time.sleep(3)
	tts.say(str(user_msg3))

	


if __name__ == '__main__':
	main()
