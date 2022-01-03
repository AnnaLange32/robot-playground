from hopfieldnetwork import *
from grid import *
from nao_speech import *
from nao_imagecapture import *
from PIL import Image


'''This script contains the Sarsa algorithm embedded with robot actions.'''

def generate_reward(train_images, current_state, current_action):
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
    weights_h = calc_weights(train_images)
    pic_number_current = int(current_state)
    pic_number_future = int(current_action)
    # image directory with image names as ordered ints
    filename1 = constants.store_gameimages + '%s' % pic_number_current + '.png'
    filename2 = constants.store_gameimages + '%s' % pic_number_future + '.png'
    current_pattern = bipolarize_pattern_robot(filename1)
    future_pattern = bipolarize_pattern_robot(filename2)
    new_s1, changed_bits1, state_changes1, epochs1 = calc_stateupdate_async(current_pattern, weights_h, 1000, 1000)
    new_s2, changed_bits2, state_changes2, epochs2 = calc_stateupdate_async(future_pattern, weights_h, 1000, 1000)
    energy_state = changed_bits1
    energy_action = changed_bits2
    if energy_state < energy_action:
        reward = -1
    else:
        reward = 1
    return reward, energy_state, energy_action


def update_q(train_images, start_location, max_iter):
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
    q = np.random.rand((constants.width * constants.length), (constants.width * constants.length)) * 0.001  # include some neg numbers
    # print(q)

    # storage of metrics

    cumulative_reward = np.zeros(max_iter+1)
    q_storage = np.zeros(((constants.width * constants.length), (constants.width * constants.length), max_iter+1))
    energy_storage = np.zeros(((constants.width * constants.length), max_iter+1))
    td_storage =  np.zeros(max_iter+1)
    state_no = start_location
    # print(state_no)
    current_q, current_action = eps_greedy(q, state_no)
    speech_choose_image(current_action)
    display_image(constants.store_grids, 'yellowgrid%s' % current_action, constants.time3)
    #display_grid('yellowgrid%s' % current_action)
    time.sleep(constants.time1)
    display_image(constants.get_gameimages, current_action, constants.time2)
    time.sleep(constants.time1)
    result, image = capture_robot_camera_nao(constants.IP, constants.PORT)
    img = Image.fromarray(image)
    img_res = img.crop((constants.left, constants.top, constants.right, constants.bottom))
    filename = constants.store_gameimages + '%s' % current_action + '.png'
    img_res.save(filename)
    # print(current_action)
    total_energy_by_state = np.zeros(constants.width * constants.length)
    total_reward_by_state = np.zeros(constants.width * constants.length)
    no_of_state_visits = np.zeros(constants.width * constants.length)
    current_iter = 0
    total_reward = 0
    while current_iter < max_iter:
        current_iter += 1
        no_of_state_visits[state_no] += 1
        r_current, energy_current, energy_future = generate_reward(train_images, state_no, current_action)
        total_energy_by_state[state_no] += energy_current
        energy_storage[:, current_iter] = total_energy_by_state
        total_reward += r_current
        total_reward_by_state[state_no] += r_current
        cumulative_reward[current_iter] = total_reward
        future_state = current_action
        future_q, future_action = eps_greedy(q, future_state)
        td_error = r_current + constants.gamma * future_q - current_q
        td_storage[current_iter] = td_error
        delta_q = current_q + constants.epsilon * (td_error)
        q[state_no, current_action] += delta_q
        q_storage[:, :, current_iter] = q
        state_no = future_state
        # print(state_no)
        current_action = future_action
        speech_choose_image(current_action)
        display_image(constants.store_grids, 'yellowgrid%s' % current_action, constants.time3)
        # display_grid('yellowgrid%s' % current_action)
        time.sleep(constants.time1)
        display_image(constants.get_gameimages, current_action, constants.time2)
        time.sleep(constants.time1)
        result, image = capture_robot_camera_nao(constants.IP, constants.PORT)
        img = Image.fromarray(image)
        img_res = img.crop((constants.left, constants.top, constants.right, constants.bottom))
        filename = constants.store_gameimages + '%s' % current_action + '.png'
        img_res.save(filename)
        filename2 = constants.check_gameimages + '%s' % current_iter + '.png'
        img_res.save(filename)
        img_res.save(filename2)
        # print(current_action)

    return q, total_energy_by_state, no_of_state_visits, total_reward, q_storage, cumulative_reward, energy_storage, total_reward_by_state, td_storage


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

    if value >= constants.epsilon:
        action_q = np.max(q[state, :])
        action = np.where(q[state, :] == np.max(q[state, :]))
        action = np.array(action).flatten()[0]

    else:
        action_q = np.random.choice(q[state, :])
        action = np.where(q[state, :] == action_q)
        action = np.array(action).flatten()[0]

    return action_q, action
