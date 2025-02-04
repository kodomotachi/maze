# disjoint_set.py

class DisjointSet:
    """
    A Disjoint Set (also called Union-Find) data structure implementation.
    
    This structure efficiently supports union and find operations, which are
    fundamental for handling dynamic connectivity in various applications such as
    network connectivity, image processing, and Kruskal's algorithm for finding
    the Minimum Spanning Tree.
    """
    # create array of parent of each cell and rank to merge 
    def __init__(self, n):
        """
        Initialize the disjoint set with `n` elements.
        Each element is initially its own parent, and the rank is set to 0.

        Parameters:
        n (int): The number of elements in the disjoint set.
        """
        self.parent = list(range(n))
        self.rank = [0] * n

    # find parent of each cell to merging
    def find(self, x):
        """
        Find the root of the set containing element `x`.

        This method uses path compression to optimize the structure of the set,
        which helps reduce the time complexity of future operations.

        Parameters:
        x (int): The element whose set representative is sought.

        Returns:
        int: The root of the set containing `x`.
        """
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression 
        return self.parent[x]

    # combine 2 sets together
    def union(self, x, y):
        """
        Merge the sets containing elements `x` and `y`.
        Uses rank to keep the tree balanced.

        Parameters:
        x (int): An element in the first set.
        y (int): An element in the second set.
        """
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
