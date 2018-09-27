# ONLY ASSUMPTION IS THAT THE GRAPH IS SETUP THE SAME WAY USING A DICTIONARY
# BY NATHAN M
# Helper class used to store each node and what it is connected to
class adjacency_list(object):
    def __init__(self, key):
        self.key = key
        self.connections = {}

    def add_adjacency(self, neighbor, weight = 0):
        self.connections[neighbor] = weight

    def get_key(self):
        return self.key

    def get_adjacencies(self):
        return self.connections.keys()

# Graph used to build the complete structure of nodes
class graph(object):
    def __init__(self):
        self.verticies = {}

    def add_vertex(self, key):
        vertex = adjacency_list(key)
        self.verticies[key] = vertex
        return vertex

    def add_edge(self, start_node, end_node, weight = 0):
        if start_node not in self.verticies:
            self.add_vertex(start_node)
        if end_node not in self.verticies:
            self.add_vertex(end_node)
        # Forms the relationship between two nodes
        self.verticies[start_node].add_adjacency(self.verticies[end_node], weight)
    # Used to iterate over dictionary
    def __iter__(self):
        return iter(self.verticies.values())


def depth_first(graph, root):
    visited, stack = [], [root.get_key()]
    while stack:
        vertex = stack.pop()
        print("Vertex: %s" % vertex)
        if vertex not in visited:
            visited.append(vertex)
            print("Visited: %s" % visited)
            for entry in graph.verticies[vertex].get_adjacencies():
                stack.append(entry.get_key())
    return visited


def breath_first(graph, root):
    visited, stack = [], [root.get_key()]
    while stack:
        vertex = stack.pop(0)
        print("Vertex: %s" % vertex)
        if vertex not in visited:
            visited.append(vertex)
            print("Visited: %s" % visited)
            for entry in graph.verticies[vertex].get_adjacencies():
                stack.append(entry.get_key())
    return visited

# Example Graph setup
adj_list = graph()
for index in range(4):
    adj_list.add_vertex(index)

adj_list.add_edge(0, 1)
adj_list.add_edge(0, 3)
adj_list.add_edge(1, 2)
adj_list.add_edge(2, 4)
adj_list.add_edge(2, 3)

print("RUNNING DEPTH FIRST")
print(depth_first(adj_list, adj_list.verticies[0]))
print("RUNNING BREATH FIRST")
print(breath_first(adj_list, adj_list.verticies[0]))
