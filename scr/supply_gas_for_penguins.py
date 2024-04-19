def gas_supply(list_city, list_storage, list_active_gas_pipelines):
    def create_adjacency_list(active_pipelines):
        adjacency_list = {}
        for pipeline in active_pipelines:
            source, destination = pipeline
            if source not in adjacency_list:
                adjacency_list[source] = []
            if destination not in adjacency_list:
                adjacency_list[destination] = []
            adjacency_list[source].append(destination)
        return adjacency_list

    def dfs(graph, start, visited):
        visited.add(start)
        for neighbor in graph.get(start, ()):
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

    unreachable = {}
    for storage in list_storage:
        visited = set()
        dfs(graph, storage, visited)

        # unreachable_cities = set(list_city)
        unreachable_cities = []
        for city in list_city:
            if city not in visited:
                unreachable_cities.append(city)

        if unreachable_cities:
            unreachable[storage] = unreachable_cities

    return unreachable
