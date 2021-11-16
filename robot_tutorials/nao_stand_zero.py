import sys
sys.path.append("/home/anna/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")
from naoqi import ALProxy

def main():

    PORT=9559
    robotIP = "172.20.10.5" #"192.168.43.7"
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)
    posture_service = ALProxy("ALRobotPosture", robotIP, PORT)


    # Go to rest position
    #motionProxy.StandZero(
    posture_service.goToPosture("StandZero", 0.5)	

    print "::::::::::::::::::::::::::::::::::::::"
    print "          NAO movement done          "
    print "::::::::::::::::::::::::::::::::::::::"

if __name__ == "__main__":
    main()
