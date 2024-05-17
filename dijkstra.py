def dijkstra_algorithm(graph, start):
    shortest_distance = {}
    predecessor = {}
    unseen_nodes = graph
    infinity = float('inf')

    for node in unseen_nodes:
        shortest_distance[node] = infinity
    shortest_distance[start] = 0

    while unseen_nodes:
        min_node = None
        for node in unseen_nodes:
            if min_node is None:
                min_node = node
            elif shortest_distance[node] < shortest_distance[min_node]:
                min_node = node

        for child_node, weight in graph[min_node].items():
            if weight + shortest_distance[min_node] < shortest_distance[child_node]:
                shortest_distance[child_node] = weight + shortest_distance[min_node]
                predecessor[child_node] = min_node

        unseen_nodes.pop(min_node)

    return shortest_distance

graph = {
    'A': {'B': 2, 'C': 6, 'E': 3},
    'B': {'A': 2, 'C': 2, 'D': 6},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 6, 'C': 1, 'E': 2},
    'E': {'A': 3, 'D': 2}
}

start_vertex = 'B'
shortest_distances = dijkstra_algorithm(graph, start_vertex)
print(f"Кратчайшие расстояния от вершины {start_vertex}: {shortest_distances}")