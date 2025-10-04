# Tutorials for pointcloud processing in Python

<div align="center">
  <p><img src="images/example_pointcloud.png"></p>
</div>

The use of pointclouds tends to increase over the years, as 3D acquisition systems and 3D modeling software become more widely available. Pointclouds are nowadays used in many areas, such as computer-aided design, metrology, extended reality, robotics, and autonomous driving, to name just a few.

These tutorials are for those wishing to learn a little bit more about the basics of pointcloud processing. Having gone through this stage during my Ph.D., I hope here to share some of what I have learned so far.

The notebooks are designed to make pointcloud processing algorithms easier to understand, without compromising performance too much and trying to minimize the use of specialized third-party software. They require basic knowledge of Python and its main scientific libraries.

## Content

Tutorials are broken down as follows:

1. Basic operations: pointcloud attributes, transformations (translations, rotations, reflections, scaling) & subsampling.
2. Spatial indexing: voxel grids, octrees & kd-trees.
3. Registration: corresponding sets & non-corresponding sets (Iterative Closest Point & Principal Axis Alignment).
4. Segmentation: Region Growing, Hough Transform & RANSAC.
5. Primitive fitting: plane, sphere, cylinder, cone & torus.
6. Normals and descriptors: normals estimation/orientation and other local descriptors.

## Dependencies

The code is in `python` and relies on `numpy`, `scipy`, `matplotlib`, and `jupyterlab`.

These dependencies may installed with `pip` with

    pip install numpy scipy matplotlib jupyterlab

or via `conda` with

    conda install numpy scipy matplotlib jupyterlab

JupyterLab may be started using the terminal or Anaconda prompt simply by typing

    jupyter lab

## Going further

The lists below do not pretend to be not exhaustive but may be a good starting point for those who whish to dive deeper in the topic of pointcloud processing with Python.

### Software

Libraries:

- **CGAL**, an open-source library for efficient and reliable geometric algorithms (in C++, with Python bidings)
- **CloudComPy**, a Python wrapper for CloudCompare (see below)
- **Open3D**, an open-source library for 3D data processing (in C++ and Python, with a 3D viewer app)
- **PCL**, a standalone, large scale, open project for 2D/3D image and pointcloud processing (in C++, with Python bidings)
- **PDAL**, an open-source library for translating and manipulating pointcloud data (in C++, with Python support)
- **PyMeshLab**, a Python library that interfaces to MeshLab (see below)
- **PyVista**, a library providing a pythonic interface to VTK (see below)
- **VTK**, an open-source software for manipulating and displaying scientific data (in C++, with wrappers in Python, Java and Tcl)

Applications:

- **Blender**, an open-source  3D computer graphics software that may be used to visualize and process pointclouds (with Python scripting capabilities)
- **CloudCompare**, an open-source 3D pointcloud (and triangular mesh) processing software (with Python scripting capabilities through **CloudComPy**)
- **MeshLab**, an open-source 3D triangular meshes (and pointclouds) processing and editing software (with Python scripting capabilities through **PyMeshLab**)
- **ParaView**, an open-source visualization application (with Python scripting capabilities)

### Resources 

Books:
- Poux, F. (2025). *3D Data Science with Python*. O'Reilly Media.
- Liu, S., Zhang, M., Kadam, P., & Kuo, C. C. J. (2021). *3D Point Cloud Analysis: Traditional, Deep Learning, and Explainable Machine Learning Methods*. Springer.
- Vosselman, G., & Maas, H. G. (2010). *Airborne and terrestrial laser scanning*. Whittles Publishing.
- Samet, H. (2006). *Foundations of multidimensional and metric data structures*. Morgan Kaufmann.
- Schneider, P., & Eberly, D. H. (2002). *Geometric tools for computer graphics*. Elsevier.
- Goulette, F. (1999). *Modélisation 3D automatique : outils de géométrie différentielle*. Presses des Mines.

Videos:
- Florent Poux YouTube channel: www.youtube.com/@FlorentPoux (last accessed in June 2025)
- CloudCompare playlist on Daniel Girardeau-Montaut YouTube channel www.youtube.com/@danielgirardeau-montaut9044 (last accessed in June 2025)

## Citation

You are mostly free to share and reuse this work as you wish. Please do not forget to cite it if you do!

An example using BibTeX:

    @unpublished{gregorio2024tutorials,
         author={Grégorio, Jean-Loup},
         title={Tutorials for pointcloud processing in Python},
         year={2024},
    }
