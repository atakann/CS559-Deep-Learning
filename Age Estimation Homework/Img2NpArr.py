#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  3 16:40:39 2019

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


folder = "/Users/atakanserbes/Desktop/Spring 2019 - CS559/Deep Learning Homework/UTKFace_downsampled/Deneme"

onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]


train_files = []
training_labels = []
i=0
for _file in onlyfiles:
    train_files.append(_file)
    label = _file.find("_")
    training_labels.append(int(_file[1:label]))
    
  
print("Files in train_files: %d" % len(train_files))


training_images = [] 
for img in listdir(folder):
    img = Image.open(os.path.join(folder, img))
    data = asarray(img)
    data = data.reshape(91, 91 ,1)
    training_images.append(data)
    
training_images = np.array(training_images)
np.save('training.npy', training_images)

np.save('training_labels.npy', training_labels)

#    
#image = Image.open("001_20161219140744200.jpg")
#data = asarray(image)
#data = data.reshape(91,91,1)
#
#print(data.shape)

#dataset = np.ndarray(shape=(len(train_files), 91, 91, 1),dtype=np.float32)
#    
#images = []
#i = 0
#for img in train_files[0:31]:
#    img = Image.open(img)
#    # Convert to Numpy Array
#    image = np.array(img)
#    image = image.reshape(91, 91, 1)
#    images.append(dataset) 
#
#
#print("All images to array!")


#path = "/Users/atakanserbes/Desktop/Spring 2019 - CS559/Deep Learning Homework/UTKFace_downsampled/Deneme"
#
#all_images = []
#for image_path in os.listdir(path):
#    img = io.imread(image_path , as_grey=True)
#    img = img.reshape([91, 91, 1])
#    all_images.append(img)
#x_train = np.array(all_images)

#image = cv2.imread("001_20161219140744200.jpg", cv2.IMREAD_GRAYSCALE)
#cv2.imshow("Example", image)
#cv2.waitKey(0)
#imglist = []
#img = np.array(image)
#img = img.reshape([91, 91, 1])
#imglist.append(img)
#print(img)



#img = open("001_20161219140744200.jpg")
#arr = np.array(img)

#plt.imshow(arr)
#from PIL import Image
#import numpy as np
#im = Image.open('1.jpg')
#im2arr = np.array(im) 