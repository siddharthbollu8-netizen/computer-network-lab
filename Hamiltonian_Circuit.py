# Hamiltonian Circuit using Backtracking
# Ellis Horowitz Algorithm.

class Hamiltonian:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        # x array tracks selected vertices using 1-based indexing
        self.x = [0] * self.n

    def next_vertex(self, k):
        while True:
            # Get next higher vertex value (modulo n+1 for 1-based vertices)
            self.x[k] = (self.x[k] + 1) % (self.n + 1)
            
            # If we cycled back to 0, no valid vertex remains at this step
            if self.x[k] == 0:
                return

            # Check if there is an edge between previous vertex and current vertex
            if self.graph[self.x[k - 1] - 1][self.x[k] - 1] != 0:
                
                # Check if this vertex has already been visited in the current path
                j = 0
                while j < k:
                    if self.x[j] == self.x[k]:
                        break
                    j += 1
                
                # If unique, check the final loop closing condition
                if j == k:
                    # If it's an intermediate step OR the last step that completes the loop back to start
                    if (k < self.n - 1) or \
                       (k == self.n - 1 and self.graph[self.x[k] - 1][self.x[0] - 1] != 0):
                        return

    def hamiltonian(self, k):
        while True:
            # Assign a valid next vertex for position k
            self.next_vertex(k)
            
            # If no vertex could be assigned, back up a step
            if self.x[k] == 0:
                return
            
            # If a full circuit is found, print it out
            if k == self.n - 1:
                print("Hamiltonian Circuit:", end=" ")
                for v in self.x:
                    print(v, end=" ")
                print(self.x[0]) # Print start vertex to show full closure
            else:
                # Recursively attempt to find a vertex for the next slot
                self.hamiltonian(k + 1)

    def solve(self):
        self.x[0] = 1 # Anchor the path starting at vertex 1
        self.hamiltonian(1)

# Example Graph (Adjacency Matrix)
graph = [
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0],
    [1, 1, 0, 1, 1],
    [0, 1, 1, 0, 1],
    [1, 0, 1, 1, 0]
]

h = Hamiltonian(graph)
h.solve()