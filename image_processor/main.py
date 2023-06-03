import cv2
import numpy as np
import sys


filename = sys.argv[1]

img = cv2.imread(filename, cv2.IMREAD_GRAYSCALE)

(h, w) = img.shape[:2]
(cX, cY) = (w // 2, h // 2)

M = cv2.getRotationMatrix2D((cX, cY), 5.4, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))

spectrum_ROI = rotated[425:425 + 200, 610:650]
max_idx = np.unravel_index(np.argmax(spectrum_ROI), spectrum_ROI.shape)

line_length = 159
measuring_point = (max_idx[1] + 610, 425)
wavelengths = np.arange(measuring_point[1], measuring_point[1] + line_length) * (-103/58) + 42105/29

file_contents = "wavelength,intensity\n"

for i in range(0, line_length):
    intensity_profile = np.max(rotated[measuring_point[1] + i, measuring_point[0]-8:measuring_point[0]+8])
    file_contents += "{},{}\n".format(wavelengths[i], intensity_profile)

with open(filename + ".csv", "w") as f:
    f.write(file_contents)
