from basic.storage import Stack
from basic.visited_nodes import VisitedNodes

def depth_search(problem):
    node = problem.start()

    stack = Stack()
    stack.push(node)

    visited = VisitedNodes()
    # visited.add(node)

    while not stack.is_empty():
        node = stack.pop()
        visited.add(node)

        if (problem.test_goal(node)):
            return (visited.length(), node)
        
        next_nodes = problem.generate_next_nodes(node)

        for next_node in next_nodes:
            if not visited.was_visited(next_node):
                stack.push(next_node)

    return (visited.length(), None)
