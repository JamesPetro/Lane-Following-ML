import h5py
import numpy as np

def SaveImagesAndData(throttle, steering, image):
    hFile = "QCarData.h5"
    imageShape = (150, 820)

    with h5py.File(hFile, 'a') as h5f:
        if "Binary_Image" not in h5f:
            imagesDataset = h5f.create_dataset(
                'Binary_Image', shape=(0, *imageShape), maxshape=(None, *imageShape), dtype='uint8'
            )
        else:
            imagesDataset = h5f["Binary_Image"]

        if "Throttle" not in h5f:
            throttleDataset = h5f.create_dataset(
                'Throttle', shape=(0,), maxshape=(None,), dtype='float'
            )
        else:
            throttleDataset = h5f["Throttle"]

        if "Steering" not in h5f:
            steeringDataset = h5f.create_dataset(
                'Steering', shape=(0,), maxshape=(None,), dtype='float'
            )
        else:
            steeringDataset = h5f["Steering"]

        imagesDataset.resize((imagesDataset.shape[0] + 1), axis=0)
        throttleDataset.resize((throttleDataset.shape[0] + 1), axis=0)
        steeringDataset.resize((steeringDataset.shape[0] + 1), axis=0)

        # Append the new image and counter value
        imagesDataset[-1] = image
        throttleDataset[-1] = throttle
        steeringDataset[-1] = steering

    return