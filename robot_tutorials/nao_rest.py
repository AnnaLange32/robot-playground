from naoqi import ALProxy

def main():

    PORT=9559
    robotIP = "192.168.0.171" #"192.168.43.7"
    motionProxy  = ALProxy("ALMotion", robotIP, PORT)

    # Go to rest position
    motionProxy.rest()


    print "::::::::::::::::::::::::::::::::::::::"
    print "          NAO Rest positon          "
    print "::::::::::::::::::::::::::::::::::::::"

if __name__ == "__main__":
    main()
