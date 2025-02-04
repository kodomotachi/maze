# kruskal_maze.py

import random
from disjoint_set import DisjointSet

# Movement directions
dx = [1, 0]
dy = [0, 1]

class KruskalMaze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid_size = rows * cols
        self.edges = []
        self.check_mst_edge = {}
        self.check_grid = {}
        
        for r in range(rows):
            for c in range(cols):
                node = r * cols + c
                if c < cols - 1:
                    right_node = node + 1
                    self.edges.append((random.random(), node, right_node))
                if r < rows - 1:
                    down_node = node + cols
                    self.edges.append((random.random(), node, down_node))

    def generate_maze(self):
        self.edges.sort()
        ds = DisjointSet(self.grid_size)
        mst = []

        for weight, u, v in self.edges:
            if ds.find(u) != ds.find(v):
                ds.union(u, v)
                mst.append((u, v))

        return mst

    def visualize_maze(self, mst):
        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(2):
                    new_x = i + dx[k]
                    new_y = j + dy[k]
                    if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                        self.check_mst_edge[(i, j, new_x, new_y)] = False

        for u, v in mst:
            r1, c1 = divmod(u, self.cols)
            r2, c2 = divmod(v, self.cols)
            self.check_mst_edge[(r1, c1, r2, c2)] = True

        for i in range(self.rows + 1):
            for j in range(self.cols + 1):
                for k in range(2):
                    new_x = i + dx[k]
                    new_y = j + dy[k]

                    if 0 <= new_x <= self.rows and 0 <= new_y <= self.cols:
                        self.check_grid[(i, j, new_x, new_y)] = True

        for i in range(self.rows):
            for j in range(self.cols):
                for k in range(2):
                    new_x = i + dx[k]
                    new_y = j + dy[k]

                    if 0 <= new_x < self.rows and 0 <= new_y < self.cols:
                        if self.check_mst_edge.get((i, j, new_x, new_y), False):
                            if k == 0:
                                self.check_grid[(i + 1, j, new_x, new_y + 1)] = False
                            else:
                                self.check_grid[(i, j + 1, new_x + 1, new_y)] = False

        return self.check_grid, self.check_mst_edge
