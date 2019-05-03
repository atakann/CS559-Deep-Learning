#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Apr  7 14:49:20 2019

@author: atakanserbes
"""

import numpy as np
from numpy import asarray
import matplotlib.pyplot as plt
#import sys
import os
from os import listdir
from PIL import Image
#from skimage import io


folder = "/Users/atakanserbes/Desktop/Spring 2019 - CS559/Deep Learning Homework/UTKFace_downsampled/test_set"

onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]


test_files = []
test_labels = []
i=0
for _file in onlyfiles:
    test_files.append(_file)
    label = _file.find("_")
    test_labels.append(int(_file[1:label]))
    
  
print("Files in test_files: %d" % len(test_files))


test_images = [] 
for img in listdir(folder):
    img = Image.open(os.path.join(folder, img))
    data = asarray(img)
    data = data.reshape(91, 91, 1)
    test_images.append(data)
    
test_images = np.array(test_images)
np.save('test.npy', test_images)
np.save('test_labels.npy', test_labels)