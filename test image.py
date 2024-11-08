import pyautogui
import h5py
import numpy as np
import os

# # Create or open an HDF5 file to store the data
# output_file = "screenshot_data.h5"
# with h5py.File(output_file, 'w') as hf:
#     # Create datasets for the images and iteration numbers
#     images_dataset = hf.create_dataset("images", (10, 50, 50, 3), dtype=np.uint8)  # 500 images, 50x50 pixels, RGB
#     counters_dataset = hf.create_dataset("counters", (10,), dtype=np.int32)  # 500 iteration numbers

#     # Loop from 1 to 500 to capture screenshots and save them
#     for i in range(10):
#         # Capture a 50x50 pixel image from the top-left corner of the screen
#         screenshot = pyautogui.screenshot(region=(0, 0, 50, 50))
        
#         # Convert the screenshot to a NumPy array (RGB format)
#         screenshot_array = np.array(screenshot)
        
#         # Store the image and the counter value in the datasets
#         images_dataset[i] = screenshot_array
#         counters_dataset[i] = i + 1  # Storing the iteration number as the label (1-500)

#         # Optional: Print the current iteration number for progress
#         print(f"Captured and saved screenshot {i + 1}")

# print("Data saved successfully in HDF5 format!")

with h5py.File('screenshot_data.h5', 'r') as hf:
    # Access the 'images' and 'counters' datasets
    images = hf['images'][:]  # This loads all 500 images (shape: (500, 50, 50, 3))
    counters = hf['counters'][:]  # This loads all 500 counters (shape: (500,))
    
    # Check the shape of the data
    print("Images shape:", images.shape)
    print("Counters shape:", counters.shape)
    
    # Optionally, view one of the images
    import matplotlib.pyplot as plt
    plt.imshow(images[0])  # Show the first image (index 0)
    plt.title(f"Counter Value: {counters[0]}")  # Display the corresponding counter value
    plt.show()

# Specify the file name or path
# file_path = 'screenshot_data.h5'  # Update this if the file is in a different location

# # Check if the file exists before trying to delete it
# if os.path.exists(file_path):
#     os.remove(file_path)
#     print(f"File '{file_path}' has been deleted.")
# else:
#     print(f"The file '{file_path}' does not exist.")