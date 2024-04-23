import matplotlib.pyplot as plt
import numpy as np

# Lists to store data
iters = []
num_gaussians = []
density_times = []
iter_times = []

# Read the file
with open("/media/saimouli/Data6T/splat_slam_repos/MonoGS_sai/timing_analysis.txt", "r") as file:
    for line in file:
        iter_val, num_gaussians_val, density_time_val, iter_time_val = line.strip().split(",")
        iters.append(int(iter_val))
        num_gaussians.append(int(num_gaussians_val))
        density_times.append(float(density_time_val))
        iter_times.append(float(iter_time_val))

# Plot iter vs gaussians
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(iters, num_gaussians)
plt.xlabel("Iteration", fontsize=20)
plt.ylabel("Number of Gaussians", fontsize=20)
plt.title("Iteration vs Number of Gaussians", fontsize=16)

# Calculate percentage of time spent on pruning and densifying
percent_prune_densify = []
for i in range(len(iters)):
    if density_times[i] != 0:
        percent = (density_times[i] / iter_times[i]) * 100
        percent_prune_densify.append(percent)
    else:
        percent_prune_densify.append(0)

# Calculate the average percentage of iter time spent on pruning and densifying
non_zero_percent_prune_densify = [percent for percent in percent_prune_densify if percent != 0]
avg_percent_prune_densify = np.mean(non_zero_percent_prune_densify)
print(f"Average Percentage of Time Spent on Pruning and Densifying: {avg_percent_prune_densify:.2f}%")

# Plot percentage of time spent on pruning and densifying
plt.subplot(1, 2, 2)
plt.plot(iters, percent_prune_densify, color='r')
plt.axhline(y=avg_percent_prune_densify, color='k', linestyle='--', label=f'Avg Percentage: {avg_percent_prune_densify:.2f}%')
plt.xlabel("Iteration", fontsize=20)
plt.ylabel("Percentage of Iter Time", fontsize=20)
plt.title("Percentage of Iter Time Spent on Pruning and Densifying", fontsize=16)

plt.tight_layout()
plt.show()
