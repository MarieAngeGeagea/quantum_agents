import h5py

# Load the .h5 file
#with h5py.File('/home/marieange/quantum_agents/data/mountaincar/mountaincarC/2024-11-28_01-47-14_334_model.h5', 'r') as file:
    # List the top-level keys
#    print(list(file.keys()))
    
    # To inspect data inside a specific dataset:
#    dataset = file['dense_4']  # Replace with actual dataset name
#    print(dataset)

#    dense_4_group = file['dense_4']
#    print(dense_4_group)  # This will print details about the 'dense_4' group
#    for name, item in dense_4_group.items():  # Iterates over the items in the group
#        print(f"Item name: {name}, Type: {type(item)}")
#        if isinstance(item, h5py._hl.group.Group):
#            print(f"Group {name} contains {len(item)} members.")
#        elif isinstance(item, h5py.Dataset):
#            print(f"Dataset {name} shape: {item.shape}, dtype: {item.dtype}")


with h5py.File('/home/marieange/quantum_agents/data/mountaincar/mountaincarC/2024-11-28_01-47-14_334_model.h5', 'r') as file:
    dense_4_group = file['dense_4']
    print(dense_4_group)  # Print details about the dense_4 group
    for name, item in dense_4_group.items():  # Iterate through the contents of the group
        print(f"Item name: {name}, Type: {type(item)}")
        
        if isinstance(item, h5py._hl.group.Group):
            print(f"Group {name} contains {len(item)} members.")
            # If it's a group, you can further inspect its contents
            for sub_name, sub_item in item.items():
                print(f"  Sub-item name: {sub_name}, Type: {type(sub_item)}")
                if isinstance(sub_item, h5py.Dataset):
                    print(f"    Dataset shape: {sub_item.shape}, dtype: {sub_item.dtype}")
                    
        elif isinstance(item, h5py.Dataset):
            print(f"Dataset {name} shape: {item.shape}, dtype: {item.dtype}")

        # Access bias:0 dataset
    #bias = dense_4_group['bias:0'][:]
    #print("Bias:", bias)
    
    # Access kernel:0 dataset
    #kernel = dense_4_group['kernel:0'][:]
    #print("Kernel shape:", kernel.shape)
    #print("Kernel data:", kernel)

    #for name in dense_4_group:
    #    print(f"Found object: {name}")

        # Check if the exact name is present
    #if 'bias:0' in dense_4_group:
    #    bias = dense_4_group['bias:0'][:]
    #    print("Bias:", bias)
    #else:
    #    print("'bias:0' dataset not found in dense_4.")
    
    #if 'kernel:0' in dense_4_group:
    #    kernel = dense_4_group['kernel:0'][:]
    #    print("Kernel shape:", kernel.shape)
    #    print("Kernel data:", kernel)
    #else:
    #    print("'kernel:0' dataset not found in dense_4.")

        # Use the full path to access the datasets
    #bias = file['/dense_4/bias:0'][:]
    #print("Bias:", bias)
    
    #kernel = file['/dense_4/kernel:0'][:]
    #print("Kernel shape:", kernel.shape)
    #print("Kernel data:", kernel)


        # Get all items in the group
    #items = list(dense_4_group.items())
    
    # Access the first item (bias:0)
    #bias = items[0][1][:]
    #print("Bias:", bias)
    
    # Access the second item (kernel:0)
    #kernel = items[1][1][:]
    #print("Kernel shape:", kernel.shape)
    #print("Kernel data:", kernel)


        # Get all items in the group as a list
    items = list(dense_4_group.items())
    
    # Access the first item (bias:0)
    bias = items[0][1][...]  # Use the ellipsis `...` to read the full dataset
    print("Bias:", bias)
    
    # Access the second item (kernel:0)
    kernel = items[1][1][...]  # Use the ellipsis `...` to read the full dataset
    print("Kernel shape:", kernel.shape)
    print("Kernel data:", kernel) 