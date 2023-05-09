from math import *
import matplotlib as mpl
import matplotlib.patches
import matplotlib.pyplot as plt
import numpy as np
from celluloid import Camera


def square_sum(y):
    return (y[0] + y[10] * cos(y[20]) - Ax)**2 + \
        (y[5] + y[10] * sin(y[20]) - Ay)**2 + \
        (y[1] + y[11] * cos(y[21] + y[16]) - Bx)**2 + \
        (y[6] + y[11] * sin(y[16] + y[21]) - By)**2 + \
        (y[2] + y[12] * cos(y[17] + y[22]) - y[1] - y[11] * cos(y[21]))**2 + \
        (y[7] + y[12] * sin(y[17] + y[22]) - y[6] - y[11] * sin(y[21]))**2 + \
        (y[2] + y[12] * cos(y[17] + y[22]) - y[4] - y[14] * cos(y[24] + y[19]))**2 + \
        (y[7] + y[12] * sin(y[17] + y[22]) - y[9] - y[14] * sin(y[24] + y[19]))**2 + \
        (y[0] + y[10] * cos(y[20] + y[15]) - y[2] - y[12] * cos(y[22]))**2 + \
        (y[5] + y[10] * sin(y[20] + y[15]) - y[7] - y[12] * sin(y[22]))**2 + \
        (y[0] + y[10] * cos(y[20] + y[15]) - y[3] - y[13] * cos(y[23]))**2 + \
        (y[5] + y[10] * sin(y[20] + y[15]) - y[8] - y[13] * sin(y[23]))**2 + \
        (y[3] - y[4])**2 + \
        (y[8] - y[13] + y[14] - y[9])**2 + \
        (pt0 * (y[7] - y[5]) + pb0 * (y[8] - y[7]))**2 + \
        (pt0 * (y[2] - y[0]) + pb0 * (y[3] - y[2]))**2 + \
        (pt0 * (y[7] - y[6]) + p * (y[6] - y[9]) + pb0 * (y[9] - y[7]))**2 + \
        (pt0 * (y[2] - y[1]) + p * (y[1] - y[4]) + pb0 * (y[4] - y[2]))**2 + \
        (pb0 * y[13] - (pb0 - p) * y[14])**2 + \
        (y[10] * y[15] - rt * phi1_nd)**2 + \
        (y[11] * y[16] - rt * phi2_nd)**2 + \
        (y[12] * y[17] - rt * phi3_nd)**2 + \
        (y[13] * y[18] + y[14] * y[19] - rb * phi4_5_nd)**2 + \
        (y[23] - 3 * np.pi / 2 + y[18])**2


def lexa(y):
    z = np.zeros(25)
    for k in range(0, 24):
        z[k] = (square_sum(y + h[k]) - square_sum(y - h[k])) / H
    # print(z)
    # print(square_sum(y))
    return y - z * tao


frames = 100
it_cnt = 10000
it_cnt2 = 10000
H = 0.00001
tao = 0.005
delta_t = 0.01
m = 100.0
kp = 0.0002
p = 0
g = 9.8
Vy = 0.0

alpha5 = 3.0 * np.pi / 2.0
Ax = 0.0
Ay = 1.9
Bx = 0.6
By = 1.3
rt = 0.6
rb = 0.38
pt0 = 24000.0 * kp
pb0 = 8000.0 * kp
phi1_nd = 2.753364902
phi2_nd = 1.182568575
phi3_nd = 0.7764555030
phi4_5_nd = 5.001905970

x = np.array([0.0, 0.0, 0.0, 0.0, 0.0, 1.3,1.3, 1.3, 0.44, 0.44, rt, rt, rt, rb, rb, phi1_nd, phi2_nd, phi3_nd, phi4_5_nd / 2.0, phi4_5_nd / 2.0, pi / 2, 5.1, 4.32, 2.21, 3 * pi / 2])
h = np.zeros((25, 25))
for i in range(0, 24):
    h[i][i] = H
# x = np.full(25, 1)


fig, axes = plt.subplots()
axes.set_aspect("equal")

plt.grid()
plt.xlim(-1, 1)
plt.ylim(0, 2)

camera = Camera(fig)

for j in range(0, frames + 1):
    # Vy += (p * (x[1] - x[0]) - m * g) / m * delta_t
    # Ay += Vy * delta_t
    # By = Ay

    axes = plt.gca()
    axes.set_aspect("equal")

    actual_cnt = it_cnt
    if j > 0:
        actual_cnt = it_cnt2

    p = 2000 * kp * sin(j / frames * pi)
    while square_sum(x) > 0.0001:
        x = lexa(x)
    for i in range(0, 5):
        d = 2 * x[10 + i]
        arc = mpl.patches.Arc((-x[i], x[5 + i]), d, d,
                              theta1=(180.0 * (1 - x[20 + i] / np.pi - x[15 + i] / np.pi)),
                              theta2=(180.0 - x[20 + i] * 180.0 / np.pi), color='red')
        axes.add_patch(arc)

    plt.plot([Ax, -Bx], [Ay, By], color='purple')
    # plt.plot(x[1], x[5], 'ro')
    # print(x[3] * x[2] + x[1] - x[0] + x[4] * x[5])

    print(j + 1)
    camera.snap()
animation = camera.animate(interval=20, repeat_delay=0)
# animation.save('balon.mp4')
plt.show()
