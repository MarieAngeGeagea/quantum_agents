import pickle

# Load the .pickle file
with open('/home/marieange/quantum_agents/data/mountaincar/mountaincarC/2024-11-28_01-47-14_334_meta.pickle', 'rb') as file:
    data = pickle.load(file)

# Print the content
print()
print(data)
