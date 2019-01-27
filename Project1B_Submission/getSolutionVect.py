'''
  File name: getSolutionVect.py
  Author: Marissa Como
  Date created: 9/23/18

• (INPUT) indexes: h' × w' matrix representing the indices of each replacement pixel.
• (INPUT) source: h × w matrix representing one color channel of the source image.
• (INPUT) target: h' × w' matrix representing one color channel of target image.
• (INPUT) offsetX: The x-axis offset of the source image with respect to the target image.
• (INPUT) offsetY: The y-axis offset of the source image with respect to the target image.
• (INPUT) mask: 
• (INPUT) colorChannel: red / green / blue
• (OUTPUT) solVectorb: 1 × N vector representing the solution vector.

'''
#!/usr/local/bin/python3
import numpy as np
import helpers
import matplotlib.pyplot as plt

def getSolutionVect(indexes, source, target, offsetX, offsetY, mask):
  indices = list(indexes) # convert zip to a list
  N = len(indices) # number of points in mask
  b = np.zeros(N) # N x 1 vector

  for i, curr_index in enumerate(indices):
    b[i] = helpers.laplacianOperator(source, curr_index) # apply laplacian operator:  4*currindex + -1*neighbors
   
    # is the current index is on boundary of the pixels to be replaced  (ie. the mask at the current_index is 1 & a neighbor is not)  
    if helpers.inside_boundary_outside(curr_index, mask) == helpers.boundary:  
      for neighbor in helpers.getNeighborhood(curr_index):  # for neighbors in neigborhood of current pixel
        if helpers.isInside(neighbor,mask) == False: # neighbor is NOT inside the replacement region  
          b[i] = target[neighbor] + b[i]  # So we --> add the intensity of target[neighbor] to b

  return b






