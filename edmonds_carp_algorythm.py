# создаем матрицу смежности графа. Первая строка - исток, последеняя сток.
# capacity_graph1 = [
#     [0, 10, 0, 11, 0, 0],
#     [0, 0,  5, 0, 9,  0],
#     [0, 0,  0, 0, 7,  0],
#     [0, 0,  0, 0,  0, 5],
#     [0, 0,  0, 0,  0, 9],
#     [0, 0,  0, 0,  0, 0],
# ]

# capacity_graph1 = [
#     [0, 11, 0, 0, 21, 0, 0],
#     [0, 0, 0, 19, 0, 0, 13],
#     [0, 0, 0, 0, 0, 0, 13],
#     [0, 0, 10, 0, 0, 0, 0],
#     [0, 0, 0, 0, 0, 12, 0],
#     [0, 0, 0, 15, 0, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0]
# ]

capacity_graph1 = [
    [0, 10, 0, 11, 0, 0],
    [0, 0, 5, 0, 9, 0],
    [0, 0, 0, 0, 7, 0],
    [0, 0, 0, 0, 0, 5],
    [0, 0, 0, 0, 0, 11],
    [0, 0, 0, 0, 0, 0]
]

# напишем функцию поиска наикротчайшего пути
def bfs(c):
    parents = [None] * len(c)
    arrived = [False] * len(c)
    queue = [0]
    arrived[0] = True

    while queue:
        u = queue.pop(0)
        for v in range(len(c)):
            if (c[u][v]) != 0 and not arrived[v]:
                arrived[v] = True
                queue.append(v)
                parents[v] = u

            if c[u][v] != 0 and v == len(c)-1:
                # Собираем пути в обратной последовательности
                path = []
                vertex = len(c) - 1
                while vertex is not None:
                    path.append(vertex)
                    parent = parents[vertex]
                    vertex = parent
                path.reverse()
                return path

    return []


# Напишем алгоритм Эдмондса Карпа.
def max_flow(C):
    n = len(C)
    new_c = [*C]
    flow = 0

    path = bfs(C)

    while path[1:-1]:
        min_flows_on_path = []
        for i in range(1, len(path)):
            v1 = path[i-1]
            v2 = path[i]
            value_between_vertex = new_c[v1][v2]
            min_flows_on_path.append(value_between_vertex)
        min_flow = min(min_flows_on_path)

        for i in range(1, len(path)):
            v1 = path[i-1]
            v2 = path[i]
            new_c[v1][v2] -= min_flow
            new_c[v2][v1] -= min_flow

        path = bfs(new_c)
        flow += min_flow

    return flow


print(max_flow(capacity_graph1))
