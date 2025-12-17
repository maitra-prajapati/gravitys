import math

class Rectangle:
    def __init__(self, length, width, vertex_x, vertex_y, angle_deg=0):
        self.length = length
        self.width = width
        self.vertex_x = vertex_x
        self.vertex_y = vertex_y
        self.angle_deg = angle_deg  # angle in degrees from horizontal
        #vertex is bottom left
        #length is bottom one
        #width is what's left
    
        angle_hor = math.radians(angle_deg)
        half_diag = (math.sqrt(length**2 + width**2))/2
        self.center_x = half_diag*math.cos(angle_hor) + vertex_x
        self.center_y = half_diag*math.sin(angle_hor) + vertex_y
        
#rectangle is finished

    

class Circle:
    def __init__(self, radius, center_x, center_y):
        self.radius = radius
        self.center = (center_x, center_y)

#circle is complete