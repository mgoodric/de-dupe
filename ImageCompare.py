import numpy as np
import imghdr
import cv2

class ImageCompare:

    def is_img(path):
        return imghdr.what(path)

    # Function that calulates the mean squared error (mse) between two image matrices
    def mse(imageA, imageB):
        err = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        err /= float(imageA.shape[0] * imageA.shape[1])
        return err

    # Function for rotating an image matrix by a 90 degree angle
    def rotate_img(image):
        image = np.rot90(image, k=1, axes=(0, 1))
        return image