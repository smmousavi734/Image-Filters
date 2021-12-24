import cv2
import PIL
import numpy as np
import matplotlib.pyplot as plt
from PIL import ImageEnhance


def filtering():
    img = cv2.imread(img_source)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    #Bluring
    av3 = cv2.blur(img,(3,3))
    av5 = cv2.blur(img,(5,5))
    plotting("Bluring", img,av3,"Averaging - 3x3",av5, "Averaging - 5x5", None)

    #Median
    median = cv2.medianBlur(img,5)
    blur = cv2.blur(img,(5,5))
    plotting("Median", img, median, "Median", blur, "Blur", None)

    #Gaussian
    gauss = cv2.GaussianBlur(img, (3,3), 1,1)
    blur = cv2.blur(img,(3,3))
    plotting("Gaussian", img, gauss, "Gaussian", blur, "Blur", None)

    #Bilateral
    bylat = cv2.bilateralFilter(img,9,75,75)
    gauss = cv2.GaussianBlur(img, (5,5), 75, 75)
    plotting("Bilateral", img, bylat, "Bilateral", gauss, "Gaussian", None)

def enhancing():
    img = PIL.Image.open(img_source)

    converter = ImageEnhance.Brightness(img)
    img2 = converter.enhance(0.5)
    img3 = converter.enhance(2)

    plotting("Brightness", img, img2, "Half Brightness", img3, "Double Brightness", None)

    converter = ImageEnhance.Sharpness(img)
    img2 = converter.enhance(0.5)
    img3 = converter.enhance(2)
    plotting("Sharpness", img, img2, "Half Sharpness", img3, "Double Sharpness", None)

    converter = ImageEnhance.Contrast(img)
    img2 = converter.enhance(0.5)
    img3 = converter.enhance(2)
    plotting("Contrast", img, img2, "Half Contrast", img3, "Double Contrast", None)

    converter = ImageEnhance.Color(img)
    img2 = converter.enhance(0.5)
    img3 = converter.enhance(2)
    plotting("Saturation", img, img2, "Half Color", img3, "Double Color", None)

def sharpening():
    # loading image
    img0 = cv2.imread(img_source,)

    # converting to gray scale
    gray = cv2.cvtColor(img0, cv2.COLOR_BGR2GRAY)
    img0 = cv2.cvtColor(img0, cv2.COLOR_BGR2RGB)
    # remove noise
    img = cv2.GaussianBlur(gray,(3,3),0)

    # convolute with proper kernels
    laplacian = cv2.Laplacian(img,cv2.CV_8UC1) #cv2.CV_8UC1 = gray scale = 0
    sobelxy = cv2.Sobel(img,cv2.CV_8UC1,1,1,ksize=5)

    plotting("Sharpening", img0, laplacian, "Laplacian", sobelxy, "Sobel X,Y", "gray")

def plotting(pltname, img1, img2, str2, img3, str3, cmp):
    
    plt.figure(pltname)
    
    plt.subplot(131)
    plt.imshow(img1,cmap = cmp)
    plt.title("Original")

    plt.subplot(132)
    plt.imshow(img2, cmap = cmp)
    plt.title(str2)

    plt.subplot(133)
    plt.imshow(img3, cmap = cmp)
    plt.title(str3)
    
    plt.show()

img_source = "D:\\2.jpeg"

filtering()
enhancing()
sharpening()

cv2.waitKey(0)