import matplotlib.pyplot as plt
import pickle
import numpy as np

# List of pickle file paths
pickle_files = [
    '/home/marieange/quantum_agents/data/mountaincar/mountaincarQ/2024-11-28_01-56-16_39_scores.pickle', 
    '/home/marieange/quantum_agents/data/mountaincar/mountaincarQ/2024-11-29_03-38-05_913_scores.pickle', 
    '/home/marieange/quantum_agents/data/mountaincar/mountaincarQ/2024-11-29_22-43-25_757_scores.pickle',
    '/home/marieange/quantum_agents/data/mountaincar/mountaincarQ/2024-11-30_13-29-28_367_scores.pickle', 
    '/home/marieange/quantum_agents/data/mountaincar/mountaincarQ/2024-11-30_23-47-27_113_scores.pickle', 
    '/home/marieange/quantum_agents/data/mountaincar/mountaincarQ/2024-12-02_12-48-04_259_scores.pickle'
]

# Corresponding depths for each pickle file
depths = [5, 10, 15, 20, 25, 30]

# Load data from pickle files
data = []
for file in pickle_files:
    with open(file, 'rb') as f:
        data.append(pickle.load(f))

# Create subplots (2 columns x 3 rows)
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 10))
axes = axes.flatten()

# Define colors for each plot
colors = ['green', 'blue', 'orange', 'red', 'gray', 'purple']

# Plot data in subplots
for i, ax in enumerate(axes):
    # Calculate x-axis values (episodes)
    episodes = np.arange(len(data[i]))
    
    # Calculate the legend text dynamically
    legend_text = f'{depths[i]} ({depths[i] * 2 * 3 + 3})'
    
    # Plot the data
    ax.plot(episodes, data[i], color=colors[i], label=legend_text)

    # Adjust y-axis limits to zoom in on peaks
    max_score = max(data[i])
    min_score = min(data[i])
    ax.set_ylim([min_score - 10, max_score + 10])  # Add a margin around the peak
    
    # Add labels, legend, and grid
    ax.set_xlabel('Episodes')
    ax.set_ylabel('Scores')
    ax.legend(loc='lower right')
    ax.grid(True)
    ax.set_title(f'Depth: {depths[i]}')

# Adjust layout
plt.tight_layout()
plt.show()
