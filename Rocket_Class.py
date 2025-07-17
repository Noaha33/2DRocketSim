import numpy as np

# Class Rocket
class Rocket:
    def __init__(self, mass, drag_coeff, max_thrust, area, angle, position=None, velocity=None, max_accel=None, max_velocity=None,):
        
        """
        Initialize Rocket with physical parameters and initial state.

        Parameters:
            mass: Mass in kg.
            max_thrust: Max thrust force in newtons.
            drag_coeff: Drag coefficient (dimensionless).
            area: Reference area (m²) for drag.
            position: Initial position vector (default [0,0]).
            velocity: Initial velocity vector (default [0,0]).
            angle: Initial heading angle in radians (default 0).
            gravity: Gravity acceleration (default Earth g).
        """
        
        self.mass = mass
        self.max_accel = max_accel
        self.max_velocity = max_velocity
        self.drag_coeff = drag_coeff
        self.max_thrust = max_thrust
        self.area = area
        self.angle = angle

        self.position = position if position is not None else np.array([0.0, 0.0])
        self.velocity = velocity if velocity is not None else np.array([0.0, 0.0])