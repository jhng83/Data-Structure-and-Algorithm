'''
In this example, the Graph class has methods to add nodes and edges. The traverse_dfs 
and traverse_bfs methods perform depth-first and breadth-first traversals, respectively.
 Adjust the methods and class structure according to your specific needs. The manual creation
 of nodes an edges here are just to illustrate the concept.
 '''
class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, start, end, weight=None):
        self.add_node(start)
        self.add_node(end)
        self.graph[start].append({'node': end, 'weight': weight})
    
    #implementing depth first traversal
    def traverse_dfs(self, start, visited=None):
        if visited is None:
            visited = set()
        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph[start]:
            if neighbor['node'] not in visited:
                self.traverse_dfs(neighbor['node'], visited)
                
    #implementing breath first traversal
    def traverse_bfs(self, start):
        visited = set()
        queue = [start]
        visited.add(start)

        while queue:
            current = queue.pop(0)
            print(current, end=" ")

            for neighbor in self.graph[current]:
                if neighbor['node'] not in visited:
                    queue.append(neighbor['node'])
                    visited.add(neighbor['node'])


# Example usage:
if __name__ == "__main__":
    my_graph = Graph()
    
    my_graph.add_edge('A', 'B', 2)
    my_graph.add_edge('A', 'C', 1)
    my_graph.add_edge('B', 'D', 3)
    my_graph.add_edge('B', 'E', 4)
    my_graph.add_edge('C', 'F', 5)

    print("DFS traversal:")
    my_graph.traverse_dfs('A')
    print("\nBFS traversal:")
    my_graph.traverse_bfs('A')

