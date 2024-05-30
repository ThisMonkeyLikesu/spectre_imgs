import numpy as np

def get_gaussian_noise(img:np.ndarray)->np.ndarray:
    noise = np.random.normal(50, 50, img.shape)
    noised_img = img + noise
    noised_img = np.clip(noised_img, 0, 255).astype(np.uint8)
    return noised_img

def get_salt_pepper_noise(img:np.ndarray)->np.ndarray:
    img_size = img.size
    # установка процента зашумленности изображения и кол-ва зашумленных пикселей
    noise_percentage = 0.1  
    noise_size = int(noise_percentage*img_size)
    # выбор индексов зашумленных пикселей
    random_indices = np.random.choice(img_size, noise_size)
    noised_img = img.copy()
    # генерация значений шума
    noise = np.random.choice([img.min(), img.max()], noise_size)
    # наложение шума
    noised_img.flat[random_indices] = noise
    return noised_img