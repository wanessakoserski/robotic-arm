from basic.visited_nodes import VisitedNodes
from basic.storage import PriorityQueue

def dijkstra(problem):
    node = problem.start()

    queue = PriorityQueue()
    queue.push(0, node)

    visited = VisitedNodes()
    visited.add(node)

    while not queue.is_empty():
        node = queue.pop()
        visited.add(node)

        if (problem.test_goal(node)):
            return (visited.length(), node)
        
        next_nodes = problem.generate_next_nodes(node)

        for next_node in next_nodes:
            if not visited.was_visited(next_node):
                next_node.cost = node.cost + problem.cost(node, next_node)
                next_cost = next_node.cost
                queue.push(next_cost, next_node)

    return (visited.length(), None)