import serial as sr
import matplotlib.pyplot as plt
import numpy as np
import time
s=sr.Serial('COM5',9600)

plt.close('all')
plt.figure()
plt.ion()

data = np.array([])

while True:
    
    height = float(s.readline().decode())
    data = np.append(data,height)
    plt.cla()
    plt.plot(data)
    plt.pause(0.55)
