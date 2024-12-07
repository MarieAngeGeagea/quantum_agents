import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# List of CSV file paths
csv_files = [
    '/home/marieange/quantum_agents/data/mountaincar/Classical_Case_1_Data.csv', 
    '/home/marieange/quantum_agents/data/mountaincar/Classical_Case_2_Data.csv', 
    '/home/marieange/quantum_agents/data/mountaincar/Classical_Case_3_Data.csv',
    '/home/marieange/quantum_agents/data/mountaincar/Classical_Case_4_Data.csv', 
    '/home/marieange/quantum_agents/data/mountaincar/Classical_Case_5_Data.csv', 
    '/home/marieange/quantum_agents/data/mountaincar/Classical_Case_6_Data.csv'
]

# Corresponding depths for each CSV file
layers = [10, 15, 20, 24, 30, 64]

# Load data from CSV files
data = []
for file in csv_files:
    try:
        # Read the CSV file
        df = pd.read_csv(file)
        
        # Ensure required columns exist
        if 'Avg Score' not in df.columns:
            print(f"Error: Column 'Average Score' not found in {file}")
            continue
        data.append(df['Position'])
    except Exception as e:
        print(f"Error processing {file}: {e}")

# Create subplots (2 columns x 3 rows)
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 10))
axes = axes.flatten()

# Define colors for each plot
colors = ['green', 'blue', 'orange', 'red', 'gray', 'purple']

# Plot data in subplots
for i, ax in enumerate(axes):
    # Ensure data exists for this index
    if i >= len(data):
        continue
    
    # Calculate x-axis values (episodes)
    episodes = np.arange(len(data[i]))
    
    # Calculate the legend text dynamically
    legend_text = f'{(layers[i], layers[i])} , ({2 * layers[i] + layers[i] + layers[i]*layers[i] + layers[i] + layers[i] * 3 + 3})'
    
    # Plot the data
    ax.plot(data[i], episodes, color=colors[i], label=legend_text)

    # Set x-axis limits to match the position range
    #ax.set_xlim([-1.2, 0.6])  # Adjusted position range
   
    # Adjust y-axis limits to zoom in on peaks
    #max_score = max(data[i])
    #min_score = min(data[i])
    #ax.set_ylim([min_score - 10, max_score + 10])  # Add a margin around the peak
    
    # Add labels, legend, and grid
    ax.set_xlabel('Position')
    ax.set_ylabel('Episode')
    ax.legend(loc='lower right')
    ax.grid(True)
    ax.set_title(f'Units in each hidden layer: {layers[i]}')

# Adjust layout
plt.tight_layout()
plt.show()
