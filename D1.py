

class PhysicsObject:
    def __init__(self, mass=1.0, position=0,
                 velocity=0,
                 acceleration=0,
                 net_force=0): 
                
        self.mass = mass
        self.position = position
        self.velocity = velocity
        self.acceleration = acceleration
        self.net_force = net_force
    
    def update_linear(self, dt):
        """Euler integration: v += a*dt, x += v*dt"""
        self.acceleration = (self.net_force) / self.mass
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
    
    def reset_forces(self):
        self.net_force = 0
    
    def apply_force(self, force):
        self.net_force += force
        




