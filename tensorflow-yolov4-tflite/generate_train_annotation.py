from absl import app, flags, logging
import os
import pickle
from absl.flags import FLAGS
import cv2

f = open("demofile.txt", "w")
for entry in os.scandir('data/trafficsigndataset'):
    if(entry.path.split('.')[1] == 'jpg'):
        item = entry.path + " "
    
    if(entry.path.split('.')[1] == 'txt'):
        f_txt = open(entry.path, "r")
        for x in f_txt:
            item = item + x
        f_txt.close()

    if(entry.path.split('.')[1] == 'txt'): f.write(item + "")
f.close()