from tkinter import *
from PIL import ImageTk, Image
import numpy as np
import math
import random
import matplotlib.pyplot as plt

root = Tk()
root.title("K-Means")
root.geometry("740x580+800+300")


photo = ImageTk.PhotoImage(file='./TestImage.jpg')
label1 = Label(root, image=photo)
label2 = Label(root, text="클러스터 개수 : ")
text = Text(root, height=2,width=5)

label1.pack() 
label2.pack()
text.pack()



image = Image.open('./TestImage.jpg')


def FindMinDistance(distance, k):
    min = distance[0]
    minIndex = 0
    for i in range(0,k):
        if distance[i] < min:
            min = distance[i]
            minIndex = i
    return minIndex


def GetEditedImage():
    k = int(text.get(1.0, END+"-1c"))
    img = np.array(image)
    img_height,img_width,channel = img.shape
    dataVector = np.ndarray(shape=(img_width * img_height, 5), dtype=float)
    dataVector_scaled = preprocessing.normalize(dataVector)

    minValue = np.amin(dataVector_scaled)
    maxValue = np.amax(dataVector_scaled)

    centroids_w = [0 for j in range(k)]
    centroids_h = [0 for j in range(k)]
    for i in range(k):
        centroids_w[i] = random.randint(0,img_width)
        centroids_h[i] = random.randint(0,img_height)
    distance = [0 for i in range(k)]
    for y in range(0,img_height):
        for x in range(0,img_width):
            for j in range(0,k):
                r = abs(int(img[y][x][0]) - int(img[centroids_h[j]][centroids_w[j]][0]))
                g = abs(int(img[y][x][1]) - int(img[centroids_h[j]][centroids_w[j]][1]))
                b = abs(int(img[y][x][2]) - int(img[centroids_h[j]][centroids_w[j]][2]))

                distance[j] = int(math.sqrt(r * r + g * g)) + int(math.sqrt(g * g + b * b)) + int(math.sqrt(r * r + b * b))
            nearest = FindMinDistance(distance,k)
            img[y][x][0] = img[centroids_h[nearest]][centroids_w[nearest]][0]
            img[y][x][1] = img[centroids_h[nearest]][centroids_w[nearest]][1]
            img[y][x][2] = img[centroids_h[nearest]][centroids_w[nearest]][2]
    

    for i in range(0,k):
        plt.scatter(centroids_h[i],centroids_w[i],color='black')


    
    result_img = Image.fromarray(img)
    result_img.show()
    plt.show()




run_btn = Button(root, padx = 20, text="실행" , command=GetEditedImage)
run_btn.pack()




root.mainloop()

