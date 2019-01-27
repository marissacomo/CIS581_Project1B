'''
  File name: helpers.py
  Author: Marissa Como
  Date created: 9/23/18
 
'''
#!/usr/local/bin/python3

def rgb2gray(I_rgb):
  r, g, b = I_rgb[:, :, 0], I_rgb[:, :, 1], I_rgb[:, :, 2]
  I_gray = 0.2989 * r + 0.5870 * g + 0.1140 * b
  return I_gray

# This function gets the pixels that are around the current pixel
#  returns an array of index pairs (neighbors)
def getNeighborhood(curr_index):
  i, j = curr_index
  neighbors = [(i + 1, j), (i - 1 , j), (i, j + 1), (i, j - 1)]
  return neighbors

# This function computes the laplacian at the current index, and helps create the A matrix
def laplacianOperator(source, curr_index):
  i, j = curr_index
  lap = (4 * source[i, j]) + (-1 * source[i + 1, j]) + (-1 * source[i - 1, j]) + (-1 * source[i, j + 1]) + (-1 * source[i, j - 1])
  return lap

# global variables to help determine the location of each pixel in relation to the mask's replacement region
inside = 0 
boundary = 1
outside = 2

# This function assess if the current pixel is inside, outside, or on the boundary of the mask's replacement region.
#   returns - inside, boundary, or outside
def inside_boundary_outside(curr_index, mask):
    if isInside(curr_index, mask) == False: # if the pixel is not inside, it is outside
        return outside
    if isBoundaryEdge(curr_index, mask) == True: # if the pixel is on the boundary of the replacement region
        return boundary
    return inside # if not outside or boundary, it is inside

# This function determines if the current pixel is inside the mask's replacement region.
#   True: if the pixel is inside the mask's replacement region
#   False: if the pixel is not inside the mask's replacement region
def isInside(curr_index, mask): 
    return mask[curr_index] == 1

# This function evaluates if the pixel is located on the boundary of the mask's replacement region.
#   False: if the pixel is not in the mask's replacement pixel region
#   True: if the pixel is not on the replacement region
def isBoundaryEdge(curr_index, mask):
    if isInside(curr_index, mask) == False:  # current index is not in the mask's replacement pixel region
      return False    
    # else -- current index is inside the mask's replacement region (it is 1)
    for neighbor in getNeighborhood(curr_index): 
        if isInside(neighbor, mask) == False: 
          return True  # The current index is in the replacement region & it's neighbor is NOT in the replacement region --> EDGE
    return False




