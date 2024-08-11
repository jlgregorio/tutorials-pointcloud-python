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