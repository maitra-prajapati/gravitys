import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from initialize import PhysicsObject

ball = PhysicsObject()
ball.mass = 5.0
ball.position = np.array([0.0,15.0], dtype = float)
dt = 0.05
ball.velocity = np.array([8.0, 0.0], dtype = float)
drag_coefficient = -0.01
trajectory = []
fig , plot = plt.subplots(1, 1, figsize = (12, 7))

def update(frame):
    ball.reset_forces()
    ball.update_linear(dt)
    ball.apply_force(drag_coefficient*ball.velocity)

    trajectory.append(ball.position.copy())

    plot.clear()
    plot.set_xlim(-20,1000)
    plot.set_ylim(-2000,200)

    xs, ys = zip(*trajectory)
    plot.plot(xs, ys, 'b-')

    plot.plot(ball.position[0], ball.position[1], 'ro', markersize = 10)
    plot.grid(True)


ani = FuncAnimation(fig, update, frames=400, interval=50, blit=False)
plt.tight_layout()
plt.show()
