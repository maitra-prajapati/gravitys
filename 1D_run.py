import numpy as np
import matplotlib.pyplot as plt
from 1D import PhysicsObject1D
m = float(input("Enter mass of object (kg): "))
x_start = float(input("Enter initial height (m): "))
force = float(input("enter a constant force value(Newton): "))
time = float(input("Enter time for which force is applied(sec): "))
total_time= float(input("Enter time for which Simulation is to run(sec): "))

# --- Simulation Setup ---
obj = PhysicsObject1D(mass=m, initial_x=x_start)
dt = time/10**3          # Time step (10 milliseconds)
  # Total simulation seconds
time_history = []
horizontal_history = []
obj.apply_force(force)
# --- Simulation Loop ---
for t in np.arange(0, total_time, dt):
    time_history.append(t)
    height_history.append(obj.y)

    if(t>=time) obj.reset_forces
    obj.update(dt)

# --- Visualization ---
plt.plot(time_history, height_history)
plt.title("1D Falling Object (Gravity Only)")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.show()
