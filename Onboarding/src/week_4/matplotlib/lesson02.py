"""Lesson 02: Working with Multiple Subplots in Matplotlib"""

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 100)
s = np.sin(x)
c = np.cos(x)
t = np.tan(x)
y1 = np.exp(x)

fig, axs = plt.subplots(2, 2, figsize=(12, 8))
plt.suptitle('Trigonometric and Exponential Functions', fontsize=16)
plt.subplots_adjust(hspace=0.5)

# Sine
axs[0, 0].plot(x, s, label='Sine', color='blue', marker='o', markersize=2)
axs[0, 0].set_title('Sine Function')
axs[0, 0].set_xlabel('x (radians)')
axs[0, 0].set_ylabel('sin(x)')
axs[0, 0].grid(True)
axs[0, 0].legend()

# Cosine (com escala personalizada, antiga aula 3)
axs[0, 1].plot(x, c, label='Cosine', color='orange')
axs[0, 1].set_title('Cosine Function with Custom Scale')
axs[0, 1].set_xlabel('x (radians)')
axs[0, 1].set_ylabel('cos(x)')
axs[0, 1].set_xticks(np.linspace(0, 2*np.pi, 5))
axs[0, 1].set_xticklabels(['0', 'π/2', 'π', '3π/2', '2π'])
axs[0, 1].set_yticks(np.linspace(-1, 1, 5))
axs[0, 1].set_yticklabels(['-1', '-0.5', '0', '0.5', '1'])
axs[0, 1].grid(True)
axs[0, 1].legend()

# Tangent
axs[1, 0].plot(x, t, label='Tangent', color='green')
axs[1, 0].set_title('Tangent Function')
axs[1, 0].set_xlabel('x (radians)')
axs[1, 0].set_ylabel('tan(x)')
axs[1, 0].grid(True)
axs[1, 0].legend()

# Exponential
axs[1, 1].plot(x, y1, label='Exponential', color='red')
axs[1, 1].set_title('Exponential Function')
axs[1, 1].set_xlabel('x (radians)')
axs[1, 1].set_ylabel('exp(x)')
axs[1, 1].grid(True)
axs[1, 1].legend()

plt.show()
