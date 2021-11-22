# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 11:37:44 2021

@author: asus


https://scikit-image.org/docs/stable/user_guide/getting_started.html

https://scikit-image.org/docs/stable/auto_examples/color_exposure/plot_histogram_matching.html#sphx-glr-auto-examples-color-exposure-plot-histogram-matching-py

https://scikit-image.org/docs/stable/auto_examples/transform/plot_rescale.html#sphx-glr-auto-examples-transform-plot-rescale-py


error PNGs
https://www.google.com/search?q=libpng+warning%3A+iCCP%3A+known+incorrect+sRGB+profile+python+fix&sxsrf=AOaemvK4ZeSvDTL2z87jXPE4D1zSPaLwow%3A1636042529348&ei=IQeEYcrbFJS95OUPjNGA-AM&oq=libpng+warning%3A+iCCP%3A+known+incorrect+sRGB+profile+python+fix&gs_lcp=Cgdnd3Mtd2l6EAM6BwgAEEcQsAM6BQgAEIAEOgYIABAWEB46CAghEBYQHRAeSgQIQRgAUNuJZFi1jGRg9Y1kaAJwAngAgAFWiAGVApIBATSYAQCgAQHIAQjAAQE&sclient=gws-wiz&ved=0ahUKEwiK8LGujf_zAhWUHrkGHYwoAD8Q4dUDCA8&uact=5



IMAGE LUMINANCE
https://stackoverflow.com/questions/6442118/python-measuring-pixel-brightness
https://stackoverflow.com/questions/596216/formula-to-determine-perceived-brightness-of-rgb-color


color transfer git
https://github.com/jrosebr1/color_transfer
https://medium.com/codezest/super-fast-color-transfer-algorithm-bd1a76bc7619
https://ieeexplore.ieee.org/document/946629/citations#citations
https://towardsdatascience.com/histogram-matching-ee3a67b4cbc1
https://www.pyimagesearch.com/2021/02/08/histogram-matching-with-opencv-scikit-image-and-python/


"""

#%% 

import matplotlib.pyplot as plt

import skimage
import numpy as np
import os

from skimage import data   # example images
from skimage import exposure
from skimage.exposure import match_histograms
from skimage import io # to import one image
from natsort import natsorted, ns # to import several images

import cv2

import scipy


#%% paths
 
imagePath   = 'C:\\Dropbox\\TASK\\2_SELECTED_STIMS\\'

imageFolder = ['B1_green','B2_blue','B3_red','training_stims']

#%% directory list
    
readPath = imagePath + imageFolder[0] + '\\'
list_files = os.listdir(readPath)

#%%
list_files = natsorted(list_files) # ordena archivos inteligentemente
print(list_files)

#%% read images OPENCV

image_list = []
for filename in list_files: 
    image_list.append(cv2.imread(readPath + filename,cv2.IMREAD_UNCHANGED))
    print(filename)
print('Done')

imagen = image_list[1]

io.imshow(imagen)
# plt.show(imagen)

# for i in range(100,1300): print(imagen[i,i])

#%% match histograms


reference = image_list[3]

image = image_list[8]

matched = match_histograms(image, reference, multichannel=True)


fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 3),
                                    sharex=True, sharey=True)
for aa in (ax1, ax2, ax3):
    aa.set_axis_off()

ax1.imshow(image)
ax1.set_title('Source')
ax2.imshow(reference)
ax2.set_title('Reference')
ax3.imshow(matched)
ax3.set_title('Matched')

plt.tight_layout()
plt.show()

#%%

matched_list = []

for index in image_list:
    matched_list.append = match_histograms(image_list[index], reference)
    





#%%



for i in range(900,950):
    for j in range(1100,1150):
        print(imagen[i,j])

#%% 

color = (0,0,0,255)
thickness = 10
start_point = (900,1100)
end_point = (1400,1400)      
  
imagen_square = cv2.rectangle(imagen,start_point,end_point,color,thickness)      
 
io.imshow(imagen_square)


       
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
'''

#%% read images SCIKIT

image_list = []
for filename in list_files:
    image_list.append(io.imread(readPath + filename  ))
    print(filename)
print('a')


imagen = image_list[3]

io.imshow(imagen)
plt.show(imagen)        

#%% read images SCIPY

image_list = []
for filename in list_files:
    image_list.append(imread(readPath + filename, mode='RGBA'))
    print(filename)
print('Done')

imagen = image_list[0]

io.imshow(imagen)
plt.show(imagen)

#%% read images matplotlib

import matplotlib.image as mpimg


image_list = []
for filename in list_files:
    image_list.append(mpimg.imread(readPath + filename))
    print(filename)
print('Done')

imagen = image_list[0]

io.imshow(imagen)
plt.show(imagen)


#%% read images PIL
from PIL import Image
image_list = []
for filename in list_files:
    image_list.append(Image.open(readPath + filename))
    print(filename)
print('Done')

imagen = image_list[3]

io.imshow(imagen)
plt.show(imagen)



#%%

imagen = io.imread(readPath + 'fabula-arbol-no-sabia-quien-era.jpg')

# imagen = data.coffee()


io.imshow(imagen)
plt.show()





#%% show image

reference = image_list[0]

io.imshow(reference)
plt.show()

#%% save image

io.imsave([reference + '_test'])





#%%

exposure.histogram(, source_range='dtype')




'''

























