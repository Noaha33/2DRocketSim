# Create Rocket
from Rocket_Class import Rocket

rocket = Rocket(mass=1000, 
                drag_coeff = 0.08, 
                max_thrust = 15000, 
                area = 1.5, 
                angle = 45
                )

dt = 0.1
for t in range(100):
    rocket.update(thrust_command = 0.8, dt = dt)