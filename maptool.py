#!/usr/bin/python
# -*-coding:utf-8-*-

"""
author:gadfy
"""

import cv2
import numpy
import zlib
import base64

src = "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"



src_d64 = base64.b64decode(src)
src_zlib = zlib.decompress(src_d64)
maps = eval(src_zlib)

print len(maps)

height = 181
width = 168

canvas = numpy.zeros((width, height, 3), numpy.uint8)
print canvas.shape

#(b, g, r)
colors = [(0xee,0xee,0xee), (0xff,0xec,0xd9), (0xff,0xcf,0xa0), (0xff,0xbb,0x79), (0x97,0x97,0x97), (0xa1,0xa1,0xf9), (0x81,0xf2,0xff)]

tmp = []

for i in range(len(maps)):
    for j in range(4):
        a = (maps[i] >> 4*j) & 15
        if not a in tmp:
            tmp.append(a)
        x = (4*i + j) % width
        y = (4*i + j) / width
        canvas[x][y] = colors[a & 7]

cv2.imwrite("demo1.jpg", canvas)
print tmp

# flip>0 水平镜像, =0 垂直镜像, <0 水平垂直镜像
canvas1 = cv2.flip(canvas, 1)
cv2.imwrite("demo2.jpg", canvas1)

canvas2 = cv2.flip(canvas, 0)
cv2.imwrite("demo3.jpg", canvas2)

canvas3 = cv2.flip(canvas, -1)
cv2.imwrite("demo4.jpg", canvas3)

canvas4 = cv2.resize(canvas, (2*height, 2*width)) # 放大效果不明显
cv2.imwrite("demo5.jpg", canvas4)
cv2.imshow("demo", canvas)
cv2.waitKey()
cv2.destroyWindow("demo")
