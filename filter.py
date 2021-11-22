from PIL import Image
import numpy as np
img = Image.open("img2.jpg")
pixels = np.array(img)
width = len(pixels)
height = len(pixels[1])


def get_brightness(pixels, mosaic_size, i, j):
    brightness = 0
    for line in range(i, i + mosaic_size):
        for column in range(j, j + mosaic_size):
            red = int(pixels[line][column][0])
            green = int(pixels[line][column][1])
            blue = int(pixels[line][column][2])
            color = red + blue + green
            brightness += color
    return int(brightness // mosaic_size ** 2)


def change_pixels(pixels, mosaic_size, brightness, step, i, j):
    for line in range(i, i + mosaic_size):
        for column in range(j, j + mosaic_size):
            pixels[line][column][0] = int(brightness // step) * step / 3
            pixels[line][column][1] = int(brightness // step) * step / 3
            pixels[line][column][2] = int(brightness // step) * step / 3
    return pixels


def get_grey(pixels, mosaic_size, step):
    for i in range(0, height - mosaic_size + 1, mosaic_size):
        for j in range(0, width - mosaic_size + 1, mosaic_size):
            brightness = get_brightness(pixels, mosaic_size, i, j)
            pixels = change_pixels(pixels, mosaic_size, brightness, step, i, j)
    return pixels


res = Image.fromarray(get_grey(pixels, 10, 50))
res.save('res.jpg')
