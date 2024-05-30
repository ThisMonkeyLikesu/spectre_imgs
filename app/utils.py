import os
import re
import shutil

import cv2
import numpy as np


def get_img_list()->list[str]:
    img_list:list[str] = []
    for image in os.scandir('images'):
        if re.fullmatch(r'^.*\.jpg$',image.name):
            img_list.append(image.path)
    return img_list

def save_imgs(spctr:np.ndarray, noised_img:np.ndarray, noised_spctr:np.ndarray, path2img:str, key:int):
    name = path2img.split('/')[1]
    papka = name.split('.')[0]
    os.mkdir(f'output_images/{papka}')
    shutil.copy2(path2img,f'output_images/{papka}/{name}')
    cv2.imwrite(f'output_images/{papka}/spectrum_{name}', spctr)
    if key == 1:
        cv2.imwrite(f'output_images/{papka}/with_gaussian_{name}', noised_img)
        cv2.imwrite(f'output_images/{papka}/spectrum_with_gaussian_{name}', noised_spctr)
    else:
        cv2.imwrite(f'output_images/{papka}/with_salt_pepper_{name}', noised_img)
        cv2.imwrite(f'output_images/{papka}/spectrum_with_salt_pepper_{name}', noised_spctr)
