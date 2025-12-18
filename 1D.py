import numpy as np

class PhysicsObject1D:
  def __init__(self, mass=1.0, position=np.array([0.0, 0.0]), 
                 velocity=np.array([0.0, 0.0]),
                 acceleration=np.array([0.0, 0.0])):
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
                   
   def _linear_mov(self,dt):
     """Euler integration: v += a*dt, x += v*dt"""
        self.acceleration = (self.net_force + self.mass * self.gravity) / self.mass
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt

   def reset_forces(self):
        self.net_force = np.zeros(2)

   def apply_force(self,force)
"""Apply force at a point"""
       self.net_force += force
