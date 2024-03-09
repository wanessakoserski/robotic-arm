class VisitedNodes:
    def __init__(self):
        self.visited = set({})


    def add(self, node):
        self.visited.add(tuple(node.state))


    def was_visited(self, node):
        return tuple(node.state) in self.visited
    
    
    def length(self):
        return len(self.visited)