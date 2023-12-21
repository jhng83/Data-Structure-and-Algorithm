'''
In this example, the Graph class has methods to add nodes and edges. The traverse_dfs 
and traverse_bfs methods perform depth-first and breadth-first traversals, respectively.
 Adjust the methods and class structure according to your specific needs. The manual creation
 of nodes an edges here are just to illustrate the concept.
 '''
import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, start, end, weight):
        self.add_node(start)
        self.add_node(end)
        self.graph[start].append({'node': end, 'weight': weight})
        self.graph[end].append({'node': start, 'weight': weight})  # For an undirected graph, add the reverse edge as well
    
    #implementing dijkstra_shortest_paths algorithm
    def dijkstra_shortest_paths(self, start):
        distances = {node: float('infinity') for node in self.graph}
        distances[start] = 0

        priority_queue = [(0, start)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            if current_distance > distances[current_node]:
                continue

            for neighbor in self.graph[current_node]:
                distance = current_distance + neighbor['weight']
                if distance < distances[neighbor['node']]:
                    distances[neighbor['node']] = distance
                    heapq.heappush(priority_queue, (distance, neighbor['node']))

        return distances

# Example usage:
if __name__ == "__main__":
    my_graph = Graph()

    nodes = ['A', 'B', 'C', 'D', 'E','F']
    
    # Add edges between all pairs of nodes with weights
    for i in range(len(nodes)):
        for j in range(i + 1, len(nodes)):
            weight = i + j
            my_graph.add_edge(nodes[i], nodes[j], weight)

    # Calculate shortest paths from node 'A'
    shortest_paths_from_A = my_graph.dijkstra_shortest_paths('B')

    # Print distances from 'A' to all other nodes
    for node, distance in shortest_paths_from_A.items():
        print(f"Distance from A to {node}: {distance}")
