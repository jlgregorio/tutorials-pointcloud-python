import numpy as np


def load_off(filename):
    """A basic reader for simple OFF files."""

    vertices, faces = [], []

    with open(filename, 'r', encoding="utf-8") as file:

        # First usually contains the letters "OFF"
        first_line = file.readline().strip()
        if not first_line.startswith("OFF"):
            raise ValueError(f"File {filename} is probably not a valid OFF file.")
        
        # Second line contains the number of vertices, faces, and edges (optional)
        second_line = file.readline().strip()
        numbers = list(map(int, second_line.split()))
        n_v = numbers[0]
        n_f = numbers[1]
        
        # Following n_v lines contain the list of vertices (x, y, z coordinates)
        for _ in range(n_v):
            line = file.readline()
            values = list(map(float, line.strip().split()))
            vertices.append(values[:3])

        # Following n_f lines contain the list of faces (index of vertices)
        for _ in range(n_f):
            line = file.readline()
            values = list(map(int, line.strip().split()))
            n = values.pop(0)
            if n!=3: # not a triangle
                raise ValueError(f"File {filename} contains a non-triangle face.")
            faces.append(values[:3])

    return np.array(vertices), np.array(faces)
