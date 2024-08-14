import numpy as np


def rotation_zyx(theta_x=0., theta_y=0., theta_z=0.):

    R_x = np.array([
        [1., 0., 0.],
        [0., np.cos(theta_x), -np.sin(theta_x)],
        [0., np.sin(theta_x), np.cos(theta_x)]
    ])
    R_y = np.array([
        [np.cos(theta_y), 0., np.sin(theta_y)],
        [0., 1., 0.],
        [-np.sin(theta_y), 0., np.cos(theta_y)]
    ])
    R_z = np.array([
        [np.cos(theta_z), -np.sin(theta_z), 0.],
        [np.sin(theta_z), np.cos(theta_z), 0.],
        [0., 0., 1.]
    ])

    return R_z @ R_y @ R_x


def rotation_f_to_t(f, t):
    """Construct a (3, 3) matrix that rotates a unit vector f into another 
    unit vector t.

    From Möller, T., & Hughes, J. F. (1999). Efficiently building a matrix to 
    rotate one vector to another. Journal of graphics tools, 4(4), 1-4."""
    
    v_x, v_y, v_z = np.cross(f, t)
    c = np.dot(f, t)
    h = 1 / (1 + c)

    # When f and t are nearly parallel the computation is numerically unstable
    if np.linalg.norm(c) > 0.99:
        return np.eye(3)

    R = np.array([
    [c + h*v_x**2, h*v_x*v_y - v_z, h*v_x*v_z + v_y],
    [h*v_x*v_y + v_z, c + h*v_y**2, h*v_y*v_z - v_x],
    [h*v_x*v_z - v_y , h*v_y*v_z + v_x, c + h*v_z**2]
    ])
    
    return R