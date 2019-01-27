'''
  File name: maskImage.py
  Author: Marissa Como
  Date created: 9/23/18

• (INPUT) img: h × w × 3 matrix representing the source image.
• (OUTPUT) mask: h × w matrix representing the logical mask
• (RETURN) mask & resized source image
'''
#!/usr/local/bin/python3
import helpers
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import cv2
import os
from scipy import misc
from PIL import Image
import  mask_creator

# align the source image and the target image
def maskImage(source, target, offsetY, offsetX): 
  # source x,y
  s_y = source.shape[0]
  s_x = source.shape[1]

  # target x,y
  t_y = target.shape[0]
  t_x = target.shape[1]
  
  # make an array of all zeros, size of target image
  mask1 = np.zeros_like(target, dtype=np.uint8)

  mask1[offsetY:offsetY + s_y, offsetX:offsetX + s_x] = source.copy()

  mask = mask_creator.mask_creator_demo(mask1.copy())

  return [mask, mask1] #mask and resized source




