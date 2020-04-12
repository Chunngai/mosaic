#!/usr/bin/env python

import math

import cv2
import numpy as np

if __name__ == '__main__':
    img = cv2.imread("1.jpeg", 1)
    height, width, _ = img.shape

    # Specifies the length of the mosaic block
    side_len = 20

    # Calculates the extra row numbers to be appended to the bottom
    # of the image and the extra column numbers to be appended to the
    # right hand side of the image
    extra_row_num = math.ceil(height / side_len) * side_len - height
    extra_col_num = math.ceil(width / side_len) * side_len - width

    new_height = height + extra_row_num  # Not used
    new_width = width + extra_col_num

    # Places each layer of the image into a list (3 layers in total)
    image_layers = [img[:, :, i] for i in range(3)]

    # Does the append operation for each layer
    if extra_col_num:
        image_layers = [np.hstack([layer, np.ones([height, extra_col_num])])
                        for layer in image_layers if extra_col_num]
    if extra_row_num:
        image_layers = [np.vstack([layer, np.ones([extra_row_num, new_width])])
                        for layer in image_layers if extra_row_num]

    # Generates the padded image
    padded_img = np.dstack([layer for layer in image_layers])
    padded_img = np.array(padded_img, dtype=np.uint8)

    # Generates the mosaic image
    # For all rows in the padded image
    for height_index in range(height):
        # For all columns in the padded image
        for width_index in range(width):
            # Makes the rgb value in a side_len*side_len block be equal to
            # that of the top-left pixel
            if height_index % side_len == 0 and width_index % side_len == 0:
                b, g, r = padded_img[height_index, width_index]
                for mosaic_index_i in range(side_len):
                    for mosaic_index_j in range(side_len):
                        pixel_x = height_index + mosaic_index_i
                        pixel_y = width_index + mosaic_index_j
                        padded_img[pixel_x, pixel_y] = b, g, r

    # Returns to the original size by slicing
    img = padded_img[:height, :width, :]

    #
    cv2.imshow("image", img)
    cv2.waitKey(0)
