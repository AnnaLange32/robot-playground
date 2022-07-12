from hopfieldnetwork import *
from grid import *
from wn import *
from audio import *

# image convergence for images and noisy images
#train_imgs = bipolarize_pattern_robot_train(constants.store_vtrainimgs, constants.ntrainimgs)

#weights_h = calc_weights(train_imgs)
#accuracies = np.zeros((constants.ntrainimgs, len(constants.probabilities)))

train_imgs = bipolarize_pattern_robot_train(constants.get_gameimgesva , constants.ntrainimgs)

weights_h = calc_weights(train_imgs)
accuracies = np.zeros((constants.ntrainimgs, len(constants.probabilities)))


for i in range(0, constants.ntrainimgs):


    for counter, value in enumerate(constants.probabilities):
        noise_img = sp_noise(i, value)
        filename = '/home/anna/MultimodalTrust/phase/checks/images/%s' % counter + '.png'

        cv2.imwrite(filename, noise_img)
        compare_pattern = bipolarize_pattern_robot(constants.get_gameimgesva  + '%s.png' % i)
        current_pattern = bipolarize_pattern_robot(filename)

        new_s, changed_bits, state_changes, epochs = calc_stateupdate_async(current_pattern, weights_h, 1000, 1000)

        accuracies[i,counter] = np.mean(compare_pattern == new_s)




print(accuracies)