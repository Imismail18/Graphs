# Graph Data Structures & Algorithms

A comprehensive Python implementation of graph data structures featuring multiple graph types (directed, undirected, weighted, unweighted) with essential algorithms including BFS, DFS, and Dijkstra's shortest path. Includes complete node/edge operations, adjacency list/matrix representations, and detailed time complexity analysis.

## Features

- **Multiple Graph Types:**
  - `Graph` - Main graph class supporting both directed and undirected graphs with optional weights
  - `DirectedGraph` - Specialized directed graph implementation
  - `UndirectedGraph` - Undirected graph with symmetric edges
  - `WeightedGraph` - Weighted directed graph for shortest path problems
  - `unweightedGraph` - Simple unweighted graph structure

- **Core Operations:**
  - Add/remove nodes and edges
  - Check node and edge existence
  - Get neighbors, nodes, and edges
  - Graph representation and matrix conversion

- **Graph Algorithms:**
  - **BFS (Breadth-First Search)** - O(V + E)
  - **DFS (Depth-First Search)** - O(V + E)
  - **Dijkstra's Algorithm** - O((V + E) log V)
  - **Shortest Path** - O((V + E) log V)
  - **Adjacency Matrix Conversion** - O(V + E)

## Installation

Clone the repository:
```bash
git clone <repository-url>
cd Graphs
```

No external dependencies required (standard library only).

## Usage

### Basic Graph Operations

```python
from graphs import Graph

# Create a graph
G = Graph()

# Add nodes
G.add_node("A")
G.add_node("B")
G.add_node("C")

# Add edges (with optional weights)
G.add_edge("A", "B", 1)
G.add_edge("A", "C", 10)
G.add_edge("B", "C", 1)

# Get information
print(G.get_nodes())      # All nodes
print(G.get_edges())      # All edges
print(G.get_neighbors("A"))  # Neighbors of A
print(len(G))             # Number of nodes

# Check existence
print(G.has_node("A"))    # True
print(G.has_edge("A", "B"))  # True
```

### Graph Algorithms

```python
# Breadth-First Search
bfs_order = G.bfs("A")
print("BFS:", bfs_order)

# Depth-First Search
dfs_order = G.dfs("A")
print("DFS:", dfs_order)

# Dijkstra's Algorithm (for weighted graphs)
distances = G.dijkstra("A")
print("Distances:", distances)

# Shortest Path
path = G.shortest_path("A", "C")
print("Shortest path A to C:", path)

# Convert to adjacency matrix
import numpy as np
matrix = G.to_adj_matrix()
print(np.array(matrix))
```

### Remove Operations

```python
# Remove edge
G.remove_edge("A", "B")

# Remove node (removes all associated edges)
G.remove_node("A")
```

## Graph Types

### Graph Class
Main graph implementation supporting both directed and undirected graphs.
```python
G = Graph(directed=False)  # Undirected (default)
G = Graph(directed=True)   # Directed
```

### DirectedGraph Class
Specialized for directed graphs only.
```python
dg = DirectedGraph()
dg.add_edge("A", "B")  # Only A→B, not B→A
```

### UndirectedGraph Class
Specialized for undirected graphs.
```python
ug = UndirectedGraph()
ug.add_edge("A", "B")  # Both A↔B
```

### WeightedGraph Class
For weighted directed graphs.
```python
wg = WeightedGraph()
wg.add_edge("A", "B", weight=5)
```

## Time Complexity

| Operation | Time Complexity |
|-----------|-----------------|
| Add Node | O(1) |
| Remove Node | O(V + E) |
| Add Edge | O(1) |
| Remove Edge | O(1) |
| Has Node | O(1) |
| Has Edge | O(1) |
| Get Neighbors | O(1) |
| BFS | O(V + E) |
| DFS | O(V + E) |
| Dijkstra | O((V + E) log V) |
| To Adjacency Matrix | O(V + E) |

## File Structure

```
graphs.py
├── Graph                 # Main graph class
├── DirectedGraph         # Directed graph implementation
├── UndirectedGraph       # Undirected graph implementation
├── WeightedGraph         # Weighted graph implementation
└── unweightedGraph       # Unweighted graph implementation
```

## Example Output

```
BFS from A:  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
DFS from A:  ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'I', 'H']
Dijkstra from A:  {'A': 0, 'B': 1, 'C': 2, 'D': 2, 'E': 1, 'F': 2, 'G': 3, 'H': 3, 'I': 4}
Shortest Path A to C:  ['A', 'B', 'C']
```

## Key Methods

### Graph Class
- `add_node(node)` - Add a node
- `remove_node(node)` - Remove a node
- `add_edge(from_node, to_node, weight=None)` - Add an edge
- `remove_edge(from_node, to_node)` - Remove an edge
- `get_nodes()` - Get all nodes
- `get_edges()` - Get all edges
- `get_neighbors(node)` - Get neighbors of a node
- `has_node(node)` - Check if node exists
- `has_edge(from_node, to_node)` - Check if edge exists
- `bfs(start)` - Breadth-first search
- `dfs(start)` - Depth-first search
- `dijkstra(start)` - Dijkstra's shortest path
- `shortest_path(start, end)` - Find shortest path
- `to_adj_matrix()` - Convert to adjacency matrix

## Contributing

Contributions are welcome! Feel free to submit issues and pull requests.

## License

This project is open source and available under the MIT License.

## Author

Created for educational purposes - learning data structures and graph algorithms.
