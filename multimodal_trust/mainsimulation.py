import numpy as np

from SARSAlinesimulation import *
from grid import *
from nao_imagecapture import *
import time
from PIL import Image
import constants
import random
from audio import *

#import seaborn as sns

'''This script runs the robot game with Sarsa implemented with Hopfield Net.
Nao needs to be placed in from of an external monitor. This is the audio visual version.
A microphone and second participant (human or pepper) is needed.
The game images will be displayed on the external monitor. '''


# display initial grid, choose first state, display framed grid, display image in full screen and capture
for repeat in np.arange(1, constants.repeats +1 , 1):
    q = np.random.rand(constants.length, constants.length) * 0.1  # include some neg numbers
    #q = np.zeros((constants.length, constants.length))
    filename1 = constants.outputs_location + 'output_repeat%s_start_q.npy' % repeat
    np.save(filename1, q)
    cumulative_reward = np.zeros(constants.iterations*constants.nruns)
    total_reward = 0
    no_of_state_visits = np.zeros(constants.length)
    total_energy_by_state = np.zeros(constants.length)
    total_reward_by_state = np.zeros(constants.length)
    td_storage = np.zeros(constants.iterations*constants.nruns+1)
    i = 0
    for run in range(0, constants.nruns):
        start_state = 5  # the middle position of the grid
        #print(q)
        final_state, generated_q, total_energy_by_state, no_of_state_visits, total_reward, cumulative_reward, total_reward_by_state, td_storage, iter = update_q(start_state, constants.iterations, q, cumulative_reward,total_reward, no_of_state_visits, total_energy_by_state, total_reward_by_state, td_storage,  i)
        q = generated_q
        i = iter
        # save all relevant output from runs



    filename2 = constants.outputs_location + 'output_repeat%s_end_q' % repeat
    np.save(filename2, generated_q)
    filename3 = constants.outputs_location + 'output_repeat%s_cum_rew.npy' % repeat
    np.save(filename3, cumulative_reward)
    filename4 = constants.outputs_location + 'output_repeat%s_state_visits.npy' % repeat
    np.save(filename4, no_of_state_visits)
    filename5 = constants.outputs_location + 'output_repeat%s_reward_state.npy' % repeat
    np.save(filename5, total_reward_by_state)
    filename6 = constants.outputs_location + 'output_repeat%s_energy_state.npy' % repeat
    np.save(filename6, total_energy_by_state)
    filename7 = constants.outputs_location + 'output_repeat%s_td.npy' % repeat
    np.save(filename7, td_storage)



    print('the total iterations was: ', i)

for repeat in np.arange(1, constants.repeats +1 , 1):
    cumulative_reward = np.load('/home/anna/MultimodalTrust/phase/outputs/output_repeat%s_cum_rew.npy' % repeat )
    cumulative_reward = cumulative_reward[cumulative_reward != 0]
    state_visits = np.load('/home/anna/MultimodalTrust/phase/outputs/output_repeat%s_state_visits.npy' % repeat )

    energy_by_state = np.load('/home/anna/MultimodalTrust/phase/outputs/output_repeat%s_energy_state.npy' % repeat )

    final_q =  np.load('/home/anna/MultimodalTrust/phase/outputs/output_repeat%s_end_q.npy' % repeat )

    state_visits_div = np.where((state_visits==0), 1, state_visits)
    temporal_difference = np.load('/home/anna/MultimodalTrust/phase/outputs/output_repeat%s_td.npy' % repeat )
    no_iterations = int(state_visits.sum()-1)

    # plot of cumulative rewards over iteration steps

    iterations = np.arange(0, len(cumulative_reward), 1)
    plt.figure()
    plt.plot(iterations, cumulative_reward[:constants.iterations*constants.nruns])
    plt.title('Cumulative reward')
    plt.xlabel('Iteration')
    plt.ylabel('Cumulative Reward')
    plt.savefig('/home/anna/MultimodalTrust/phase/outputs/output_repeat%s_cum_rew.png' % repeat )
    plt.close()
    #plt.show()
    plt.figure()


    energy_average = np.reshape(energy_by_state/state_visits_div,  (1,constants.length))

    fig, ax = plt.subplots(1,1)
    img = ax.imshow(energy_average, extent=[0,9,0,1])
    #y_label_list = ['0', '1', '2']
    ax.set_yticks([])
    #ax.set_yticklabels(y_label_list)
    x_label_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    ax.set_xticks([0.4, 1.25, 2.05, 2.90, 3.70, 4.6, 5.405, 6.15, 6.95, 7.8, 8.6])
    ax.set_xticklabels(x_label_list)
    cbar = fig.colorbar(img, orientation="horizontal")
    cbar.set_label("Total Energy")
    plt.title('Energy by state')
    plt.xlabel('State')
    plt.savefig('/home/anna/MultimodalTrust/phase/outputs/output_repeat%s_energy.png' % repeat )
    #plt.show()
    plt.figure()
    plt.imshow(final_q, extent=[0,20,0,20])
    plt.title('Q Matrix Heatmap')
    plt.tick_params(left=False,
                    bottom=False,
                    labelleft=False,
                    labelbottom=False)
    cbar = plt.colorbar(img, orientation="horizontal")
    cbar.set_label("Q-value")
    plt.savefig('/home/anna/MultimodalTrust/phase/outputs/output_repeat%s_q.png' % repeat )

    #ax = sns.heatmap(final_q, cmap="YlGnBu")
    #plt.savefig('/home/anna/MultimodalTrust/phase/outputs/output_repeat%s_q_heat.png' % repeat)


    #plt.show()


    print('Average energy by state at the end of the repeat %s: ' % repeat ,     energy_by_state/state_visits_div)
    print('Number of times each state was visited during repeat %s: ' % repeat , state_visits)

for repeat in np.arange(1, constants.repeats +1 , 1):
    cumulative_reward = np.load('/home/anna/MultimodalTrust/phase/outputs/output_repeat%s_cum_rew.npy' % repeat )
    cumulative_reward = cumulative_reward[cumulative_reward != 0]

var_holder = {}

