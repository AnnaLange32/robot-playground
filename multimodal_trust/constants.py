
# file locations
audio_path = '/home/anna/nao_trust_2/multimodal_trust/store_audio/'
get_gameimages = '/home/anna/nao_trust_2/multimodal_trust/gameimg/'  # bipolar, low res images for game play are saved here, need to be named with integer numbers (e.g. 1.png)
store_gameimages = '/home/anna/nao_trust_2/multimodal_trust/store_gameimg/'  # image storage for Nao captures
store_vagameimgs = '/home/anna/nao_trust_2/multimodal_trust/gameimg/gameimgva/' # concat image storage game, used in Hopfield

store_grids = '/home/anna/nao_trust_2/multimodal_trust/gamegrid/'  # location of all grids
get_trainimgs = '/home/anna/nao_trust_2/multimodal_trust/trainimg/' # location of training images
store_vtrainimgs = '/home/anna/nao_trust_2/multimodal_trust/store_trainimg/' # location of training images
store_vatrainimgs = '/home/anna/nao_trust_2/multimodal_trust/store_train_audioimg/' # location of training images visual audio

store_captured = '/home/anna/nao_trust_2/multimodal_trust/store_captured/'
outputs_location = '/home/anna/nao_trust_2/multimodal_trust/outputs/'
store_audio = '/home/anna/nao_trust_2/multimodal_trust/store_audio/' # image storage for human speech training

# Nao set up
IP = "192.168.0.165" # '141.23.190.106' #'172.20.10.5' #  # Nao's IP address, read nao_tutorial1 for more
IP2 = "192.168.0.171" # '141.23.190.106' #'172.20.10.5' #  # Nao's IP address, read nao_tutorial1 for more
PORT = 9559  # Nao port, should remain unchanged

# The coordinates for cropping the image to the correct frame (manually generated from a captured example)
left = 70  # x left
top = 55  # y top
right = 255  # x right
bottom = 240  # y bottom

# time variables these are magic numbers that I trialled
time1 = 0.35  # time sleep after grid is shown
time2 = 0.5  # time to wait after image display
time3 = 2 #time wait after grid display
time4 = 2
time5 = 5
time6 = 0.3
time7 = 3


length = 11  # the length of the game grid
# Note: width x length images need to be located in get_gameimages, named 0.png to width x length in integers
nruns = 10 # number of runs
iterations = 20 # iteration to run the SARSA for
repeats = 3 # new repeat = new q-matrix for this 'run'
rsize = (32, 32)  # size of the images, the images displayed on screen should be in the same format
ntrainimgs = 5  # number of images that the Hopfield net is trained with
epsilon = 0.3  # exploration parameter
gamma = 0.4  # discounting
probabilities = (0, 0.05, 0.1, 0.2, 0.25, 0.5, 0.6, 0.75, 0.7, 0.8, 0.85)
state_numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


#audio constants
fs = 44100  # Sample rate
seconds = 3  # Duration of recording
conditions = ['Trustworthy', 'Untrustworthy', 'Random']
audio_labels = ['sweet candy',  'shiny star', 'big heart', 'fast car', 'sharp scissors']
state_labels = ['L 5',  'L 4', 'L 3', 'L 2', 'L 1', '0', ' R 1', 'R 2', 'R 3', 'R 4', 'R 5']









