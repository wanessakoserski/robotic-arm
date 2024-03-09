class Node:
    def __init__(self, state, parent_node=None, edge=None, cost=0.0, heuristic=0.0):
        self.state = state
        self.parent_node = parent_node
        self.edge = edge
        self.cost = cost
        self.heuristic = heuristic


    def __repr__(self):
        return str(self.state)
    
    
    def __lt__(self, another):
        return (self.cost + self.heuristic) < (another.cost + another.heuristic)