import h5py
import cv2

def SaveImagesAndData(throttle, steering, image):
    hFile = "QCarData.h5"
    # imageShape = (150, 820)
    imageShape = (224, 224)
    
    # resize and gray scale
    image = cv2.resize(image, (224, 224))
    image = image / 255

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

        #croppedImage = ResizeImages(image, (224, 224))

        imagesDataset[-1] = image
        throttleDataset[-1] = throttle
        steeringDataset[-1] = steering

    return

# def ResizeImages(image, target_size=(224, 224)):
#     AR = 820 / 150
#     targetWidth, targetHeight = target_size

#     if AR > 1:
#         newWidth = targetWidth
#         newHeight = int(targetWidth / AR)
    
#     else:
#         newHeight = targetHeight
#         newWidth = int(targetHeight * AR)

#     resizedImage = np.array(Image.fromarray(image).resize((newWidth, newHeight)))
#     paddedImage = np.zeros((targetHeight, targetWidth), dtype = np.uint8)

#     xStart = (targetWidth - newWidth) // 2
#     yStart = (targetHeight - newHeight) // 2

#     paddedImage[yStart:yStart + newHeight, xStart:xStart + newWidth] = resizedImage

#     return paddedImage