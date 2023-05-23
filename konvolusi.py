# -*- coding: utf-8 -*-
"""Konvolusi.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1DRuPCsnk9edGgIx9AuHNxy4KslENLH9T

1207070025 Caesar Noor
"""

# Commented out IPython magic to ensure Python compatibility.

# impor library
import matplotlib.pyplot as plt
# %matplotlib inline

from skimage import data
from skimage.io import imread
from skimage.color import rgb2gray 
import numpy as np

import cv2

# membaca dan memberi label pada gambar input 
citra1 = imread(fname="gedung.tif")
print(citra1.shape)

# menampilkan gambar input
plt.imshow(citra1, cmap='gray')

# rumus fungsi proses konvolusi
kernel = np.array([[-1, 0, -1], 
                   [0, 4, 0], 
                   [-1, 0, -1]])

# memberi label pada gambar hasil konvolusi atau output
citraOutput = cv2.filter2D(citra1, -1, kernel)

# mengatur ukuran gambar input dan output
fig, axes = plt.subplots(1, 2, figsize=(12, 12))
ax = axes.ravel()

# menampilkan dan memberi judul pada gambar input dan output
ax[0].imshow(citra1, cmap = 'gray')
ax[0].set_title("Citra Input")
ax[1].imshow(citraOutput, cmap = 'gray')
ax[1].set_title("Citra Output")