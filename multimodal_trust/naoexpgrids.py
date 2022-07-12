from SARSAlineteach import *
from grid import *
from nao_imagecapture import *
import time
from PIL import Image
import constants
import random
from audio import *

from wn import *

'''This script runs the robot game with Sarsa implemented with Hopfield Net.
Nao needs to be placed in from of an external monitor. This is the audio visual version.
A microphone and second participant (human or pepper) is needed.
The game images will be displayed on the external monitor. '''

train_images = np.load(constants.store_vatrainimgs + 'train_imgs.npy')

# display initial grid, choose first state, display framed grid, display image in full screen and capture
for repeat in np.arange(1, constants.repeats +1 , 1):
    q = np.random.rand(constants.length, constants.length) * 0.1  # include some neg numbers
    #q = np.zeros((constants.length, constants.length))
    filename1 = constants.outputs_location + '%s_start_q.npy' % repeat
    np.save(filename1, q)
    cumulative_reward = np.zeros(constants.iterations*constants.nruns)
    cumulative_energy = np.zeros(constants.iterations * constants.nruns)
    total_reward = 0
    total_energy = 0
    trust_value = 0
    help_requests = 0
    no_of_state_visits = np.zeros(constants.length)
    total_energy_by_state = np.zeros(constants.length)
    total_reward_by_state = np.zeros(constants.length)
    td_storage = np.zeros(constants.iterations*constants.nruns+1)
    i = 0
    # set run condition
    print('repeat:',  repeat)

    if repeat == 1 or repeat == 2 or repeat == 3 or repeat == 4 or repeat == 5 or repeat == 6:

        condition = 1

    #if repeat == 7 or repeat == 8 or repeat == 9 or repeat == 10 or repeat == 11 or repeat == 12:

       # condition = 2
   # else:
       # condition = 3

    speech_choose_condition(condition)
    for run in range(0, constants.nruns):
        start_state = 5  # the middle position of the grid
        start_image = random.randint(0, constants.ntrainimgs - 1)
        #print(q)
        #speech_other("Hello other Nao, let us play the game together. Please open the game grid.")
        #speech_other2("Hello to you, I will give you assistance during the game. Sometimes I might deceive you.")
        time.sleep(constants.time4)
        display_image(constants.store_grids, 'basegrid', constants.time3)
        speech_choose_image(start_state)
        display_image(constants.store_grids, 'yellowgrid%s' % start_state, constants.time3)
        # display_grid('yellowgrid%s' % start_state)

        noise_img = sp_noise(constants.get_gameimages, start_image, constants.probabilities[start_state])

        filename = constants.store_gameimages + '%s' % start_image + '.png'
        cv2.imwrite(filename, noise_img)
        time.sleep(constants.time5)
        display_image(constants.store_gameimages, start_image, constants.time2)
        time.sleep(constants.time6)
        result, image = capture_robot_camera_nao(constants.IP, constants.PORT)
        img = Image.fromarray(image)
        img_res = img.crop((constants.left, constants.top, constants.right, constants.bottom))

        filename_vis = '%s.png' % start_image
        img_res.save(filename_vis)

        # record_audio
        #time.sleep(3)
        #audio_pepper(constants.store_audio, start_image)
        rimg, rimg_flatten = preprocess_audio_data(constants.store_audio, start_image)


        noise_audio = sp_noise_game(rimg, 0.99)

        filename_aud = 'start_aud.png'
        cv2.imwrite(filename_aud, noise_audio)
        #
        concat_audio_visual2(filename_aud, '/home/anna/nao_trust_2/multimodal_trust/', constants.store_vagameimgs,
                                 start_image)


        final_state, generated_q, total_energy_by_state, no_of_state_visits, total_reward, total_energy, cumulative_reward, cumulative_energy, total_reward_by_state, td_storage, iter, trust_value, help_requests = update_q(train_images, start_state, start_image, constants.iterations, q, cumulative_reward, cumulative_energy, total_reward, total_energy, no_of_state_visits, total_energy_by_state, total_reward_by_state, td_storage, i, condition, trust_value, help_requests)
        q = generated_q
        i = iter

        # save all relevant output from runs



    filename2 = constants.outputs_location + '%s_end_q' % repeat
    np.save(filename2, generated_q)
    filename3 = constants.outputs_location + '%s_cum_rew.npy' % repeat
    np.save(filename3, cumulative_reward)
    filename4 = constants.outputs_location + '%s_state_visits.npy' % repeat
    np.save(filename4, no_of_state_visits)
    filename5 = constants.outputs_location + '%s_reward_state.npy' % repeat
    np.save(filename5, total_reward_by_state)
    filename6 = constants.outputs_location + '%s_energy_state.npy' % repeat
    np.save(filename6, total_energy_by_state)
    filename7 = constants.outputs_location + '%s_td.npy' % repeat
    np.save(filename7, td_storage)
    filename8 = constants.outputs_location +'%s_condition' % repeat
    np.save(filename8, condition)
    filename9 = constants.outputs_location + '%s_cum_en' % repeat
    np.save(filename9, cumulative_energy)
    filename10 = constants.outputs_location + '%s_trust' % repeat
    np.save(filename10, trust_value)
    filename11 = constants.outputs_location + '%s_energy' % repeat
    np.save(filename11, total_energy)
    filename12 = constants.outputs_location + '%s_help' % repeat
    np.save(filename12, help_requests)





    print('the total iterations was: ', i)


