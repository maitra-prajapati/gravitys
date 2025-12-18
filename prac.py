import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from D1 import PhysicsObject1D

mass = 3.0
init_position = 2.0
init_velocity = -1
force = 2.0
dt = 0.01
obj = PhysicsObject1D(mass, init_position, init_velocity)  
positions = []
velocities = []

fig, (ax_pos, ax_vel) = plt.subplots(2, 1, figsize=(10, 6))

def update(frame):
    obj.reset_forces()
    obj.apply_force(force)
    obj.update_linear(dt)
    
    positions.append(obj.position)
    velocities.append(obj.velocity)
    
    ax_pos.clear()
    ax_pos.plot(positions, 'b-', linewidth=2)
    ax_pos.plot(len(positions)-1, obj.position, 'ro', markersize=15, label=f'x: {obj.position:.2f}')
    ax_pos.set_title('X Position'); ax_pos.grid(True)
    ax_pos.legend()
    
    ax_vel.clear()
    ax_vel.plot(velocities, 'g-', linewidth=2)
    ax_vel.plot(len(velocities)-1, obj.velocity, 'go', markersize=15, label=f'vx: {obj.velocity:.2f}')
    ax_vel.set_title('X Velocity'); ax_vel.grid(True)
    ax_vel.legend()

ani = FuncAnimation(fig, update, frames=400, interval=50, blit=False)
plt.tight_layout()
plt.show()
