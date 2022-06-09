

import argparse
import numpy as np
import os
import cv2
import pandas as pd


WIDTH = 346
HEIGHT = 260


def draw_color(events, N):
    img = np.ones(shape=(HEIGHT, WIDTH, 3), dtype='uint8') * 128
    h_width = int(WIDTH/2)
    h_height = int(HEIGHT/2)
    red = (0,0,255)
    green = (0,255,0)
    blue = (255,0,0)
    black = (0,0,0)
    counter = 0
    for t,x,y,p in zip(events['timestamp'], events['x'], events['y'], events['polarity']):
        row = x%2       # used to check bayer.
        col = y%2
        x = int(x/2)
        y = int(y/2)
        if row==0 and col==0:       # red
            img[y, x] = red if p == 1 else black
        elif row==1 and col==0:     # green
            img[y, x+h_width] = green if p == 1 else black
        elif row==0 and col==1:     # green
            img[y+h_height, x] = green if p == 1 else black
        else:                       # blue
            img[y+h_height, x+h_width] = blue if p == 1 else black
        counter += 1
        if counter == N:
            counter = 0
            cv2.imshow('color', img)
            if cv2.waitKey(0) == ord('q'):
                os.abort()
            img = np.ones(shape=(HEIGHT, WIDTH, 3), dtype='uint8') * 128


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='davis346 color drawer')
    parser.add_argument('--filename', type=str, default='davis_color.csv')
    parser.add_argument('--events_number', type=int, default=3e4)
    args = parser.parse_args()

    dataframe = pd.read_csv(args.filename, sep=',', skiprows=1, header=0)
    draw_color(dataframe, args.events_number)
