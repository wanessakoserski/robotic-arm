from robotic_arm import RoboticArm
from basic.path import edge_path, node_path
from algorithms.dijkstra import dijkstra
from algorithms.a_star import a_star
from algorithms.depth_search import depth_search
from algorithms.greedy import greedy_search


def test_problem(problem, algorithm):
    (visited_states_amount, solution_node) = algorithm(problem)

    if (solution_node is None):
        print("There is no solution for the problem")
    else:
        path = edge_path(solution_node)
        print(f"Solution: {path}")
        nodes = node_path(solution_node)

    print(f"Visited states: {visited_states_amount}")

    print("Initial state: ")
    print(problem.show(problem.root_node))

    print("Next states: ")
    for node in nodes:
        print("Next node cost: " + str(node.cost))
        print("Next node movements: " + str(node.edge))
        print(problem.show(node))


if __name__ == "__main__":
    problem = RoboticArm()

    print("\n\n>> Robotic arm problem using Greedy Search <<\n")
    test_problem(problem, greedy_search)

    print("\n\n>> Robotic arm problem using Dijkstra <<\n")
    test_problem(problem, dijkstra)

    print("\n\n>> Robotic arm problem using A* <<\n")
    test_problem(problem, a_star)
