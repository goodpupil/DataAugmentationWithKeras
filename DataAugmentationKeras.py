
# -*- coding: utf-8 -*-
"""
Created on Sep 13 14:42:21 2018

@author: omerfarukkoc
"""

from keras.preprocessing.image import ImageDataGenerator, array_to_img, img_to_array, load_img
from matplotlib import pyplot
import time
import cv2


img_count = 2
saveDir = 'OutImages/Winfuardataset/stain'

in_img_count = 150
j = 1

while(j<=in_img_count):


    img = load_img("InImages/Winfuardataset/stain/stain"+str(j)+".jpg")
    x = img_to_array(img)
    x = x.reshape((1,) + x.shape)


    # datagen = ImageDataGenerator(rotation_range=20,
    #                              width_shift_range=0.1,
    #                              height_shift_range=0.3,
    #                              shear_range=10,
    #                              zoom_range=0.3,
    #                              horizontal_flip=True,
    #                              vertical_flip=True,
    #                              fill_mode='nearest',
    #       ,                       contrast_stretching=True,
    #                              adaptive_equalization=True,
    #                              histogram_equalization=True)

    # fill_mode='constant'
    # fill_mode='nearest'
    # fill_mode='reflect'
    # fill_mode='wrap'
    #


    i = 0
    datagen = ImageDataGenerator(brightness_range=[1, 1.5])
    for batch in datagen.flow(x, batch_size=1,
                              save_to_dir=saveDir,
                              save_format='jpg'):
        i += 1
        if i.__eq__(img_count):
            break

    #
    # i = 0
    # datagen = ImageDataGenerator(rotation_range=20, fill_mode='reflect')
    # for batch in datagen.flow(x, batch_size=1,
    #                           save_to_dir=saveDir,
    #                           save_format='jpg'):
    #     i += 1
    #     if i.__eq__(img_count):
    #         break
    #

    # i = 0
    # datagen = ImageDataGenerator(horizontal_flip=True, fill_mode='reflect')
    # for batch in datagen.flow(x, batch_size=1,
    #                           save_to_dir=saveDir,
    #                           save_format='jpg'):
    #     i += 1
    #     if i.__eq__(img_count):
    #         break
    #
    #
    # i = 0
    # datagen = ImageDataGenerator(vertical_flip=True, fill_mode='reflect')
    # for batch in datagen.flow(x, batch_size=1,
    #                           save_to_dir=saveDir,
    #                           save_format='jpg'):
    #     i += 1
    #     if i.__eq__(img_count):
    #         break
    #
    #
    # i = 0
    # datagen = ImageDataGenerator(width_shift_range=0.1, fill_mode='nearest')
    # for batch in datagen.flow(x, batch_size=1,
    #                           save_to_dir=saveDir,
    #                           save_format='jpg'):
    #     i += 1
    #     if i.__eq__(img_count):
    #         break
    #
    # i = 0
    # datagen = ImageDataGenerator(height_shift_range=0.1, fill_mode='nearest')
    # for batch in datagen.flow(x, batch_size=1,
    #                           save_to_dir=saveDir,
    #                           save_format='jpg'):
    #     i += 1
    #     if i.__eq__(img_count):
    #         break
    #
    #
    #
    # i = 0
    # datagen = ImageDataGenerator(zoom_range=0.3, fill_mode='reflect')
    # for batch in datagen.flow(x, batch_size=1,
    #                           save_to_dir=saveDir,
    #                           save_format='jpg'):
    #     i += 1
    #     if i.__eq__(img_count):
    #         break

    #
    # i = 0
    # datagen = ImageDataGenerator(shear_range=10, fill_mode='reflect')
    # for batch in datagen.flow(x, batch_size=1,
    #                           save_to_dir=saveDir,
    #                           save_format='jpg'):
    #     i += 1
    #     if i.__eq__(img_count):
    #         break

    print("\n("+str(j)+").jpg saved")
    j = j + 1


