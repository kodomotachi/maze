# disjoint_set.py

class DisjointSet:
    # create array of parent of each cell and rank to merge 
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    # find parent of each cell to merging
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression 
        return self.parent[x]

    # combine 2 sets together
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            if self.rank[root_x] > self.rank[root_y]:
                self.parent[root_y] = root_x
            elif self.rank[root_x] < self.rank[root_y]:
                self.parent[root_x] = root_y
            else:
                self.parent[root_y] = root_x
                self.rank[root_x] += 1
