#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr  4 13:18:42 2019

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


folder = "/Users/atakanserbes/Desktop/Spring 2019 - CS559/Deep Learning Homework/UTKFace_downsampled/validation_set"

onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]


validation_files = []
validation_labels = []
i=0
for _file in onlyfiles:
    validation_files.append(_file)
    label = _file.find("_")
    validation_labels.append(int(_file[1:label]))
    
  
print("Files in vaildation_files: %d" % len(validation_files))


validation_images = [] 
for img in listdir(folder):
    img = Image.open(os.path.join(folder, img))
    data = asarray(img)
    data = data.reshape(91, 91, 1)
    validation_images.append(data)
    
validation_images = np.array(validation_images)
np.save('validation.npy', validation_images)
np.save('validation_labels.npy', validation_labels)