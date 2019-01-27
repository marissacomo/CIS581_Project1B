'''
  File name: test_script.py
  Author:
  Date created:
'''
#!/usr/local/bin/python3
import numpy as np
import matplotlib.pyplot as plt
import os
from scipy import misc
from PIL import Image
import cv2

from maskImage import maskImage
from seamlessCloningPoisson import seamlessCloningPoisson


if __name__ == "__main__":
  folder = 'images'

  # source image
  im_path = os.path.join(folder,"mms.jpg") #"pencil.jpg") #"monkey.JPG") #"SourceImage.png") #"dog.jpg") #"plane.jpg")  # "SoureImage.png")
  source = np.array(Image.open(im_path).convert('RGB'))
  source = misc.imresize(source, 0.7, interp="bicubic")

  # target image
  im_path = os.path.join(folder, "pizza.png") #"desk.png") #"spaceship.JPG")#'TargetImage.png') #"field.jpg") #"sky.png") #'TargetImage.png')
  target = np.array(Image.open(im_path).convert('RGB'))
 # target = misc.imresize(target, 0.25, interp="bicubic")

  # pasting location on target
  offsetY  = 75 #125(gorilla) #200(dog)   #150(plane)  #75 (minion)
  offsetX  = 125 #75 #375        #150         #75

  # 1.1 Align the Source Image and Create its Mask
  mask, source_resized = maskImage(source, target, offsetY, offsetX)

  channels = source.shape[-1] # color channels (r g b)

  # Call the Wrapper Function
  seamlessClone = [seamlessCloningPoisson(source_resized[:,:,i], target[:,:,i], mask, offsetY, offsetX) for i in range(channels)]
  seamlessCloneMerged = cv2.merge(seamlessClone) # final result of the seamless cloning
 
  plt.figure()
  plt.imshow(seamlessCloneMerged);
  plt.title("Result");
  plt.show() 
