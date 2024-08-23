import numpy as np

def cartesian_to_spherical(u):
    """Cartesian to spherical coordinates (only theta and phi)"""

    x, y, z = u
    
    theta = np.arccos(z/np.sqrt(x**2 + y**2 + z**2))
    
    if np.isclose(x, 0.0) and np.isclose(y, 0.0):
        phi = 0.0
    else:
        phi = np.sign(y) * np.arccos(x / np.sqrt(x**2 + y**2))

    return theta, phi

def spherical_to_cartesian(u):
    """Spherical to cartesian coordinates (unit vector)"""
    
    theta, phi = u

    return np.array([np.cos(phi)*np.sin(theta),
                     np.sin(phi)*np.sin(theta),
                     np.cos(theta)])