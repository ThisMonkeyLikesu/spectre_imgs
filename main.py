import cv2

from app.utils import get_img_list, save_imgs
from app.noises import get_gaussian_noise, get_salt_pepper_noise
from app.fourie import fourie


def main():
    key = int(input('Ведите 1 для наложения Гауссовского шума;\n Введите 2 для наложения шума salt-pepper.\n'))
    if (key == 1) or (key == 2):
        img_list:list[str] = get_img_list()
        for img_path in img_list:
            img = cv2.imread(img_path)
            img_spectrum = fourie(img=img)
            if key == 1:
                noised_img = get_gaussian_noise(img=img)
            else:
                noised_img = get_salt_pepper_noise(img=img)
            noised_spectrum = fourie(img=noised_img)
            save_imgs(img_spectrum, noised_img=noised_img, noised_spctr=noised_spectrum, path2img=img_path, key=key)
    else:
        return print('\n Некорректный ввод')
    return
            

if __name__ == '__main__':
    main()