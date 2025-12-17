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
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.gravity = gravity
        self.angular_velocity = angular_velocity
        self.angular_acceleration = angular_acceleration
        self.net_force = net_force
        self.net_torque = net_torque  # Scalar for 2D rotation around z-axis
    
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




