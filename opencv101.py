import cv2
import numpy as np
from matplotlib import pyplot as plt

def readNwrite(img):
    print ("Press 'S' to save, Esc or 'Q' to quit")
    cv2.imshow('image', img)
    key = cv2.waitKey(0)
    if key == 27 or key == ord('q'): # Strike "ESC" and destroy the window
        cv2.destroyAllWindows()
    elif key == ord('s'): # Strike "S" and save the image
        cv2.imwrite('grayscaled.png',img)
        cv2.destroyAllWindows()

def blurImage(img):
    kernel = np.ones((5, 5), np.float32) / 25
    dst = cv2.filter2D(img, -1, kernel)

    plt.subplot(121), plt.imshow(img), plt.title('Original')
    plt.xticks([]), plt.yticks([])
    plt.subplot(122), plt.imshow(dst), plt.title('Averaging')
    plt.xticks([]), plt.yticks([])
    plt.show()

def showHistogram(img):
    color = ('b', 'g', 'r')
    for i, col in enumerate(color):
        histr = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(histr, color=col)
        plt.xlim([0, 256])
    plt.show()

def main():
    # read a image in greyscale
    img = cv2.imread('test.jpg', 0)
    #readNwrite(img)
    img = cv2.imread('test.jpg')
    blurImage(img)
    #showHistogram(img)

if __name__ == "__main__":
    main()