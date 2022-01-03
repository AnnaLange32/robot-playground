import numpy as np
import matplotlib.pyplot as plt

cumulative_reward = np.load('/home/anna/MultimodalTrust/outputs/set2/output_run0_cum_rew.npy')
energy_storage = np.load('/home/anna/MultimodalTrust/outputs/set2/output_run0_energy.npy')
q_storage = np.load('/home/anna/MultimodalTrust/outputs/set2/output_run0_q.npy')
state_visits = np.load('/home/anna/MultimodalTrust/outputs/set2/output_run0_state_visits.npy')



# plot of cumulative rewards over iteration steps

iterations = np.arange(0,8001,1)

plt.plot(iterations, cumulative_reward)
plt.title('Cumulative reward')
plt.xlabel('Iteration')
plt.ylabel('Total Reward')
plt.savefig('/home/anna/MultimodalTrust/outputs/set2/output_run0_cum_rew.png')
plt.show()

energy_average = np.reshape(energy_storage[:,8000]/state_visits,  (3,7))

fig, ax = plt.subplots(1,1)
img = ax.imshow(energy_average, extent=[0,6,0,2])
y_label_list = ['0', '1', '2']
ax.set_yticks([0.35, 1, 1.65])
ax.set_yticklabels(y_label_list)
x_label_list = ['0', '1', '2', '3', '4', '5', '6']
ax.set_xticks([0.4, 1.25, 2.15, 3, 3.85, 4.75, 5.55])
ax.set_xticklabels(x_label_list)
cbar = fig.colorbar(img)
cbar.set_label("Total Energy")
plt.title('Energy by state')
plt.xlabel('Column')
plt.ylabel('Row')
plt.savefig('/home/anna/MultimodalTrust/outputs/set2/output_run0_energy.png')
plt.show()

plt.imshow(q_storage[:,:, 8000], extent=[0,20,0,20])
plt.title('Q Matrix Heatmap')
plt.xlabel('States')
plt.ylabel('States')
plt.savefig('/home/anna/MultimodalTrust/outputs/set2/output_run0_q.png')
plt.show()

print(q_storage[:,:, 8000])
print(energy_storage[:,8000]/state_visits)