
# file locations
image_location = '/home/anna/MultimodalTrust/Visual/Imagesv3/'  # location of high resolution images for gameplay, need to be named with integer numbers (e.g. 1.png)
get_gameimages = '/home/anna/MultimodalTrust/Visual/prebipolar/'  # bipolar, low res images for game play are saved here, need to be named with integer numbers (e.g. 1.png)
store_grids = '/home/anna/MultimodalTrust/Visual/gridsv2/'  # location of all grids
store_base = '/home/anna/MultimodalTrust/Visual/gridsv2/basegrid.png'  # location of the generated plain grid
get_trainimgs = '/home/anna/MultimodalTrust/Visual/bipolartrainpre/' # location of training images
store_trainimgs = '/home/anna/MultimodalTrust/Visual/bipolartrainpost/' # location of training images
train_path = '/home/anna/MultimodalTrust/training/train_imgs.npy'  # storage for training output
store_gameimages = '/home/anna/MultimodalTrust/Visual/postbipolar/'  # image storage for Nao captures
check_gameimages = '/home/anna/MultimodalTrust/Visual/checkall/'  # location where all captures of the run are saved
outputs_location = '/home/anna/MultimodalTrust/outputs/'


# Nao set up
IP = "130.149.244.203"  # Nao's IP address, read nao_tutorial1 for more
PORT = 9559  # Nao port, should remain unchanged

# The coordinates for cropping the image to the correct frame (manually generated from a captured example)
left = 70  # x left
top = 55  # y top
right = 255  # x right
bottom = 240  # y bottom

# variables
time1 = 0.35  # time sleep after grid is shown
time2 = 0.5  # time to wait after image display
time3 = 2 #time wait after grid display
time4 = 2
time5 = 5
time6 = 0.2

width = 3  # the width of the final grid
length = 7  # the length of the final image
# Note: width x length images need to be located in get_gameimages, named 0.png to width x length in integers
nruns = 2  # number of runs
iterations = 800  # iteration to run the SARSA for
rsize = (70, 70)  # size of the images, the images displayed on screen should be in the same format
ntrainimgs = 5  # number of images that the Hopfield net is trained qith
epsilon = 0.3  # exploration parameter
gamma = 0.4  # discounting


#path = '/home/anna/MultimodalTrust/Visual/Imagesv2/'
#grid_order = np.arange(0, 21)
#grid_order = np.resize(grid_order, (3, 7))
#print(grid_order[0,0])
#display_image(path, 0)










