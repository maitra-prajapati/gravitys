import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from D1 import PhysicsObject1D  # Import the 1D physics class

# User inputs for initial conditions
mass = float(input("Enter mass of the object: "))
type = input("Enter a for constant force, b for harmonic motion")
if type == 'b':
    k = float(input("Enter spring constant: "))
    
    A = float(input("Enter amplitude of motion: "))
    init_pos = 0.0
    force = lambda obj: -k * obj.position
    init_vel = (k / mass) ** 0.5 * A
else:
    constant_force = float(input("Enter constant force value: "))
    force = lambda obj: constant_force  # Constant force
    init_pos = float(input("Enter initial position of the object: "))
    init_vel = float(input("Enter initial velocity of the object: "))

dt = 0.01 # Time step for the simulation

# Initialize the 1D physics object
obj = PhysicsObject1D(mass, init_pos, init_vel)  

# Setup a single plot for the x-axis
fig, ax = plt.subplots(figsize=(10, 2))
if type == 'a':
    def update(frame):
    # Physics update loop
        obj.reset_forces()
        obj.apply_force(force)
        obj.update_linear(dt)
    
        ax.clear()
    
    # 1. Plot the object as a point on the x-axis (y is constant at 0)
        ax.plot(obj.position, 0, 'ro', markersize=15, label=f'x: {obj.position:.2f} m')
    
    # 2. Draw a horizontal line to represent the axis
        ax.axhline(0, color='black', linewidth=1)
    
    # 3. Configure the axis view
    # Centering the view around the object with a +/- 10 unit window
        ax.set_xlim(obj.position - 10, obj.position + 10)
        ax.set_ylim(-1, 1)
    
    # 4. Styling the plot
        ax.get_yaxis().set_visible(False)  # Hide the y-axis as it's 1D
        ax.set_xlabel('Position (m)')
        ax.set_title('1D Point Object Motion')
        ax.grid(False)
        ax.legend(loc='upper right')
else:
    def update(frame):
        # Physics update loop
        obj.reset_forces()
        obj.apply_force(force)
        obj.update_linear(dt)
    
        ax.clear()
    
        # 1. Plot the object as a point on the x-axis (y is constant at 0)
        ax.plot(obj.position, 0, 'bo', markersize=15, label=f'x: {obj.position:.2f} m')
    
        # 2. Draw a horizontal line to represent the axis
        ax.axhline(0, color='black', linewidth=1)
    
        # 3. Configure the axis view
        # Centering the view around the object with a +/- 10 unit window
        ax.set_xlim(obj.position - 4, obj.position + 4)
        ax.set_ylim(-1, 1)
    
        # 4. Styling the plot
        ax.get_yaxis().set_visible(False)  # Hide the y-axis as it's 1D
        ax.set_xlabel('Position (m)')
        ax.set_title('1D Harmonic Motion')
        ax.grid(False)
        ax.legend(loc='upper right')


# Create the animation
ani = FuncAnimation(fig, update, frames=400, interval=0.5, blit=False)
plt.tight_layout()
plt.show()

