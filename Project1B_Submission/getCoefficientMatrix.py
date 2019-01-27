'''
  File name: getCoefficientMatrix.py
  Author: Marissa Como
  Date created: 9/23/18

• (INPUT) indexes: h' × w' matrix representing the indices of each replacement pixel.
• (OUTPUT) coeffA: an N × N sparse matrix representing the Coefficient Matrix, where N is the number of replacement pixels.

'''
#!/usr/local/bin/python3
import numpy as np
import helpers

def getCoefficientMatrix(indexes): 
  indices = list(indexes).copy() #convert zip to a list
  N = len(indices) # number of points in mask
  A = np.zeros(shape=(N,N)) # coeffA Matrix

  for i, curr_index in enumerate(indices):
    A[i,i] = 4  # 4 at the current pixel -- will be 4's on the diagonal

    for neighbor in helpers.getNeighborhood(curr_index): # Get all neighboring points    
      if neighbor not in indices: # if neighbor is NOT in the mask (indices), keep it 0
        x = 0;
      else: # if neighbor is in the mask (indices), set indicies at the neighbor's index to -1
        j = indices.index(neighbor)
        A[i,j] = -1
  return A

