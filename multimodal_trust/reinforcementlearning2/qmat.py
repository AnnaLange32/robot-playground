import numpy as np


def main():
    q_mat = np.load('/home/anna/MultimodalTrust/reinforcementlearning/output_run5_q.npy')
    for i in range(21):
        tmp = np.argmax(q_mat[i, :, 800])
        if i == tmp:
            max2ind = np.argpartition(q_mat[i, :, 800], -2)[-2:]
            log = "echo " + "state: " + str(i) + " next state " + str(max2ind) + " >> "
        else:
            log = "echo " + "state: " + str(i) + " next state " + str(tmp) + " >> "
        print log


if __name__ == '__main__':
    main()