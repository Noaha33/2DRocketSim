import numpy as np


def air_density(self):
    """Returns air density (kg/m^3) at altitude h (m), using ISA approximation (up to 11 km)."""
    T0 = 288.15        # sea level standard temperature, K
    P0 = 101325        # sea level standard pressure, Pa
    L = 0.0065         # temperature lapse rate, K/m
    R = 287.05         # specific gas constant for dry air, J/(kg·K)
    g = 9.80665        # gravity, m/s^2

    h = self.position[1]

    T = T0 - L * h
    P = P0 * (T / T0) ** (g / (R * L))
    rho = P / (R * T)
    return rho

def compute_drag_force(self, rho):
    """
    Computes drag force assuming sea level density
    F_drag = 0.5 * rho * v^2 * Cd * A
    rho = 1.225 kg/m^3
    """
    speed = np.linalg.norm(self.velocity)
    if speed == 0:
        return np.zeros(1)
    
    direction = -self.velocity / speed  
    drag_magnitude = 0.5 * rho * speed**2 * self.drag_coeff * self.area
    drag_force = drag_magnitude * direction

    return drag_force