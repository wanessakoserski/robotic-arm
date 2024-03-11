from basic.storage import PriorityQueue
from basic.visited_nodes import VisitedNodes

def greedy_search(problem):
    node = problem.start()

    queue = PriorityQueue()
    queue.push(0, node)

    visited = VisitedNodes()

    while not queue.is_empty():
        node = queue.pop()
        visited.add(node)

        if problem.test_goal(node):
            return (visited.length(), node)

        next_nodes = problem.generate_next_nodes(node)

        for next_node in next_nodes:
            if not visited.was_visited(next_node):
                heuristic_value = problem.heuristic(next_node)
                queue.push(heuristic_value, next_node)

    return (visited.length(), None)
