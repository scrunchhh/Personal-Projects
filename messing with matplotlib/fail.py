import numpy as np
import matplotlib.pyplot as plt
import keyboard
from random import randint
import easygui

origin = np.array([[0, 0, 0], [0, 0, 0]])
x = 0
y = 0


plt.quiver(*origin, x, y, color='black', scale = 21)
plt.show()
