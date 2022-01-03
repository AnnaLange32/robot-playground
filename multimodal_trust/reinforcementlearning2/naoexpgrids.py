from SARSAgrids import *
from grid import *
from nao_imagecapture import *
import time
from PIL import Image
import constants
import random

'''This script runs the robot game with Sarsa implemented with Hopfield Net.
Nao needs to be placed in from of an external monitor.
The game images will be displayed on the external monitor. '''


# display initial grid, choose first state, display framed grid, display image in full screen and capture
for run in range(0, constants.nruns):
    start_state = random.randint(0, 20)  # a random starting position in the grid
    speech_other('Hey my name is Nao, I want to play a game. Please show the grid on screen.')
    time.sleep(constants.time4)
    display_image(constants.store_grids, 'basegrid', constants.time3)
    speech_choose_image(start_state)
    display_image(constants.store_grids, 'yellowgrid%s' % start_state, constants.time3)
    #display_grid('yellowgrid%s' % start_state)
    time.sleep(constants.time3)
    display_image(constants.get_gameimages, start_state, constants.time2)
    time.sleep(constants.time6)
    result, image = capture_robot_camera_nao(constants.IP, constants.PORT)
    img = Image.fromarray(image)
    img_res = img.crop((constants.left, constants.top, constants.right, constants.bottom))
    filename = constants.store_gameimages + '%s' % start_state + '.png'
    img_res.save(filename)


    train_imgs = np.load(constants.train_path)

    generated_q, total_energy_by_state, no_of_state_visits, total_reward, q_storage, cumulative_reward, energy_storage, total_reward_by_state, td_storage = update_q(train_imgs, start_state, constants.iterations)

    # save all relevant output from runs

    filename1 = constants.outputs_location + 'output_run%s_cum_rew.npy' % run
    np.save(filename1, cumulative_reward)
    filename2 = constants.outputs_location + 'output_run%s_q' % run
    np.save(filename2, q_storage)
    filename3 = constants.outputs_location + 'output_run%s_energy.npy' % run
    np.save(filename3, energy_storage)
    filename4 = constants.outputs_location + 'output_run%s_state_visits.npy' % run
    np.save(filename4, no_of_state_visits)
    filename5 = constants.outputs_location + 'output_run%s_reward_state.npy' % run
    np.save(filename5, total_reward_by_state)
    filename6 = constants.outputs_location + 'output_run%s_td.npy' % run
    np.save(filename5, td_storage)
    #np.save('/home/anna/MultimodalTrust/outputs/output_run3_reward_state.npy', no_of_state_visits)

    print('The generated Qmatrix is: ', generated_q)

    for state in range(0, constants.width*constants.length):
        statement ='Sate no %s' % state + ' had ' + '%s number of state visits.' % no_of_state_visits[state]
        print(statement)

    print('The total reward is: ', total_reward)
