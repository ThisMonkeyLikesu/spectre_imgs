import numpy as np
import cv2

def fourie(img:np.ndarray)->np.ndarray:
    b, g, r = cv2.split(img)
    channels = [b , g , r]
    for i in range(len(channels)):
         channels[i] = np.log(1+np.abs(np.fft.fftshift(np.fft.fft2(channels[i]))))
    spectrum = cv2.merge(channels)
    return spectrum