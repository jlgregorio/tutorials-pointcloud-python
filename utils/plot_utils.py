import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def cells_to_rect(cells, size, color="gray"):

    rectangles = []

    for key in cells.keys():

        anchor_point = [size * d for d in key]
        
        rectangles.append(Rectangle(anchor_point, size, size, color=color, fill=False, lw=1))
    
    return rectangles


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


def voxel_data(origin, size):
    
    
    X = np.array([
        [[0., 1., 0.], [0., 0., 0.], [1., 0., 0.], [1., 1., 0.]], # bottom face
        [[0., 0., 0.], [0., 0., 1.], [1., 0., 1.], [1., 0., 0.]], # left face
        [[1., 0., 1.], [1., 0., .0], [1., 1., 0.], [1., 1., 1.]], # front face
        [[0., 0., 1.], [0., 0., 0.], [0., 1., 0.], [0., 1., 1.]], # back face
        [[0., 1., 0.], [0., 1., 1.], [1., 1., 1.], [1., 1., 0.]], # right face
        [[0., 1., 1.], [0., 0., 1.], [1., 0., 1.], [1., 1., 1.]] # top face
    ])
    
    return size*(X + origin)


def plot_voxel(positions, size, **kwargs):

    g = [voxel_data(p, size) for p in positions]
    g = np.concatenate(g)
    
    return Poly3DCollection(g, **kwargs)
