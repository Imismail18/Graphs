"""
Structure of comments:
Function description.
Time complexity O()
"""

class Graph:
    # Initialize a graph.
    # Time complexity O(1)
    def __init__(self, directed=False):
        self.directed = directed
        self.adj_list = dict()

    def __len__(self):
        return len(self.adj_list)

    def __repr__(self):
        graph_str = ""
        for node, neghbors in self.adj_list.items(): graph_str = f"{node} -> {neghbors}\n"
        return graph_str

    # Check if a node exists in the graph.
    # Time complexity O(1)
    def __contains__(self, item):
        return item in self.adj_list

    # Add a node to the graph.
    # Time complexity O(1)
    def add_node(self, node):
        if node not in self.adj_list: self.adj_list[node] = set()
        else: raise  ValueError("Node exists already!")

    # Remove a node and all its edges from the graph.
    # Time complexity O(V + E)
    def remove_node(self, node):
        if node not in self.adj_list: raise ValueError("Node does not exist!")

        for nighbors in self.adj_list.values(): nighbors.discard(node)
        del self.adj_list[node]

    # Add an edge between two nodes with optional weight.
    # Time complexity O(1)
    def add_edge(self, from_node, to_node, weight=None):
        if from_node not in self.adj_list: self.add_node(from_node)

        if to_node not in self.adj_list: self.add_node(to_node)

        if weight is None: 
            self.adj_list[from_node].add(to_node)

            if not self.directed: self.adj_list[to_node].add(from_node)

        else: 
            self.adj_list[from_node].add((to_node, weight))

            if not self.directed: self.adj_list[to_node].add((from_node, weight))

    # Remove an edge between two nodes.
    # Time complexity O(1)
    def remove_edge(self, from_node, to_node):
        if from_node in self.adj_list:
            if to_node in self.adj_list[from_node]: self.adj_list[from_node].remove(to_node)
            else: raise ValueError("Edge does not exist!")
            
            if not self.directed and from_node in self.adj_list[to_node]: self.adj_list[to_node].remove(from_node) 
        else: raise ValueError("Edge does not exist!")

    # Get all neighbors of a node.
    # Time complexity O(1)
    def get_nighbors(self, node):
        return self.adj_list.get(node, set())

    # Check if a node exists in the graph.
    # Time complexity O(1)
    def has_node(self, node):
        return node in self.adj_list

    # Check if an edge exists between two nodes.
    # Time complexity O(1)
    def has_edge(self, from_node, to_node):
        if from_node in self.adj_list: return to_node in self.adj_list[from_node]
        return False

    # Return a list of all nodes in the graph.
    # Time complexity O(V)
    def get_nodes(self):
        return list(self.adj_list.keys())

    # Return a list of all edges in the graph.
    # Time complexity O(V + E)
    def get_edges(self):
        edges = []
        for from_node, neighbors in self.adj_list.items():
            edges.extend((from_node, to_node) for to_node in neighbors)
        return edges

    # Breadth-First Search traversal starting from a node.
    # Time complexity O(V + E)
    def bfs(self, start):
        visited = set()
        queue = [start]
        order = []

        while queue:
            node = queue.pop(0)
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_nighbors(node)

                for neighbor in neighbors:
                    if isinstance(neighbor, tuple): neighbor = neighbor[0]

                    if neighbor not in visited: queue.append(neighbor)
        return order


    # Depth-First Search traversal starting from a node.
    # Time complexity O(V + E)
    def dfs(self, start):
        visited = set()
        stack = [start]
        order = []

        while stack:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                order.append(node)
                neighbors = self.get_nighbors(node)

                for neighbor in sorted(neighbors, reverse=True):
                    if isinstance(neighbor, tuple): neighbor = neighbor[0]

                    if neighbor not in visited: stack.append(neighbor)
        return order

    def is_empty(self):
        return len(self.adj_list) == 0

    # Find shortest distances from start node to all other nodes using Dijkstra's algorithm.
    # Time complexity O((V + E) log V)
    def dijkstra(self, start):
        import heapq

        distances = {node: float("inf") for node in self.adj_list}

        distances[start] = 0
        heap = [(0, start)]

        while heap:
            curr_distance, curr_node = heapq.heappop(heap)
            if curr_distance > distances[curr_node]: continue

            neighbors = self.adj_list.get(curr_node, set())
            for neighbor in neighbors:
                if isinstance(neighbor, tuple): to, weight = neighbor
                else: to, weight = neighbor, 1
                # to, weight = neighbor if isinstance(neighbor, tuple) else to, weight = neighbor, 1

                distance = curr_distance + weight
                if distance < distances[to]:
                    distances[to] = distance
                    heapq.heappush(heap, (distance, to))
        return distances

    # Find the shortest path between two nodes using Dijkstra's algorithm.
    # Time complexity O((V + E) log V)
    def shortest_path(self, start, end):
        import heapq

        distances = {node: float("inf") for node in self.adj_list}
        prev = {node: None for node in self.adj_list}
        
        distances[start] = 0
        heap = [(0, start)]

        while heap:
            curr_distance, curr_node = heapq.heappop(heap)
            if curr_node == end: break

            if curr_distance > distances[curr_node]: continue

            neighbors = self.adj_list.get(curr_node, set())
            for neighbor in neighbors:
                if isinstance(neighbor, tuple): to, weight = neighbor
                else: to, weight = neighbor, 1
                #to, weight = neighbor if isinstance(neighbor, tuple) else to, weight = neighbor, 1

                distance = curr_distance + weight
                if distance < distances[to]:
                    distances[to] = distance
                    prev[to] = curr_node
                    heapq.heappush(heap, (distance, to))
        
        path = []
        node = end
        while node is not None:
            path.append(node)
            node = prev.get(node)
        path.reverse()
        if path[0] == start: return path
        return []

    # Convert adjacency list representation to adjacency matrix.
    # Time complexity O(V + E)
    def to_adj_matrix(self):
        nodes = self.get_nodes()
        index = {node: i for i, node in enumerate(nodes)}
        size = len(nodes)
        matrix = [[0 for _ in range(size)] for _ in range(size)]
        
        for from_node, neighbors in self.adj_list.items():
            for to_node in neighbors:
                if isinstance(to_node, tuple):
                    to, weight = to_node
                    matrix[index[from_node]][index[to]] = weight

                else: matrix[index[from_node]][index[to_node]] = 1
        return matrix



   

class DirectedGraph:
    # Initialize an empty directed graph.
    # Time complexity O(1)
    def __init__(self):
        self.graph = {}

    # Add a vertex to the directed graph.
    # Time complexity O(1)
    def add_vertex(self, vertex):
        if vertex not in self.graph: self.graph[vertex] = []

    # Add a directed edge from start to end vertex.
    # Time complexity O(1)
    def add_edge(self, start, end):
        self.add_vertex(start)
        self.add_vertex(end)
        self.graph[start].append(end)

    # Remove a directed edge from start to end vertex.
    # Time complexity O(n)
    def remove_edge(self, start, end):
        if start in self.graph and end in self.graph[start]: self.graph[start].remove(end)

    # Remove a vertex and all its associated edges.
    # Time complexity O(V + E)
    def remove_vertex(self, vertex):
        if vertex in self.graph: del self.graph[vertex]

        for edges in self.graph.values(): 
            if vertex in edges: edges.remove(vertex)

    # Check if a directed edge exists from start to end.
    # Time complexity O(n)
    def has_edge(self, start, end):
        return start in self.graph and end in self.graph[start]

    # Return a list of vertices that vertex points to.
    # Time complexity O(1)
    def neighbors(self, vertex):
        if vertex not in self.graph: raise ValueError("Vertex does not exist")
        return self.graph[vertex]

    # Check if the directed graph is empty.
    # Time complexity O(1)
    def is_empty(self):
        return len(self.graph) == 0

    # Return the number of vertices in the directed graph.
    # Time complexity O(1)
    def __len__(self):
        return len(self.graph)

    # Return string representation of the directed graph.
    # Time complexity O(V)
    def __repr__(self):
        return str(self.graph)





class WeightedGraph:
    # Initializes an empty weighted graph.
    def __init__(self):
        self.graph = {}

    # Adds a vertex to the graph.
    def add_vertex(self, vertex):
        if vertex not in self.graph: self.graph[vertex] = []

    # Adds a directed edge with a weight.
    def add_edge(self, start, end, weight):
        self.add_vertex(start)
        self.add_vertex(end)
        self.graph[start].append((end, weight))

    # Removes an edge.
    def remove_edge(self, start, end):
        if start in self.graph: self.graph[start] = [(vertex, weight) for vertex, weight in self.graph[start] if vertex != end]

    # Checks if an edge exists.
    def has_edge(self, start, end):
        if start not in self.graph: return False

        return any(vertex == end for vertex, _ in self.graph[start])

    # Returns all neighbors and their weights.
    def neighbors(self, vertex):
        if vertex not in self.graph: raise ValueError("Vertex does not exist")

        return self.graph[vertex]

    # Returns the number of vertices.
    def __len__(self):
        return len(self.graph)

    # Checks if the graph is empty.
    def is_empty(self):
        return len(self.graph) == 0

    # Returns a string representation.
    def __repr__(self):
        return str(self.graph)





class UndirectedGraph:
    # Initializes an empty undirected graph.
    # Time complexity: O(1)
    def __init__(self):
        self.graph = {}

    # Adds a vertex to the graph.
    # Time complexity: O(1)
    def add_vertex(self, vertex):
        if vertex not in self.graph: self.graph[vertex] = []

    # Adds an undirected edge between two vertices.
    # Time complexity: O(1) average
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # Removes an edge between two vertices.
    # Time complexity: O(n)
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]: self.graph[vertex1].remove(vertex2)

            if vertex1 in self.graph[vertex2]: self.graph[vertex2].remove(vertex1)

    # Removes a vertex and all its edges.
    # Time complexity: O(V + E)
    def remove_vertex(self, vertex):
        if vertex not in self.graph: return

        for neighbor in self.graph[vertex]: self.graph[neighbor].remove(vertex)

        del self.graph[vertex]

    # Checks if an edge exists between two vertices.
    # Time complexity: O(n)
    def has_edge(self, vertex1, vertex2):
        return (
            vertex1 in self.graph
            and vertex2 in self.graph[vertex1]
        )

    # Returns the neighbors of a vertex.
    # Time complexity: O(1)
    def neighbors(self, vertex):
        if vertex not in self.graph: raise ValueError("Vertex does not exist")

        return self.graph[vertex]

    # Returns the number of vertices.
    # Time complexity: O(1)
    def __len__(self):
        return len(self.graph)

    # Checks if the graph is empty.
    # Time complexity: O(1)
    def is_empty(self):
        return len(self.graph) == 0

    # Returns a string representation of the graph.
    # Time complexity: O(V)
    def __repr__(self):
        return str(self.graph)






class unweightedGraph:
    # Initializes an empty unweighted graph.
    # Time complexity: O(1)
    def __init__(self):
        self.graph = {}

    # Adds a vertex to the graph.
    # Time complexity: O(1) average
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Adds an undirected edge between two vertices.
    # Time complexity: O(1) average
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # Removes an edge between two vertices.
    # Time complexity: O(n)
    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)

            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    # Checks if an edge exists.
    # Time complexity: O(n)
    def has_edge(self, vertex1, vertex2):
        return (
            vertex1 in self.graph
            and vertex2 in self.graph[vertex1]
        )

    # Returns the neighbors of a vertex.
    # Time complexity: O(1)
    def neighbors(self, vertex):
        if vertex not in self.graph:
            raise ValueError("Vertex does not exist")

        return self.graph[vertex]

    # Removes a vertex and all its edges.
    # Time complexity: O(V + E)
    def remove_vertex(self, vertex):
        if vertex not in self.graph:
            return

        for neighbor in self.graph[vertex]:
            self.graph[neighbor].remove(vertex)

        del self.graph[vertex]

    # Returns the number of vertices.
    # Time complexity: O(1)
    def __len__(self):
        return len(self.graph)

    # Checks if the graph is empty.
    # Time complexity: O(1)
    def is_empty(self):
        return len(self.graph) == 0

    # Returns a string representation of the graph.
    # Time complexity: O(V)
    def __repr__(self):
        return str(self.graph)


if __name__ == "__main__":
    print("==" * 30, "\nGraph:\nBeginning:\n", "__" * 30)
    print()

    G = Graph()

    G.add_node("A")
    G.add_node("B")
    G.add_node("C")
    G.add_node("D")
    G.add_node("E")
    G.add_node("F")
    G.add_node("G")
    G.add_node("H")
    G.add_node("I")

    G.add_edge("A", "B", 1)
    G.add_edge("A", "C", 10)
    G.add_edge("B", "C", 1)
    G.add_edge("B", "D", 1)
    G.add_edge("D", "C", 1)
    G.add_edge("A", "E", 1)
    G.add_edge("E", "F", 1)
    G.add_edge("G", "F", 1)
    G.add_edge("F", "H", 1)
    G.add_edge("H", "I", 1)
    G.add_edge("I", "G", 100)

    print(G)


    import numpy as np
    print(np.array(G.to_adj_matrix()))

    print("\nBFS from A: ", G.bfs("A"))
    print("DFS from A: ", G.dfs("A"))
    print("Dijkstra from A: ", G.dijkstra("A"))
    print("Shortest Path From A to C: ", G.shortest_path("A", "C"))

    print()
    print(G.get_edges())
    print()
    print(G.get_nodes())
    print()
    print(G.get_nighbors("D"))

    print(G.has_node("F"))
    print(G.has_edge("A", "B"))

    print(len(G))

    G.remove_node("A")
    print(G.get_nodes())

    # G.remove_edge("A", "B")
    print(G.get_edges())

    print("==" * 30, "\nGraph - End\n")
    print()

    

    print("==" * 30, "\nDirected Graph:\nBeginning:\n", "__" * 30)
    print()

    graph = DirectedGraph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    print(graph)
    print(graph.has_edge("A", "B"))
    print(graph.neighbors("A"))
    print(len(graph))

    graph.remove_edge("A", "B")
    print(graph)

    print("==" * 30, "\nDirected Graph - End\n")
    print()



    print("==" * 30, "\nunDirected Graph:\nBeginning:\n", "__" * 30)
    print()

    
    graph = UndirectedGraph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    print(graph)
    print(graph.has_edge("A", "B"))
    print(graph.neighbors("A"))
    print(len(graph))

    graph.remove_edge("A", "B")
    print(graph)

    print("==" * 30, "\nunDirected Graph - End\n")
    print()


    print("==" * 30, "\nWeighted Graph:\nBeginning:\n", "__" * 30)
    print()
    
    graph = WeightedGraph()

    graph.add_edge("A", "B", 5)
    graph.add_edge("A", "C", 10)
    graph.add_edge("B", "D", 3)
    graph.add_edge("C", "D", 2)

    print(graph)
    print(graph.has_edge("A", "B"))
    print(graph.neighbors("A"))
    print(len(graph))


    print("==" * 30, "\nWeighted Graph - End\n")
    print()


    print("==" * 30, "\nunWeighted Graph:\nBeginning:\n", "__" * 30)
    print()

    graph = unweightedGraph()

    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")

    print(graph)
    print(graph.has_edge("A", "B"))
    print(graph.neighbors("A"))
    print(len(graph))

    graph.remove_edge("A", "B")
    print(graph)

    print("==" * 30, "\nunWeighted Graph - End\n")
    print()