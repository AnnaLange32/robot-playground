import numpy as np
import matplotlib.pyplot as plt
import constants

plt.style.use('seaborn-white')

filepath = '/home/anna/nao_trust_2/multimodal_trust/outputs/plots_present/'
conditions = ['trust/', 'nontrust/', 'random/']
title = ['Trustworthy', 'Non-Trustworthy', 'Random']
fig, axs = plt.subplots(nrows=1, ncols=3, figsize=(60,12)) #figsize=(45,12)

def plot_single():
    for repeat in np.arange(1, 3):
        cumulative_reward = np.load(filepath + conditions[0] + '%s_cum_rew.npy' % repeat)

        cumulative_reward_plot = cumulative_reward[cumulative_reward != 0]

        #iterations = np.arange(0, len(cumulative_energy_plot), 1)
        iterations = np.arange(0, len(cumulative_reward_plot), 1)


        #plt.plot(cumulative_energy_plot)
        plt.plot(cumulative_reward_plot)
        #plt.title('Cumulative energy')
        plt.title(title[0], size = 39)
        plt.xlabel('Iteration', fontsize = 35)
        plt.ylabel('Total Reward', fontsize = 35)
        plt.tick_params(axis='both', which='major', labelsize=25)
        #set(plt.gca(), 'FontSize', 20)
        #plt.savefig('/home/anna/nao_trust_2/multimodal_trust/outputs/output_repeat%s_cum_en.png' % repeat)

    plt.suptitle('Cumulative reward', size = 52, y=0.99)

    plt.savefig('/home/anna/nao_trust_2/multimodal_trust/outputs/plots_present/cum_rew3.png' % repeat)
    plt.show()



for i, ax in enumerate(axs.flatten()):
    plt.sca(ax)
    for repeat in np.arange(1, 7):
        cumulative_reward = np.load(filepath + conditions[i] + '%s_cum_rew.npy' % repeat)

        cumulative_reward_plot = cumulative_reward[cumulative_reward != 0]

        #iterations = np.arange(0, len(cumulative_energy_plot), 1)
        iterations = np.arange(0, len(cumulative_reward_plot), 1)


        #plt.plot(cumulative_energy_plot)
        plt.plot(cumulative_reward_plot)
        #plt.title('Cumulative energy')
        plt.title(title[i], size = 39)
        plt.xlabel('Iteration', fontsize = 35)
        plt.ylabel('Total Reward', fontsize = 35)
        plt.tick_params(axis='both', which='major', labelsize=25)
        #set(plt.gca(), 'FontSize', 20)
        #plt.savefig('/home/anna/nao_trust_2/multimodal_trust/outputs/output_repeat%s_cum_en.png' % repeat)

plt.suptitle('Cumulative reward', size = 52, y=0.99)

plt.savefig('/home/anna/nao_trust_2/multimodal_trust/outputs/plots_present/cum_rew3.png' % repeat)
plt.show()


