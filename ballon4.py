import numpy as np
import sympy as sp
from math import *
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches
import matplotlib.path

it_cnt = 10000
tao = 0.01
Ax, Bx, Ay, By, C = -0.353, 0.353, 0.3, 0.3, 3.0 * np.pi / 8.0
x = np.array([1.0, 1.0, 1.0, 1.0, 1.0])
for i in range(it_cnt):
  x -= np.array([x[0] + x[2] * cos(3.0 * np.pi / 2.0 - x[3]) - Ax,
                 x[1] + x[2] * cos(3.0 * np.pi / 2.0 + x[4]) - Bx,
                 x[2] + x[2] * sin(3.0 * np.pi / 2.0 - x[3]) - Ay,
                 (x[3] + x[4]) * x[2] + (x[1] - x[0]) - C,
                 x[2] + x[2] * sin(3.0 * np.pi / 2.0 + x[4]) - By]) * tao
print(x)
plt.grid()
plt.xlim(-1, 1)
plt.ylim(-0.1, 1)

axes = plt.gca()
axes.set_aspect("equal")

arc1 = mpl.patches.Arc((x[0], x[2]), 2.0 * x[2], 2.0 * x[2], theta1 = (270.0 - x[3] * 180.0 / np.pi), theta2 = 270.0)
arc2 = mpl.patches.Arc((x[1], x[2]), 2.0 * x[2], 2.0 * x[2], theta1 = 270.0, theta2 = 270.0 + x[4] * 180.0 / np.pi)
plt.plot([Ax, Bx], [Ay, By])
plt.plot([x[0], x[1]], [0, 0])
axes.add_patch(arc1)
axes.add_patch(arc2)
plt.show()
