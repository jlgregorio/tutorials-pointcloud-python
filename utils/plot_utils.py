import numpy as np
import matplotlib.pyplot as plt


def cuboid_to_poly3D(origin, size):
    """Convert a rectangular cuboid to a set of 3D polygons, for Matplotlib."""
    
    # Quadrangular faces of one unit cube defined by the sequence of its vertices
    # (somehow similar to STL format but with quad faces instead of triangles)
    vertices = np.array([
        [[0., 1., 0.], [0., 0., 0.], [1., 0., 0.], [1., 1., 0.]], # bottom face
        [[0., 0., 0.], [0., 0., 1.], [1., 0., 1.], [1., 0., 0.]], # left face
        [[1., 0., 1.], [1., 0., .0], [1., 1., 0.], [1., 1., 1.]], # front face
        [[0., 0., 1.], [0., 0., 0.], [0., 1., 0.], [0., 1., 1.]], # back face
        [[0., 1., 0.], [0., 1., 1.], [1., 1., 1.], [1., 1., 0.]], # right face
        [[0., 1., 1.], [0., 0., 1.], [1., 0., 1.], [1., 1., 1.]] # top face
    ])
    
    return size*vertices + origin
