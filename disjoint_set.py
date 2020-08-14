class DisjointSet:
    """Disjoint set implementation"""

    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, index):
        if index != self.parent[index]:
            self.parent[index] = self.find(self.parent[index])
        return self.parent[index]

    def union(self, index1, index2):
        parent1 = self.find(index1)
        parent2 = self.find(index2)
        if self.rank[parent1] < self.rank[parent2]:
            self.parent[parent1] = parent2
        else:
            self.parent[parent2] = parent1
            if self.rank[parent2] == self.rank[parent1]:
                self.rank[parent1] += 1
