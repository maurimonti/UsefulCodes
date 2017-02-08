# pendulum with friction and great angles

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint


m = 1  # Kg
g = 9.81  # m/s**2
l = 10  # m
b = 0.1  # s**-1
a0 = 0.5  # s**-2
dt = 0.05  # s

deg0 = 120  # degrees
degv0 = 0  # degrees/s

th0 = np.radians(deg0)  # conversion in radiant
w0 = np.radians(degv0)


def f(t):
    # driving function
    return a0 * np.cos(g / l * t)


def dU_dx(U, t):
    # differential equation definition
    return [U[1], -g / l * np.sin(U[0]) - b * U[1] + f(t)]


def init():
    # initialization of the animation
    line.set_data([], [])
    point.set_data([], [])
    time_text.set_text('')
    return line, time_text


def animate(i):
    # core of the animation
    thisx = [0, xs[i]]
    thisy = [0, ys[i]]

    line.set_data(thisx, thisy)
    point.set_data(xs[i], ys[i])
    time_text.set_text(time_template % (i * dt))
    return line, point, time_text


if __name__ == '__main__':
    U0 = [th0, w0]  # theta(0) and thetadot(0)
    ts = np.arange(0, 100, dt)
    Us = odeint(dU_dx, U0, ts)  # solution of the ode
    thetas = Us[:, 0]  # actual solution in theta

    # plt.plot(ts, thetas)
# plt.xlabel("t(s)")
# plt.ylabel("theta")
    # plt.show()

    # passage to cartesian coordinates
    xs, ys = l * np.sin(thetas), - l * np.cos(thetas)

    fig = plt.figure()
    ax = fig.add_subplot(111, autoscale_on=False,
                         xlim=(- l - 1, l + 1), ylim=(- l - 1, l + 1),
                         aspect='equal')
    # ax.grid()

    line, = ax.plot([], [], 'ro-', lw=2)  # line
    point, = ax.plot([], [], 'go', markersize=20)  # "ball" of pendulum
    time_template = 'time = %.1fs'
    time_text = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    ani = animation.FuncAnimation(fig, animate, np.arange(1, len(thetas)),
                                  interval=25, blit=True, init_func=init,
                                  repeat=True)  # animation generation

    plt.show()
