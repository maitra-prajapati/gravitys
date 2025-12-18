import numpy as np

class PhysicsObject:
    def __init__(self, mass=1.0, position=np.array([0.0, 0.0]), 
                 velocity=np.array([0.0, 0.0]),
                 acceleration=np.array([0.0, 0.0]),
                 gravity=np.array([0.0, -9.81]), 
                 angular_velocity=0.0, 
                 angular_acceleration=0.0, 
                 net_force=np.array([0.0, 0.0]), 
                 net_torque=0.0):
        self.mass = mass
        self.position = np.array(position if position is not None else [0.0, 0.0], dtype = float)
        self.velocity = np.array(velocity if velocity is not None else [0.0, 0.0], dtype = float)
        self.acceleration = np.array(acceleration if acceleration is not None else [0.0, 0.0], dtype = float)
        self.gravity = gravity
        self.angular_velocity = np.array(angular_velocity if angular_velocity is not None else [0.0, 0.0], dtype = float)
        self.angular_acceleration =np.array(angular_acceleration if angular_acceleration is not None else [0.0, 0.0], dtype = float)
        self.net_force = np.array(net_force if net_force is not None else [0.0, 0.0], dtype = float)
        self.net_torque =np.array(net_torque if net_torque is not None else [0.0, 0.0], dtype = float) # Scalar for 2D rotation around z-axis
    
    def update_linear(self, dt):
        """Euler integration: v += a*dt, x += v*dt"""
        self.acceleration = (self.net_force + self.mass * self.gravity) / self.mass
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
    
    def update_angular(self, dt, moment_of_inertia=1.0):
        """omega += alpha*dt; alpha = torque / I"""
        self.angular_acceleration = self.net_torque / moment_of_inertia
        self.angular_velocity += self.angular_acceleration * dt
    
    def reset_forces(self):
        self.net_force = np.zeros(2)
        self.net_torque = 0.0
    
    def apply_force(self, force, point=np.array([0.0, 0.0]), r=np.array([0.0, 0.0])):
        """Apply force at relative point for torque: tau = r x F (2D: rx*Fy - ry*Fx)"""
        self.net_force += force
        self.net_torque += r[0] * force[1] - r[1] * force[0]




