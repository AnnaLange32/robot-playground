import sys
sys.path.append("/home/anna/pynaoqi-python2.7-2.5.7.1-linux64/lib/python2.7/site-packages")

from naoqi import ALProxy

def main():

    PORT=9559
    robotIP = "130.149.244.203" #"192.168.43.7"
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)

    # Go to rest position
    motionProxy.rest()


    print "::::::::::::::::::::::::::::::::::::::"
    print "          NAO Rest positon          "
    print "::::::::::::::::::::::::::::::::::::::"

if __name__ == "__main__":
    main()
