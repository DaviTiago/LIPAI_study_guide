"""Lesson 02: Multiple Subplots with Matplotlib"""
from cProfile import label
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
s = np.sin(x)
c = np.cos(x)
t = np.tan(x)
y1 = np.exp(x)

# Create a figure and axis
fig, axs = plt.subplots(2, 2, figsize=(10, 15))
plt.suptitle('Trigonometric and Exponential Functions', fontsize=16)
plt.subplots_adjust(hspace=0.5)

axs[0,0].plot(x, s, label='Sine', color='blue')
axs[0,0].set_title('Sine Function')
axs[0,0].set_xlabel('x (radians)')
axs[0,0].set_ylabel('sin(x)')
axs[0,0].grid(True)
axs[0,0].legend()

axs[0,1].plot(x, c, label='Cosine', color='orange')
axs[0,1].set_title('Cosine Function')
axs[0,1].set_xlabel('x (radians)')
axs[0,1].set_ylabel('cos(x)')
axs[0,1].grid(True)
axs[0,1].legend()

axs[1,0].plot(x, t, label='Tangent', color='green')
axs[1,0].set_title('Tangent Function')
axs[1,0].set_xlabel('x (radians)')
axs[1,0].set_ylabel('tan(x)')
axs[1,0].grid(True)
axs[1,0].legend()

axs[1,1].plot(x, y1, label='Exponential', color='red')
axs[1,1].set_title('Exponential Function')
axs[1,1].set_xlabel('x (radians)')
axs[1,1].set_ylabel('exp(x)')
axs[1,1].grid(True)
axs[1,1].legend()

plt.show()


