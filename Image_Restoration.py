import cv2

img = cv2.imread('damaged_image.png')
mask = cv2.imread('mask.png', 0)
dst = cv2.inpaint(img, mask, 3, cv2.INPAINT_NS)

cv2.imwrite('restored.png', dst)
