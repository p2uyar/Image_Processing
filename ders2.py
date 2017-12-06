
import numpy as np
import matplotlib.pyplot as plt
def createCircularMask(h, w, center=None, radius=None):
if center is None: # use the middle of the image
center = [int(w/2), int(h/2)]
if radius is None: # use the smallest distance between the center and image walls
radius = min(center[0], center[1], w-center[0], h-center[1])
y, x = np.ogrid[:h, :w]
dist_from_center = np.sqrt((x - center[0])**2 + (y-center[1])**2)
mask = dist_from_center <= radius
return mask
img = plt.imread("image.jpg")
h, w = img.shape[:2]
radius = h/4
mask = createCircularMask(h, w, radius=radius)
img[~mask] = 0
plt.imsave("image2.jpg", img, cmap="gray")
