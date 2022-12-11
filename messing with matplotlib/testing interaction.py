import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import easygui
import matplotlib
matplotlib.use("TkAgg")

import pylab
plt.ion()

origin = np.array([[0, 0, 0], [0, 0, 0]])
mag = 0
dir = 0
fig = plt.quiver(*origin, mag, dir, color = 'black', scale = 21)

pause = False

def onclick(event):
    global pause
    mag = easygui.enterbox("Enter Magnitude")
    dir = easygui.enterbox("Enter Direction")
    pause = not pause

fig.canvas.mpl_connect('button_press_event', onclick)

def drawGraph(m, d):
    mag = m
    dir = d
    fig.clear()
    fig
    plt.draw()

while True:
    if not pause:
        drawGraph(mag, dir)
    fig.canvas.get_tk_widget().update() # process events
