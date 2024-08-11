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


def voxel_data(origin, size):
    
    X = np.array([
        [[0., 1., 0.], [0., 0., 0.], [1., 0., 0.], [1., 1., 0.]],
        [[0., 0., 0.], [0., 0., 1.], [1., 0., 1.], [1., 0., 0.]],
        [[1., 0., 1.], [1., 0., .0], [1., 1., 0.], [1., 1., 1.]],
        [[0., 0., 1.], [0., 0., 0.], [0., 1., 0.], [0., 1., 1.]],
        [[0., 1., 0.], [0., 1., 1.], [1., 1., 1.], [1., 1., 0.]],
        [[0., 1., 1.], [0., 0., 1.], [1., 0., 1.], [1., 1., 1.]]
    ])
    
    return size*(X + origin)


def plot_voxel(positions, size, **kwargs):

    g = [voxel_data(p, size) for p in positions]
    g = np.concatenate(g)
    
    return Poly3DCollection(g, **kwargs)
