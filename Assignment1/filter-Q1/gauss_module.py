# import packages: numpy, math (you might need pi for gaussian functions)
import numpy as np
import math
from scipy.signal import convolve2d

def gauss(sigma):

	x= np.linspace(-3*sigma,3*sigma,11)
	Gx=1/(np.sqrt(2*np.pi)*sigma)*np.exp(-1*x**2/(2*sigma**2))
	# Gx=Gx/np.max(Gx)
	return Gx, x


def gaussderiv(img, sigma):
	Dy,x=gaussdx(sigma)
	Dy=Dy[: ,None]
	Dx=Dy.T

	imgDx=convolve2d(img,Dx,mode='same')
	imgDy=convolve2d(img,Dy,mode='same')

	return imgDx, imgDy

def gaussdx(sigma):

	x= np.linspace(-3*sigma,3*sigma,11)
	D=-1/(np.sqrt(2*np.pi)*sigma**3)*x*np.exp(-1*x**2/(2*sigma**2))
	return D, x

def gaussianfilter(img, sigma):

	Gx,x=gauss(sigma)
	Gx=Gx[: ,None]
	Gy=Gx.T
	Result_Gx=convolve2d(img,Gx,mode='same')
	outimage=convolve2d(Result_Gx,Gy,mode='same')

	return outimage
