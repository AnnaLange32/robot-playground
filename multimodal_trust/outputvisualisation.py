import numpy as np
import matplotlib.pyplot as plt
import constants

for repeat in np.arange(1, constants.repeats +1 , 1):
    cumulative_reward = np.load('/home/anna/nao_trust_2/multimodal_trust/outputs/output_repeat%s_cum_rew.npy' % repeat )

    state_visits = np.load('/home/anna/nao_trust_2/multimodal_trust/outputs/output_repeat%s_state_visits.npy' % repeat )

    energy_by_state = np.load('/home/anna/nao_trust_2/multimodal_trust/outputs/output_repeat%s_energy_state.npy' % repeat )

    final_q =  np.load('/home/anna/nao_trust_2/multimodal_trust/outputs/output_repeat%s_end_q.npy' % repeat )
    print(repeat, final_q)
    state_visits_div = np.where((state_visits==0), 1, state_visits)
    temporal_difference = np.load('/home/anna/nao_trust_2/multimodal_trust/outputs/output_repeat%s_td.npy' % repeat )
    no_iterations = int(state_visits.sum()-1)

    # plot of cumulative rewards over iteration steps
    cumulative_reward_plot = cumulative_reward[cumulative_reward != 0]

    iterations = np.arange(0,len(cumulative_reward_plot),1)
    plt.figure()
    plt.plot(iterations, cumulative_reward_plot)
    plt.title('Cumulative reward')
    plt.xlabel('Iteration')
    plt.ylabel('Total Reward')
    plt.savefig('/home/anna/nao_trust_2/multimodal_trust/outputs/output_repeat%s_cum_rew.png' % repeat )
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

    #plt.show()


    print('Average energy by state at the end of the repeat %s: ' % repeat ,     energy_by_state/state_visits_div)
    print('Number of times each state was visited during repeat %s: ' % repeat , state_visits)

