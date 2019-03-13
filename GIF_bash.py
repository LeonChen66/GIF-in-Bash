# -*- coding: utf-8 -*-
import cv2
import numpy as np
import os
import imageio
import time
from subprocess import call
import argparse
parser = argparse.ArgumentParser(description='Optional app description')
parser.add_argument('-f', '--filename', type=str,
                    help='input the GIF filename')
parser.add_argument('-s', '--size', type=int,
                    help='Output size', default=54)
parser.add_argument('-t', '--threshold', type=int,
                    help='Color mapping threshold', default=128)
parser.add_argument('-q', '--freq', type=float,
                    help='Frequency of GIF', default=0.2)
args = parser.parse_args()
size = args.size
timeout = args.freq
def trans_color(img,threshold=150):
    #img = cv2.imread(filename)
    img = cv2.resize(img, (size, size), interpolation=cv2.INTER_CUBIC)

    # Opencv is BGR
    white = np.where((img[:, :, 0] > threshold) & (
        img[:, :, 1] > threshold) & (img[:, :, 2] > threshold))
    black = np.where((img[:, :, 0] < threshold) & (
        img[:, :, 1] < threshold) & (img[:, :, 2] < threshold))
    red = np.where((img[:, :, 0] < threshold) & (
        img[:, :, 1] < threshold) & (img[:, :, 2] > threshold))
    green = np.where((img[:, :, 0] < threshold) & (
        img[:, :, 1] > threshold) & (img[:, :, 2] < threshold))
    blue = np.where((img[:, :, 0] > threshold) & (
        img[:, :, 1] < threshold) & (img[:, :, 2] < threshold))
    yellow = np.where((img[:, :, 0] < threshold) & (
        img[:, :, 1] > threshold) & (img[:, :, 2] > threshold))
    purple = np.where((img[:, :, 0] > threshold) & (
        img[:, :, 1] < threshold) & (img[:, :, 2] > threshold))
    bluegreen = np.where((img[:, :, 0] > threshold) & (
        img[:, :, 1] > threshold) & (img[:, :, 2] < threshold))
    output = [[0]*size for _ in range(size)]
    output = np.array(output)
    output[white] = 47
    output[black] = 40
    output[green] = 42
    output[red] = 41
    output[blue] = 44
    output[yellow] = 43
    output[purple] = 45
    output[bluegreen] = 46 
    return output

#cmd = 'echo -e '
def generate(output):
    cmd = ''
    for i in range(size):
        cmd += '\n'
        for j in range(size):
            cmd += "\033[{};36m  \033[0m".format(output[i][j])
    print(cmd)

# define clear function


def clear():
    # check and make call for specific operating system
    _ = call('clear' if os.name == 'posix' else 'cls')

def main():

    gif = imageio.mimread(args.filename)

    imgs = [cv2.cvtColor(img, cv2.COLOR_RGB2BGR) for img in gif]
    #img = cv2.imread('butter.jpg')
    while 1:
        for img in imgs:
            output = trans_color(img,args.threshold)
            time.sleep(timeout)
            generate(output)

if __name__ == "__main__":
    main()
