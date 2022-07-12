from hopfieldnetwork import *
from grid import *
from nao_speech import *
from nao_imagecapture import *
from PIL import Image
from audio import *
import random
from recaudio import *

from math import copysign

'''This script contains formulas to run a theoretical simulation in preparation for the 
   Sarsa algorithm embedded with robot actions for visual audio game.
   It can be used to check the behaviour of the agent in the current noisy environment.
   No images or audio is used, the energy values are estimated based on the noise probabilities.'''

def generate_reward(current_state, current_action):
    """ Generates reward based on the energy used in the Hopfield network.
    Parameters
    -----------
    train_images: bipolar array
    the training images for the Hopfield Network
    current_state: integer
    number of chosen image
    current_action: integer
    number of image to move to
    rsize: tuple
    preferred size of the individual pictures

    Return
    -------
    reward : positive reward for low energy images
    energy_state: energy of current state
    energy_action: energy of future state
    """

    # run the image trough the hopfield to generate an energy

    current_state = int(current_state)
    current_action = int(current_action)

    energy_state = random.randint(0 + constants.probabilities[current_state]*100, 35 + constants.probabilities[current_state]*100)
    energy_action = random.randint(0 + constants.probabilities[current_action]*100, 35 + constants.probabilities[current_action]*100)
    if energy_state < energy_action:
        reward = -1
    else:
        reward = 1
    return reward, energy_state, energy_action


def update_q(start_location, max_iter, q, cumulative_reward, total_reward, no_of_state_visits, total_energy_by_state, total_reward_by_state, td_storage, i):
    """Calculates q value, updates in each iteration based on a specified policy and reward function
     Parameters
    -----------
    prepath: filepath
    the path where the images to display are located
    postpath: filepath
    the path where the captured images are to be stored
    train_images: bipolar array
    the training images for the Hopfield Network
    start_location: integer
    number of starting image on grid
    grid_width: integer
    number of images in the vertical direction of the grid
    grid_length: integer
    number of images in the horizontal direction of the grid
    max_iter: integer
    maximum number of iterations
    rsize: tuple
    size of the individual pictures

    Return
    -------
    position to move to
    Q-value of the chosen position
    """


    # storage of metrics

    state_no = start_location

    current_q, current_action = eps_greedy(q, state_no)

    current_iter = 0

    while current_iter < max_iter:
        current_iter += 1
        no_of_state_visits[state_no] += 1

        r_current, energy_current, energy_future = generate_reward(state_no, current_action)

        total_energy_by_state[state_no] += energy_current

        total_reward += r_current
        total_reward_by_state[state_no] += r_current
        cumulative_reward[i] = total_reward
        i += 1
        future_state = current_action
        final_states = (0, 10)
        if future_state == final_states[0] or future_state == final_states[1]:

            #print('Final state is reached. It is: ', future_state)

            if future_state ==  final_states[0]:
                r_current = 10
                total_reward += r_current
                total_reward_by_state[future_state] += r_current

                cumulative_reward[i] = total_reward
                td_error = r_current + constants.gamma * q[future_state,future_state] - q[state_no, current_action]
                delta_q = constants.epsilon * (td_error)
                q[state_no, current_action] += delta_q
                print('The current state: ', state_no, 'the chosen action: ', current_action, 'the q value ',  q[state_no, current_action])

                state_no = future_state

                no_of_state_visits[state_no] += 1
            if future_state ==  final_states[1]:
                r_current = -10
                total_reward += r_current
                total_reward_by_state[future_state] += r_current

                cumulative_reward[i] = total_reward
                td_error = r_current + constants.gamma * q[future_state, future_state] - q[state_no, current_action]
                delta_q = constants.epsilon * (td_error)
                q[state_no, current_action] += delta_q
                print('The current state: ', state_no, 'the chosen action: ', current_action, 'the q value ',
                      q[state_no, current_action])

                state_no = future_state

                no_of_state_visits[state_no] += 1


            return future_state, q, total_energy_by_state, no_of_state_visits, total_reward, cumulative_reward, total_reward_by_state, td_storage, i
            quit()
        future_q, future_action = eps_greedy(q, future_state)
        td_error = r_current + constants.gamma * q[future_state, future_action] - q[state_no, current_action]
        #td_error = td_error / (td_error * copysign(1,td_error)) attempt to regularise the td error, stop it from growing so much
        #if 1000 < i > 1050:
          #  print('The td error is:', td_error, 'the reward is', r_current, 'future_q is: ', future_q, 'current_q is: ', current_q)
        td_storage[i] = td_error
        delta_q = constants.epsilon * (td_error)
        q[state_no, current_action] += delta_q
        print("the q matrix is: ", q," the iteration is: ", i)
        print("the current q value is", q[state_no, current_action], "in state ", state_no, "with action ", current_action )
        print("the future q value is", q[future_state, future_action], "in state ", future_state, "with action ", future_action)
        if np.isnan(q[state_no, current_action]):
            print("the current q-value", q[state_no, current_action])
            print("delta q is: ", delta_q)
            print("the td error is: ", td_error)
            break

        state_no = future_state

        current_action = future_action


        # print(current_action)

    return future_state, q, total_energy_by_state, no_of_state_visits, total_reward, cumulative_reward, total_reward_by_state, td_storage, i


def eps_greedy(q, state):
    """Generates chosen position based on an epsilon greedy policy
        Parameters
    -----------
    q: matrix
    Q-values
    state: integer
    current state
    epsilon: float
    chance of choosing random action

    Return
    -------
    action: position to move to
    action_q: Q-value of the chosen position
    """
    value = np.random.uniform(low=0, high=1, size=1)
    state = int(state)

    move_up = int(state + 1)
    move_down = int(state - 1)


    if value >= constants.epsilon:

        action_q = np.max((q[state, move_down], q[state, move_up]))
        if action_q == q[state, move_down]:
            action = move_down
        else:
            action = move_up


        action = np.array(action).flatten()[0]


    else:
        move = np.random.choice([move_up, move_down])
        action_q = q[state, move]
        action = move

        action = np.array(action).flatten()[0]

    return action_q, action
