import numpy as np
import time
import os
from termcolor import colored, cprint
import sounddevice as sd
from scipy.io.wavfile import write
import constants
from naoqi import ALProxy

''' This scripts contains functions to record either a human or a robot
    and save the recorded audio automatically in the specified path.'''

def audio_human(audiopath, audion):


    #name = raw_input("Press enter to switch the pattern: ")
    text = colored(' \n Say the pattern label: ' , 'red', attrs=['reverse', 'blink'])#+ constants.audio_labels[audion]

    print(text)

    myrecording = sd.rec(int(constants.seconds * constants.fs), samplerate=constants.fs, channels=2)

    #tts.say(audio_labels[i])

    sd.wait()  # Wait until recording is finished

    #time.sleep(2) # allow some sleep time to avoid saving errors

    write(audiopath + str(audion)+ '.wav' , constants.fs, myrecording)  # Save as WAV file

    #audio_file = 'ffmpeg -loglevel quiet -f alsa -i default -t 3 ' + data_exp + str(i + 1) + '.wav -y &'

    #os.system(audio_file)

    #time.sleep(1) # this is the magic number

    print " ...... audio captured"

    return myrecording




def audio_pepper(audiopath, audion):

    fs = 44100  # Sample rate

    seconds = 3  # Duration of recording

    PI_PEPPER, PORT = constants.IP2, constants.PORT



    tts = ALProxy("ALTextToSpeech", PI_PEPPER, PORT)

    tts.setLanguage("English")



    #name = raw_input("Press enter to switch the pattern: ")

    text = colored(' \n Say the pattern label: ' + constants.audio_labels[audion], 'red', attrs=['reverse', 'blink'])

    print(text)

    myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
    time.sleep(1)
    tts.say(constants.audio_labels[audion])

    sd.wait()  # Wait until recording is finished

    myrecording = myrecording[int(fs*0.5):, :]
    write(audiopath + str(audion)+ '.wav' , fs, myrecording)  # Save as WAV file

    print(myrecording.shape)
    #audio_file = 'ffmpeg -loglevel quiet -f alsa -i default -t 3 ' + data_exp + str(i + 1) + '.wav -y &'

    #os.system(audio_file)

    #time.sleep(1) # this is the magic number

    print "audio captured"




        # pause_pattern = raw_input("::::::::::::::::::Press enter then label the pattern:::::::::::")




    #tts.say("trial")






