from sympy import *
from numpy import *
import matplotlib.pyplot as plt
import numpy as np
from scipy.linalg import solve

#function to calculate and plot losses
def calculate_losses(u, v, x):
    sum_L1 = 0
    sum_L2 = 0
    #array for storing L1 losses for every domain
    L1 = []
    #array for storing L2 Losses for every domain
    L2 = []
    #array for x axis values
    x_axis=[]
    y=[]
    for i in range(x):
        #calculating L1
        sum_L1 = sum_L1 + abs((u[i] - v[i]))
        #calculating L2
        sum_L2 = sum_L2 + ((u[i] - v[i]) * (u[i] - v[i]))
        L1.append(sum_L1)
        L2.append(sum_L2)
        x_axis.append(abs(u[i]-v[i]))
        y.append((u[i] - v[i]) * (u[i] - v[i]))

    print("Loss 1 : ", sum_L1)
    print("Loss 2 : ", sum_L2)

    plt.title("L1 vs L2")
    plt.xlabel("u-v")
    plt.ylabel("L1 vs L2")
    #plot L1
    plt.plot(x_axis, x_axis)
    #plot L2
    plt.plot(x_axis, y)
    plt.show()

    return 0


u = np.random.rand(3)  # vector u
v = np.random.rand(3)  # vector v
x = len(u) #length for the for loop

#passing the values to the function
calculate_losses(u, v, x)
