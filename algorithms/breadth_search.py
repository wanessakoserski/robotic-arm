from basic.storage import Queue
from basic.visited_nodes import VisitedNodes

def breadth_search(problem):
    node = problem.start()

    queue = Queue()
    queue.push(node)

    visited = VisitedNodes()

    while not queue.is_empty():
        node = queue.pop()
        visited.add(node)

        if (problem.test_goal(node)):
            return (visited.length(), node)
        
        next_nodes = problem.generate_next_nodes(node)

        for next_node in next_nodes:
            if not visited.was_visited(next_node):
                queue.push(next_node) 

    return (visited.length(), None)

