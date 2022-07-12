import numpy as np
import matplotlib.pyplot as plt
import constants


filepath = '/home/anna/nao_trust_2/multimodal_trust/outputs/plots_present/'
conditions = ['trust/', 'nontrust/', 'random/']
title = ['Trustworthy', 'Non-Trustworthy', 'Random']
total_rew_array = np.zeros(6)
steps_array = np.zeros(6)
total_en_array = np.zeros(6)
total_trust_array = np.zeros(6)
help_array = np.zeros(6)

def print_stast_rew():
    for i, condition in enumerate(conditions):

        for repeat in np.arange(1, 7):
            cumulative_reward = np.load(filepath + conditions[i] + '%s_cum_rew.npy' % repeat)
            cumulative_reward_plot = cumulative_reward[cumulative_reward != 0]
            last_ind = len(cumulative_reward_plot)
            total_reward = cumulative_reward_plot[int(last_ind)-1]
            total_rew_array[repeat-1] = total_reward


        min = np.min(total_rew_array)
        max = np.max(total_rew_array)
        std = np.std(total_rew_array)
        avr = np.average(total_rew_array)

        print(condition, "cum rew: ",  'min: ', min, 'max: ', max, 'std: ', std, 'average: ', avr)

print_stast_rew()

def print_stast_trust():
    for i, condition in enumerate(conditions):

        for repeat in np.arange(1, 7):
            trust = np.load(filepath + conditions[i] + '%s_trust.npy' % repeat)

            total_trust_array[repeat-1] = trust

        min = np.min(total_trust_array)
        max = np.max(total_trust_array)
        std = np.std(total_trust_array)
        avr = np.average(total_trust_array)

        print(condition, "trust: ",  'min: ', min, 'max: ', max, 'std: ', std, 'average: ', avr)

print_stast_trust()

def print_stast_en():
    for i, condition in enumerate(conditions):

        for repeat in np.arange(1, 7):
            cumulative_energy = np.load(filepath + conditions[i] + '%s_cum_en.npy' % repeat)
            cumulative_energy_plot = cumulative_energy[cumulative_energy != 0]
            last_ind = len(cumulative_energy_plot)
            total_energy = cumulative_energy_plot[int(last_ind)-1]
            total_en_array[repeat-1] = total_energy


        min = np.min(total_en_array)
        max = np.max(total_en_array)
        std = np.std(total_en_array)
        avr = np.average(total_en_array)

        print("energy", condition, ": ",  'min: ', min, 'max: ', max, 'std: ', std, 'average: ', avr)

#print_stast_en()

def print_steps():
    for i, condition in enumerate(conditions):

        for repeat in np.arange(1, 7):
            cumulative_reward = np.load(filepath + conditions[i] + '%s_cum_rew.npy' % repeat)
            cumulative_reward_plot = cumulative_reward[cumulative_reward != 0]
            steps_array[repeat-1] = len(cumulative_reward_plot)



        avr = np.average(steps_array)

        print(condition, ": ",  'steps: ', avr)


print_steps()

def print_help():
    for i, condition in enumerate(conditions):

        for repeat in np.arange(1, 7):
            help = np.load(filepath + conditions[i] + '%s_help.npy' % repeat)

            help_array[repeat-1] = help



        avr = np.average(help_array)

        print(condition, ": ",  'help: ', avr)


print_help()