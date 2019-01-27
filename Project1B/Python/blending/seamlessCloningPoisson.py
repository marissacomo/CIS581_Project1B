'''
  File name: seamlessCloningPoisson.py
  Author: Marissa Como
  Date created: 9/23/18

• (INPUT) sourceImg: h × w × 3 matrix representing the source image.
• (INPUT) targetImg: h' × w' × 3 matrix representing the target image.
• (INPUT) mask: The logical matrix h × w representing the replacement region.
• (INPUT) offsetX: The x-axis offset of the source image with respect to the target image.
• (INPUT) offsetY: The y-axis offset of the source image with respect to the target image.
• (OUTPUT) resultImg: h' × w' × 3 matrix representing the resulting cloned image.

# 1.6 Wrapper Function - 
'''
#!/usr/local/bin/python3
from getIndexes import getIndexes
from getCoefficientMatrix import getCoefficientMatrix
from getSolutionVect import getSolutionVect
from reconstructImg import reconstructImg
from maskImage import maskImage

 # 1.6 Wrapper Function - This function calls getIndexes.py, getCoefficientMatrix.py, 
 # getSolutionVect.py, reconstructImg.py and solves the linear system.
def seamlessCloningPoisson(source, target, mask, offsetY, offsetX): 

  # 1.2 Index the Pixels 
  indexes = getIndexes(mask)

  # 1.3 Compute the Coefficient Matrix
  coeffA = getCoefficientMatrix(indexes)  

  # 1.4 Compute the Solution Vector
  indices = getIndexes(mask)
  color = getSolutionVect(indices, source, target, offsetX, offsetY, mask)
  
  # 1.5 Seamlessly Clone the Image
  indices2 = getIndexes(mask)
  resultImg = reconstructImg(indices2, color, target, coeffA) 

  return resultImg


