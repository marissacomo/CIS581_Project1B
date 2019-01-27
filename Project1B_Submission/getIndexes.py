'''
  File name: getIndexes.py
  Author: Marissa Como
  Date created: 9/23/18

• (INPUT) mask: The logical matrix h × w representing the replacement region.
• (OUTPUT) indexes: h' × w' matrix representing the indices of each replacement pixel. The value 0 means that is not a replacement pixel.
'''
#!/usr/local/bin/python3
import numpy as np
import cv2

def getIndexes(mask):
  indices = np.nonzero(mask)   
  indexes = zip(indices[0], indices[1])
  return indexes
