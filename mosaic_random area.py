#!/usr/bin/env python

import cv2
import numpy as np


def set_bound(coordinate, sign, direction):
    global half_side_len
    global height
    global width

    coordinate_ = 0
    if sign == '+':
        coordinate_ = coordinate + half_side_len
    elif sign == '-':
        coordinate_ = coordinate - half_side_len

    if coordinate_ <= 0:
        coordinate_ = 0

    if direction == 'y' and coordinate_ >= height:
        coordinate_ = height - 1
    elif direction == 'x' and coordinate_ >= width:
        coordinate_ = width - 1

    return coordinate_


def on_mouse(event, x, y, flags, param):
    global img_cp
    global img_bool
    global half_side_len
    global height
    global width

    if x >= width - 1 or y >= height - 1:
        return

    if event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
        if img_bool[y, x]:
            print(1)
            return
        else:
            print(img_bool[y, x])

        # print(x, y)
        # print("x:", x - half_side_len, x + half_side_len + 1)
        # print("y:", y - half_side_len, y + half_side_len + 1)
        # b, g, r = img_cp[x, y]

        yt = set_bound(y, '-', 'y')
        yb = set_bound(y, '+', 'y')
        xl = set_bound(x, '-', 'x')
        xr = set_bound(x, '+', 'x')

        for mosaic_index_i in range(xl, xr + 1):
            for mosaic_index_j in range(yt, yb + 1):
                # print("x:", mosaic_index_i, x, "y:", mosaic_index_j, y)
                img_cp[mosaic_index_j, mosaic_index_i] = img[y, x]
                img_bool[mosaic_index_j, mosaic_index_i] = True

                cv2.imshow("img", img_cp)
        # input()

    # global preceding_pt
    #
    # if event == cv2.EVENT_LBUTTONUP or not cv2.EVENT_FLAG_LBUTTON:
    #     preceding_pt = (-1, -1)
    # elif event == cv2.EVENT_LBUTTONDOWN:
    #     preceding_pt = (x, y)
    # elif event == cv2.EVENT_MOUSEMOVE and flags == cv2.EVENT_FLAG_LBUTTON:
    #     current_pt = (x, y)
    #     print(x, y)
    #
    #     cv2.line(img=img_cp, pt1=preceding_pt, pt2=current_pt, color=(0, 0, 0),
    #              thickness=2, lineType=cv2.LINE_AA)
    #     cv2.imshow("img", img_cp)
    #
    #     preceding_pt = current_pt


if __name__ == '__main__':
    img = cv2.imread("3 (copy).jpeg", 1)

    height, width, _ = img.shape

    img_cp = np.copy(img)
    img_bool = np.zeros([height, width], dtype=bool)
    # print(type(img))

    # preceding_pt = None
    side_len = 20
    half_side_len = side_len // 2

    cv2.namedWindow("img")
    cv2.setMouseCallback("img", on_mouse)
    cv2.imshow("img", img_cp)
    cv2.waitKey(0)
