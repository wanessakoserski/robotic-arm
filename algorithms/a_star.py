from basic.visited_nodes import VisitedNodes
from basic.storage import PriorityQueue

def a_star(problem):
    node = problem.start()

    queue = PriorityQueue()
    queue.push(0, node)

    visited = VisitedNodes()
    # visited.add(node)

    while not queue.is_empty():
        node = queue.pop()
        visited.add(node)

        if(problem.test_goal(node)):
            return (visited.length(), node)
        
        next_nodes = problem.generate_next_nodes(node)

        for next_node in next_nodes:
            if not visited.was_visited(next_node):
                next_node.cost = node.cost + problem.cost(node, next_node)
                next_node.heuristic = problem.heuristic(next_node)
                a_star_n = (next_node.cost + next_node.heuristic)

                queue.push(a_star_n, next_node)

    return (visited.length(), None)