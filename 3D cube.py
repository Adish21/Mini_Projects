import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

# Parameters
frames = 60  # Number of frames
size = 100   # Cube size
colors = np.linspace(0, 1, frames)  # Color gradient from light to dark

# Generate figure and axis
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define cube vertices
vertices = [
    [-size, -size, -size],
    [size, -size, -size],
    [size, size, -size],
    [-size, size, -size],
    [-size, -size, size],
    [size, -size, size],
    [size, size, size],
    [-size, size, size]
]

# Define edges linking vertices
edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],
    [4, 5], [5, 6], [6, 7], [7, 4],
    [0, 4], [1, 5], [2, 6], [3, 7]
]

def animate(i):
    ax.clear()
    ax.set_xlim(-size, size)
    ax.set_ylim(-size, size)
    ax.set_zlim(-size, size)
    ax.grid(False)
    ax.set_axis_off()

    # Rotate cube
    angle = i * (360 / frames)
    rot_matrix = np.array([
        [np.cos(np.radians(angle)), -np.sin(np.radians(angle)), 0],
        [np.sin(np.radians(angle)), np.cos(np.radians(angle)), 0],
        [0, 0, 1]
    ])

    rotated_vertices = np.dot(vertices, rot_matrix)

    for edge in edges:
        ax.plot3D(rotated_vertices[edge, 0], rotated_vertices[edge, 1], rotated_vertices[edge, 2], 'gray')

    # Set cube color
    cube_color = plt.cm.binary(colors[i])  # Dark gradient color
    ax.add_collection3d(plt.Poly3DCollection([rotated_vertices], facecolors=[cube_color], edgecolors='black', linewidths=1))

ani = FuncAnimation(fig, animate, frames=frames, interval=50)
plt.show()
