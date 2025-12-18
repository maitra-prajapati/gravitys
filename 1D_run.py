import numpy as np
import matplotlib.pyplot as plt

m = float(input("Enter mass of object (kg): "))
y_start = float(input("Enter initial height (m): "))

# --- Simulation Setup ---
obj = PhysicsObject1D(mass=m, initial_y=y_start)
dt = 0.01          # Time step (10 milliseconds)
total_time = 2.0   # Total simulation seconds
time_history = []
height_history = []

# --- Simulation Loop ---
for t in np.arange(0, total_time, dt):
    time_history.append(t)
    height_history.append(obj.y)
    
    obj.update(dt)
    
    # Optional: Stop if the object hits the ground
    if obj.y <= 0:
        break

# --- Visualization ---
plt.plot(time_history, height_history)
plt.title("1D Falling Object (Gravity Only)")
plt.xlabel("Time (s)")
plt.ylabel("Height (m)")
plt.grid(True)
plt.show()
