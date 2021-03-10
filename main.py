import cv2 as cv2
import numpy as np
from matplotlib import pyplot as plt

import math

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def run_circles():
	#img = cv2.imread('data/target.jpg', 0)
	img_blur = cv2.medianBlur(img, 5)
	#cimg = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
	circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 20,
							   param1=50,param2=30, minRadius=50, maxRadius=150)

	circles = np.uint16(np.around(circles))
	for i in circles[0, :]:
		# draw the outer circle
		cv2.circle(gray, (i[0], i[1]), i[2], (0, 0, 255), 2)
		# draw the center of the circle
		cv2.circle(gray, (i[0], i[1]), 2, (255, 0, 0), 3)


def run_cv():
	#img = cv2.imread('data/target.jpg',0)
	#gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

	th, th1 = cv2.threshold(img, 100, 255,
					cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

	cnts = cv2.findContours(th1, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

	contours, hierarhy = cv2.findContours(th1, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	s1 = 25
	s2 = 200
	xcnts = []

	i = 0;
	for cnt in cnts:
		(x, y), radius = cv2.minEnclosingCircle(cnt)
		size = cv2.contourArea(cnt)
		if s1 < size < s2 and radius < 25:
			xcnts.append(cnt)

	print("\nDots number: {}".format(len(xcnts)))

	cv2.drawContours(gray, xcnts, -1, (0, 255, 0), 3)

if __name__ == '__main__':
	img = cv2.imread('data/target.jpg', 0)
	gray = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)

	run_cv()
	run_circles()

	plt.imshow(gray)
	plt.savefig('data/tmp.jpg')
	plt.show()


