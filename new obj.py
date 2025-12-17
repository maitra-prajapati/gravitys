import numpy as np
from gravitys.initialize import PhysicsObject

ball = PhysicsObject(mass = 23.0,
                     position=np.array([0, 19.9]),
                     velocity=np.array([23, 344.4]),
                     gravity= np.array([0, -9.8])
                     )
dt = 0.1
dragcoeff = -0.1
t = 4
frames = t/dt
print("TIME  |  POSI  |  RANGE")
for step in range(int(frames)):
    drag = dragcoeff * ball.velocity
    ball.reset_forces()
    ball.apply_force(drag)
    ball.update_linear(dt)
    ball.update_angular(dt)
    print(f"{t*dt:.1f}s | {ball.position} | {ball.velocity}")