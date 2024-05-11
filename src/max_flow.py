import csv
from collections import defaultdict, deque

infinity = float("inf")


def bfs(graph, source, sink, parent):
    visited = set()
    queue = deque()
    queue.append(source)
    visited.add(source)

    while queue:
        node = queue.popleft()

        for neighbor, capacity in graph[node].items():
            if capacity > 0 and neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = node

    return sink in visited


def ford_fulkerson(graph, source, sink):
    max_flow = 0
    parent = {}

    while bfs(graph, source, sink, parent):
        path_flow = infinity
        node = sink

        while node != source:
            path_flow = min(path_flow, graph[parent[node]][node])
            node = parent[node]

        max_flow += path_flow
        node = sink
        while node != source:
            parent_node = parent[node]
            graph[parent_node][node] -= path_flow
            node = parent[node]

    return max_flow


def read_graph_from_file(filename):
    graph = defaultdict(dict)
    with open(filename, newline="") as csv_file:
        reader = csv.reader(csv_file)
        farms = next(reader)
        shops = next(reader)
        for row in reader:
            node1, node2, capacity = row
            graph[node1][node2] = int(capacity)

    return graph, farms, shops


def calculate_max_flow(filename):
    graph, farms, shops = read_graph_from_file(filename)

    source = "Source"
    sink = "Sink"

    for farm in farms:
        graph[source][farm] = infinity
    for shop in shops:
        graph[shop][sink] = infinity

    max_flow = ford_fulkerson(graph, source, sink)
    return max_flow
