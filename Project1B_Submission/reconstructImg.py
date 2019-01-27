'''
  File name: reconstructImg.py
  Author: Marissa Como
  Date created: 9/23/18

• (INPUT) indexes: h' × w' matrix representing the indices of each replacement pixel.
• (INPUT) red/blue/green: 1 × N vector representing the intensity of the current color channel replacement pixel.
• (INPUT) targetImg: h' × w' × 3 matrix representing the target image.
• (OUTPUT) resultImg: h' × w' × 3 matrix representing the resulting cloned image.

'''
#!/usr/local/bin/python3
import numpy as np
from scipy.sparse import linalg
import matplotlib.pyplot as plt

def reconstructImg(indexes, color_b, target, A):
  indices = list(indexes) #convert zip to a list

  color_b = color_b.reshape(len(indices))
  
  x = linalg.cg(A, color_b) # unknown intensities

  cloneColor = np.copy(target).astype(int)

  for i,index in enumerate(indices):
      cloneColor[index] = x[0][i] # set the the previously unknown intensities

  return cloneColor

