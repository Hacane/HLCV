# import packages: numpy, math (you might need pi for gaussian functions)
import numpy as np
import math
import matplotlib.pyplot as plt
	
from importlib import reload
import sys
def gauss(sigma):
	x= np.linspace(-3*math.ceil(sigma), 3*math.ceil(sigma), 3*2*math.ceil(sigma)+1,dtype='int') 
	G=np.exp(-(x*x)/(2*(sigma*sigma)))/(sigma*np.sqrt(2*np.pi))

	plt.plot(x,G, label="1D Gaussian of sigma = " + str(sigma))  # log log plot of the input data
	plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.) # the key of the graph
	plt.ylabel('guassin function' )
	plt.xlabel('x axis')
	plt.show()
     
	return G,x

def gaussderiv(img, sigma):

	img=np.asarray(img)
	if(len(img.shape)== 3):
		greyImg =  np.dot(img[...,:3], [0.299, 0.587, 0.144])
	else:
		greyImg=img
	imgDx =  np.copy(greyImg)
	imgDy =  np.copy(greyImg)
	D,x2 = gaussdx(sigma)
	plt.figure()
	plt.imshow(greyImg,cmap='gray')
	 
	for i in range(0,greyImg[1,:].size):
	    imgDx[:,i] = np.convolve(imgDx[:,i], D, mode='same')

	  
	    
	plt.figure()
	plt.imshow(imgDx,cmap='gray')


	for i in range(0,imgDy[:,1].size):
	    imgDy[i,:] = np.convolve(imgDy[i,:], D, mode='same')
	   
	    
	plt.figure()
	plt.imshow(imgDy,cmap='gray')
	return imgDx, imgDy

def gaussdx(sigma):
	x= np.linspace(-3*math.ceil(sigma), 3*math.ceil(sigma), 3*2*math.ceil(sigma)+1,dtype='int') 
	D=x*np.exp(-(x*x)/(2*(sigma*sigma)))/(-sigma*sigma*sigma*np.sqrt(2*np.pi))

	plt.plot(x,D, label="1D Gaussian derivative of sigma = " + str(sigma))  # log log plot of the input data
	plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left', borderaxespad=0.) # the key of the graph
	plt.ylabel('guassin derivative function' )
	plt.xlabel('x axis')
	plt.show()
	return D,x

def gaussianfilter(img, sigma):
 
	#img= plt.imread("./code/filter-Q1/graf.png")
	img=np.asarray(img)
	greyImg =  np.dot(img[...,:3], [0.299, 0.587, 0.144])
	kernel = np.outer(scipy.signal.windows.gaussian(3*2*sigma+1, sigma),scipy.signal.windows.gaussian(3*2*sigma+1, sigma))
	outimage = scipy.signal.fftconvolve(greyImg, kernel, mode='same')
	plt.figure()
	plt.imshow(greyImg,cmap='gray')
	plt.xlabel('input image')
	plt.figure()
	plt.imshow(outimage,cmap='gray')
	plt.xlabel('blurred output image with segma= ' + str(sigma))
	return outimage
