from Input import edges
from collections import defaultdict, deque


def recursive(edge, graph, small_caves_visited, can_visit_one_small_cave_twice):
    paths_found = 0
    for destination in graph[edge]:
        if destination == "end":
            paths_found += 1
        elif destination == "start":
            continue
        elif destination[0].isupper():
            paths_found += recursive(destination, graph, small_caves_visited, can_visit_one_small_cave_twice)
        elif (can_visit_one_small_cave_twice and 2 not in small_caves_visited.values()) or small_caves_visited[
            destination
        ] < 1:
            small_caves_visited[destination] += 1
            paths_found += recursive(destination, graph, small_caves_visited, can_visit_one_small_cave_twice)
            small_caves_visited[destination] -= 1
    return paths_found


graph = defaultdict(set)
for edge in edges:
    graph[edge[0]].add(edge[1])
    graph[edge[1]].add(edge[0])

small_caves_visited = defaultdict(lambda: 0)
print(recursive("start", graph, small_caves_visited, False))
print(recursive("start", graph, small_caves_visited, True))
