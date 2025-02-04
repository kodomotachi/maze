# kruskal_maze.py

import random
from disjoint_set import DisjointSet

# Movement directions: right and down
# These arrays help navigate through the grid.
dx = [1, 0]
dy = [0, 1]

class KruskalMaze:
    def __init__(self, rows, cols):
        """
        Initialize the maze generator with given dimensions.

        Parameters:
        rows (int): Number of rows in the maze.
        cols (int): Number of columns in the maze.
        """
        self.rows = rows
        self.cols = cols
        self.grid_size = rows * cols  # Total number of nodes in the grid.
        self.edges = []  # List to store edges between grid nodes.
        self.check_mst_edge = {}  # To keep track of edges in the MST.
        self.check_grid = {}  # To represent the maze structure.
        
        # Create edges for all possible right and down connections in the grid.
        for r in range(rows):
            for c in range(cols):
                node = r * cols + c  # Linear index for the grid cell.
                # Create an edge to the right neighbor if within bounds.
                if c < cols - 1:
                    right_node = node + 1
                    self.edges.append((random.random(), node, right_node))
                # Create an edge to the down neighbor if within bounds.
                if r < rows - 1:
                    down_node = node + cols
                    self.edges.append((random.random(), node, down_node))

    def generate_maze(self):
        """
        Generate the maze using Kruskal's algorithm.

        Returns:
        list: Minimum Spanning Tree (MST) representing the maze structure.
        """
        # Sort edges by weight (random priority for randomness in maze generation).
        self.edges.sort()
        ds = DisjointSet(self.grid_size)  # Initialize disjoint set for nodes.
        mst = []  # List to store edges in the MST.

        # Iterate through edges, adding them to the MST if they connect disjoint sets.
        for weight, u, v in self.edges:
            if ds.find(u) != ds.find(v):  # Check if nodes belong to different sets.
                ds.union(u, v)  # Merge the sets.
                mst.append((u, v))

        return mst

    def visualize_maze(self, mst):
        """
        Visualize the maze based on the given Minimum Spanning Tree (MST).

        Parameters:
        mst (list): List of edges representing the maze structure.

        Returns:
        tuple: Two dictionaries representing the maze structure and MST edges.
        """
        # Initialize all edges as walls.
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(2):  # For right and down directions.
                    new_x = i + dx[k]
                    new_y = j + dy[k]
                    if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                        self.check_mst_edge[(i, j, new_x, new_y)] = False

        # Mark the edges in the MST as pathways.
        for u, v in mst:
            r1, c1 = divmod(u, self.cols)  # Convert linear index to 2D coordinates.
            r2, c2 = divmod(v, self.cols)
            self.check_mst_edge[(r1, c1, r2, c2)] = True

        # Initialize the maze grid structure.
        for i in range(self.rows + 1):
            for j in range(self.cols + 1):
                for k in range(2):
                    new_x = i + dx[k]
                    new_y = j + dy[k]

                    # Mark valid grid positions as walls initially.
                    if 0 <= new_x <= self.rows and 0 <= new_y <= self.cols:
                        self.check_grid[(i, j, new_x, new_y)] = True

        # Remove walls based on MST pathways.
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(2):
                    new_x = i + dx[k]
                    new_y = j + dy[k]

                    if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                        if self.check_mst_edge.get((i, j, new_x, new_y), False):
                            if k == 0:  # Right direction
                                self.check_grid[(i + 1, j, new_x, new_y + 1)] = False
                            else:  # Down direction
                                self.check_grid[(i, j + 1, new_x + 1, new_y)] = False

        return self.check_grid, self.check_mst_edge
