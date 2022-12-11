import numpy as np
import matplotlib.pyplot as plt
import keyboard


def mag(l):
    return [i[0] for i in l]
def dir(l):
    return [i[1] for i in l]

V = np.array([[1,1], [-2, 2], [4, -7]])
Vp = V[0] + V[1]

origin = np.array([[0, 0, 0], [0, 0, 0]])

plt.quiver(*origin, V[:, 0], V[:, 1], color=['r', 'g', 'b'], scale = 21)
plt.quiver(*origin, Vp[0], Vp[1], color=['black'], scale = 21)
plt.show()