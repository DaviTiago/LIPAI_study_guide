"""Lesson 01: Introduction to Matplotlib"""
import matplotlib.pyplot as plt
import numpy as np

# Generate some data
x = np.linspace(0, 10, 100) # Create an array of 100 points from 0 to 10
y = np.sin(x)
y1 = np.cos(x) 

# Create a simple line plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, label='Sine Wave', color='blue')
plt.plot(x, y1, label='Cosine Wave', color='orange')
plt.title('Sine and Consine Wave Example')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
# Add a legend and grid
plt.legend()
plt.grid(True)
# Show the plot
plt.show()
