class DirectedGraph:
    def __init__(self):
        self.graph = {}

    def addVertex(self, vertex):
        """Adds a new vertex to the graph if it doesn't already exist."""
        if vertex not in self.graph:
            self.graph[vertex] = []
            print(f"Vertex '{vertex}' added.")
        else:
            print(f"Vertex '{vertex}' already exists.")

    def addEdge(self, from_vertex, to_vertex):
        """Adds a directed edge from one vertex to another."""
        if from_vertex not in self.graph:
            print(f"Vertex '{from_vertex}' does not exist. Adding it now.")
            self.addVertex(from_vertex)
        if to_vertex not in self.graph:
            print(f"\nVertex '{to_vertex}' does not exist. Adding it now.\n")
            self.addVertex(to_vertex)

        self.graph[from_vertex].append(to_vertex)
        print(f"Edge added: {from_vertex} ➝ {to_vertex}")

    def listOutgoingAdjacentVertex(self, vertex):
        """Lists all vertices that have outgoing edges from the given vertex."""
        if vertex not in self.graph:
            print(f"\nVertex '{vertex}' does not exist in the graph.")
            return

        outgoing = self.graph[vertex]
        if outgoing:
            print(f"\nOutgoing vertices from '{vertex}': {', '.join(outgoing)}")
        else:
            print(f"\nNo outgoing edges from vertex '{vertex}'.")

if __name__ == "__main__":
    g = DirectedGraph()

    g.addVertex("A")
    g.addVertex("B")
    g.addVertex("D")
    g.addEdge("A", "B")
    g.addEdge("A", "C")
    g.addEdge("B", "C")
    g.addEdge("C", "D")

    g.listOutgoingAdjacentVertex("A")
    g.listOutgoingAdjacentVertex("B")
    g.listOutgoingAdjacentVertex("C")
    g.listOutgoingAdjacentVertex("D")
