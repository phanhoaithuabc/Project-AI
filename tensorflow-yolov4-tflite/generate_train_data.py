from absl import app, flags, logging
import os
import pickle
from os import listdir
from os.path import isfile, join
from absl.flags import FLAGS
import cv2

f = open("demofile.txt", "w")
for entry in os.scandir('/'):
    files.append(entry.path)