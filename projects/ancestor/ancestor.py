class Stack():
    def __init__(self):
        self.stack = []
    def push(self, value):
        self.stack.append(value)
    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None
    def size(self):
        return len(self.stack)

class Graph():
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, v_pair):
        if v_pair[1] not in self.vertices:
            self.vertices[v_pair[1]] = set()
            self.vertices[v_pair[1]].add(v_pair[0])
        else:
            self.vertices[v_pair[1]].add(v_pair[0])


    def get_neighbors(self, vertex_id):
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            return None


def earliest_ancestor(ancestors, starting_node):
    
    # build graph from input data 
    #input data list of parnet child pairs [(1,3),(2,3)]

    # if you flip the graph upside down, child above, dfs should return a path until the last node [6,3,1,10]
    #return node at path -1

    ## dfs

    g = Graph()

    for pair in ancestors:
        g.add_vertex(pair)

    if starting_node not in g.vertices:
        return -1

    s = Stack()
    visited = set()

    s.push([starting_node])

    better_path = []

    while s.size() > 0:

        path = s.pop()
        
        if len(path) > len(better_path):
            better_path = path
        elif len(path) == len(better_path):
            if path[-1] < better_path[-1]:
                better_path = path

        v = path[-1]

        if v not in visited:
            visited.add(v)

        neighbors = g.get_neighbors(v)

        if neighbors is not None:
            for neighbor in neighbors:
                new_path = path + [neighbor]
                s.push(new_path)
        
    return better_path[-1]






test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 6))
