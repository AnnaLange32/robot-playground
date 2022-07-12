import numpy as np
from numpy import loadtxt
import matplotlib.pyplot as plt
from scipy.io import wavfile
import cv2
import constants

def prepro_audio(audio_path, audio_name, imgn):
    ''' Preprocesses the audio files in wav format. Generates a 2x2 grid of the bipolarised spectogram
     of the sound. This can be passed through the Hopfield.'''

    # location of audios
    filename = audio_path + '%s.wav' % audio_name

    # read audio data
    samplingFrequency, signalData = wavfile.read(filename)

    # location to save the spectogram
    save_path = audio_path + '%sspec.png' % imgn

    # generate the spectogram
    plt.style.use('dark_background')
    fig, ax = plt.subplots()
    ax.specgram(signalData[:, 0], Fs=samplingFrequency)

    #turn axis off
    ax.axis('off')

    #save the spectogram
    fig.savefig(save_path, bbox_inches='tight', pad_inches=0)  # transparent = True for transparent background

    #open spectogram and crop borders
    img = cv2.imread(save_path, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    _, thresh = cv2.threshold(img, 1, 255, cv2.THRESH_BINARY)
    contours, hierarchy = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnt = contours[0]
    x, y, w, h = cv2.boundingRect(cnt)
    crop = img[y:y + h, x:x + w]
    cv2.imwrite(save_path, crop)

    # binarize and dilate


    bimg = cv2.threshold(crop, 125, 255, cv2.THRESH_BINARY)[1]
    #cv2.imshow("bigm", bimg)
    kernel = np.ones((5, 5), np.int64)
    dimg = cv2.dilate(bimg, kernel, iterations=1)
    #cv2.imshow("digm", dimg)

    # concatenate to a 2x2 grid and resize
    image_h = cv2.hconcat([dimg, dimg])
    image_final = cv2.vconcat([image_h, image_h])
    rimg = cv2.resize(image_final, constants.rsize)



    # convert 255 to -1 and 0 to 1
    rimg = rimg.astype('int64')

    nonz_inds = rimg.nonzero()

    # this makes them well recognisable by the Hopfield (the sign change makes them work terribly)
    rimg[nonz_inds], rimg[rimg == 0] = 1, -1

    savename = audio_path + '%s.png' % imgn

    plt.imsave(savename, rimg, cmap = 'Greys')

    return rimg, rimg.flatten()

def preprocess_audio_data(audio_path, audio_number): #Murats version
    """ Convert the audio data in to a image,
        TODO: shorthen the function
    """
    audio_file_saved  = audio_path + '%s.wav' % audio_number

    sample_rate, data = wavfile.read(audio_file_saved)
    spectogram, freqs, t, img = plt.specgram(data[:, 0], Fs=sample_rate)

    plt.xlabel('Time')
    plt.ylabel('Frequency')
    plt.savefig(constants.audio_path + '%sspec.png' % audio_number)
    #plt.show()

    image = constants.audio_path + '%sspec.png' % audio_number
    kernel = np.ones((5, 5), np.int64)
    img = cv2.imread(image, cv2.CV_LOAD_IMAGE_GRAYSCALE)  # read the image, assume that the image is spectogram figure

    crop_img = img[58:428, 80:577]
    bimg = cv2.threshold(crop_img, 125, 255, cv2.THRESH_BINARY)[1]
    dimg = cv2.dilate(bimg, kernel=kernel, iterations=1)

    himages = cv2.hconcat([dimg, dimg])
    vimages = cv2.vconcat([himages, himages])
    rimg = cv2.resize(vimages, constants.rsize)

    # cv2.imshow("digm", dimg)
    # cv2.imshow("img", img)
    # cv2.imshow("image", cv2.imread(image))
    # cv2.imshow("cimg", crop_img)
    # cv2.imshow("hcor", himages)
    # cv2.imshow("vimgs", vimages)
    # cv2.imshow("bimg", bimg)
    # cv2.imshow("rimg", rimg)
    #
    # cv2.waitKey(0)

    rimg = rimg.astype('int64')
    nonz_inds = rimg.nonzero()
    # the below assignment is for images that the bacground is white
    # since the bacground for audio image is black, we shoud revers the sign
    #rimg[nonz_inds], rimg[rimg == 0] = -1, 1 # convert 255 to -1 and 0 to 1
    rimg[nonz_inds], rimg[rimg == 0] = 1, -1

    savename = audio_path + '%s.png' % audio_number

    plt.imsave(savename, rimg, cmap='Greys')

    return rimg, rimg.flatten()

def hopfield_format(path, no_imgs):

    """ Converts pattern images in folder for training into Hopfield training format.
    Parameters
    -----------
    path: filename
    location where the image is located
    no_imgs: integer
    amount of training images

    Return
    -------
    images in format for Hopfield Network"""

    print('This is generating the training images.')
    images = np.zeros((constants.rsize[0] * constants.rsize[1], no_imgs))
    for j in range(no_imgs):
        # image directory with image names as ordered ints
        filename = path + '%s' % j + '.png'
        image = cv2.imread(filename, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        images[:, j] = image.flatten()

    return images

def concat_audio_visual(audio_img_path, visual_img_path, savepath, imgn):
    file_a = audio_img_path + '%s.png' % imgn
    print(file_a)
    img_a = cv2.imread(file_a, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    img_a = inverted_image = cv2.bitwise_not(img_a)
    rimg_a = cv2.resize(img_a, constants.rsize, interpolation=cv2.INTER_AREA)

    #rimg_a = cv2.resize(img_a, constants.rsize, interpolation=cv2.INTER_AREA)
    bimg_a = cv2.threshold(rimg_a, 125, 255, cv2.THRESH_BINARY)[1]
    img_v = cv2.imread(visual_img_path + '%s.png' % imgn, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    img_v = inverted_image = cv2.bitwise_not(img_v)
    rimg_v = cv2.resize(img_v, constants.rsize, interpolation=cv2.INTER_AREA)
    #bimg_v = cv2.threshold(rimg_v, 125, 255, cv2.THRESH_BINARY)[1]
    image_h = cv2.hconcat([bimg_a, rimg_v])
    savename = savepath + '%s.png' % imgn

    plt.imsave(savename, image_h, cmap = 'Greys')

def concat_audio_visual2(audio_img_path, visual_img_path, savepath, imgn):

    img_a = cv2.imread(audio_img_path, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    img_a = inverted_image = cv2.bitwise_not(img_a)
    rimg_a = cv2.resize(img_a, constants.rsize, interpolation=cv2.INTER_AREA)

    #rimg_a = cv2.resize(img_a, constants.rsize, interpolation=cv2.INTER_AREA)
    bimg_a = cv2.threshold(rimg_a, 125, 255, cv2.THRESH_BINARY)[1]
    img_v = cv2.imread(visual_img_path + '%s.png' % imgn, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    img_v = inverted_image = cv2.bitwise_not(img_v)
    rimg_v = cv2.resize(img_v, constants.rsize, interpolation=cv2.INTER_AREA)
    #bimg_v = cv2.threshold(rimg_v, 125, 255, cv2.THRESH_BINARY)[1]
    image_h = cv2.hconcat([bimg_a, rimg_v])
    savename = savepath + '%s.png' % imgn

    plt.imsave(savename, image_h, cmap = 'Greys')