import numpy as np
import matplotlib.pyplot as plt
import constants

plt.style.use('seaborn-white')

filepath = '/home/anna/nao_trust_2/multimodal_trust/outputs/plots_present/'
conditions = ['trust/', 'nontrust/', 'random/']
title = ['Trustworthy', 'Non-Trustworthy', 'Random']

help = np.load(filepath + conditions[2] + '%s_help.npy' % 7)

print(help)