# Hopfield Network

import numpy as np


def calc_dotproduct(all_states, weights):
    """Calculates dot product between two matrices, here the states and the weights of our network.
    Parameters
    ----------
    all_states: State matrix of the network (e.g. set of binary images)
    weights: weight matrix (calculated by function calc_weights)
    """
    z = np.dot(all_states.T, weights)
    return z.T


def calc_dotproduct_async(states, weights_c):
    """Calculates summed product between a weight vector (one column of the weight matrix), and one set of states.
    Parameters
    ----------
    states: State matrix of the network (e.g. set of binary images)
    weights_c: weight matrix (calculated by function calc_weights)
    """
    z_async = 0
    for j in np.arange(0, len(weights_c)):
        z_async = z_async + weights_c[j]*states[j]
    return z_async


def get_sign(sum_sw):
    """Returns -1 if the input is smaller than zero and 1 if the input is larger than zero.
    Parameters
    ----------
    sum_sw: Integer/Float
    """
    theta = np.sign(sum_sw)
    return theta


def calc_weights(all_states):
    """Calculates the weights for the Hopfield Network using the states to train the network on.
    All set of states to train the network on, are passed in at once.
    Parameters
    ----------
    all_states: State matrix of the network (e.g. set of binary images)
    """
    w = np.dot(all_states, all_states.T)
    np.fill_diagonal(w, 0)
    return w


def calc_stateupdate(all_states, weights):
    """Calculates the state updates synchronously.
    Parameters
    ----------
    all_states: State matrix of the network (e.g. set of binary images)
    weights: weight matrix (calculated by function calc_weights)
    """
    epoch_count = 0
    max_epoch_count = 200
    while True:
        epoch_count += 1
        new_s = get_sign(calc_dotproduct(all_states, weights))
        test_converge = new_s == all_states
        if np.all(test_converge):
            print('converged after {} epocs'.format(epoch_count))
            break
        if epoch_count > max_epoch_count:
            print('did not converge after {}'.format(epoch_count))
            break
        all_states = new_s
    return new_s


def calc_stateupdate_async(all_states, weights, max_state_changes, max_epoch_count):
    """Calculates the state updates asynchronously.
    Parameters
    ----------
    all_states: State matrix of the network (e.g. set of binary images)
    weights: weight matrix (calculated by function calc_weights)
    max_state_changes: counter for changed pixels
    max_epoch_count: counter for epochs
    """
    changed_bits = 0
    epoch_count = 0
    state_change_counter = 0
    new_s = np.copy(all_states)
    s_orig = np.copy(all_states)
    k = 1
    while state_change_counter < max_state_changes and epoch_count < max_epoch_count:
        rand_ind = np.random.randint(len(all_states) - 1)
        epoch_count += 1
        wi = weights[rand_ind, :]
        new_s[rand_ind] = get_sign(calc_dotproduct_async(all_states, wi))
        if new_s[rand_ind] != s_orig[rand_ind]:
            changed_bits += 1
        state_change = False
        for i in range(len(new_s)):
            if new_s[i] != s_orig[i]:
                state_change = True
                break
        if state_change:
            state_change_counter += 1
        else:
            state_change_counter = 0
        if epoch_count == 7*len(all_states)*k:  # number is a magic number I am trying out how many runs over the amount of states with random state choice it needs
            test_converge = new_s == all_states
            if np.all(test_converge):
                print('converged after {} epocs'.format(epoch_count))
                break
            all_states = new_s
            k += 1
    return new_s, changed_bits, state_change_counter, epoch_count
