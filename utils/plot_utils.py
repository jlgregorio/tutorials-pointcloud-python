import os

import numpy as np

from manip_utils import rotation_f_to_t
from file_utils import load_off


# Directory where the primitive surface templates are stored
PDIR = os.path.join(os.path.dirname(__file__), "primitive_surface_templates")


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


def generate_plane_mesh(center, normal, tangent, length, width):
    """Mesh of a rectangle in 3D space."""

    # Start with a "unit" plane, with parameters:
    # c = (0., 0., 0.), n = (0., 0., 1.), t = (1., 0., 0.), l = 1., w = 1.
    plane_vertices, plane_faces = load_off(os.path.join(PDIR, "plane.off"))
    # Adjust dimensions
    plane_vertices[:, 0] *= length
    plane_vertices[:, 1] *= width
    # Adjust orientation
    R = np.stack((tangent, np.cross(normal, tangent), normal), axis=1)
    plane_vertices = (R @ plane_vertices.T).T
    # Adjust position
    plane_vertices += center

    return plane_vertices, plane_faces


def generate_sphere_mesh(center, radius):
    """Mesh of a sphere in 3D space."""

    # Start with a "unit" sphere, with parameters:
    # c = (0., 0., 0.), r = 1.
    sphere_vertices, sphere_faces = load_off(os.path.join(PDIR, "sphere.off"))
    # Adjust dimensions
    sphere_vertices *= radius
    # Adjust position
    sphere_vertices += center

    return sphere_vertices, sphere_faces


def generate_cylinder_mesh(center, normal, radius, length):
    """Mesh of a cylinder in 3D space."""

    # Start with a "unit" cylinder, with parameters:
    # c = (0., 0., 0.), n = (0., 0., 1.), r = 1., l = 1.
    cylinder_vertices, cylinder_faces = load_off(os.path.join(PDIR, "cylinder.off"))
    # Adjust radius and length
    cylinder_vertices[:, :2] *= radius
    cylinder_vertices[:, 2] *= length
    # Adjust orientation
    R = rotation_f_to_t(np.array([0., 0., 1.]), normal)
    cylinder_vertices = (R @ cylinder_vertices.T).T
    # Adjust center
    cylinder_vertices += center

    return cylinder_vertices, cylinder_faces


def generate_cone_mesh(apex, normal, half_angle, length):
    """Mesh of a cone in 3D space."""

    # Start with a "unit" cone, with parameters:
    # c = (0., 0., 0.), n = (0., 0., -1.), a = pi/4 (or r = 1.), l = 1.
    cone_vertices, cone_faces = load_off(os.path.join(PDIR, "cone.off"))
    # Adjust dimensions
    cone_vertices[:, :2] *= length * np.tan(half_angle)  # base radius
    cone_vertices[:, 2] *= length  # height
    # Adjust rotation
    R = rotation_f_to_t(np.array([0., 0., 1.]), normal)
    cone_vertices = (R @ cone_vertices.T).T
    # Adjust position (apex)
    cone_vertices += apex
    
    return cone_vertices, cone_faces


def generate_torus_mesh(center, normal, major_radius, minor_radius):
    """Mesh of a torus in 3D space."""

    # Start with a "unit" torus, with parameters:
    # c = (0., 0., 0.), n = (0., 0., 1.), R = 1., r = 0.5
    torus_vertices, torus_faces = load_off(os.path.join(PDIR, "torus.off"))
    # Current vertices parameters
    # Distances from center in xy plane
    distance_from_center = np.linalg.norm(torus_vertices[:, :2], axis=1)
    # Angles in xy plane (major radius)
    theta = np.arctan2(torus_vertices[:, 1], torus_vertices[:, 0])
    # Angle in cross-section (minor radius)
    phi = np.arctan2(torus_vertices[:, 2], distance_from_center - 1.) # R = 1.
    # New torus
    # Adjust dimensions
    new_distance_from_center = major_radius + minor_radius * np.cos(phi)
    new_x = new_distance_from_center * np.cos(theta)
    new_y = new_distance_from_center * np.sin(theta)
    new_z = minor_radius * np.sin(phi)
    torus_vertices = np.stack((new_x, new_y, new_z), axis=1)
    # Adjust orientation
    R = rotation_f_to_t(np.array([0., 0., 1.]), normal)
    torus_vertices = (R @ torus_vertices.T).T
    # Adjust position
    torus_vertices += center

    return torus_vertices, torus_faces
