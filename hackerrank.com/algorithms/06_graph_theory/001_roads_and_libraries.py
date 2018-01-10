"""
https://www.hackerrank.com/challenges/torque-and-development/problem

Минимальное остовное дерево
https://ru.wikipedia.org/wiki/%D0%9C%D0%B8%D0%BD%D0%B8%D0%BC%D0%B0%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5_%D0%BE%D1%81%D1%82%D0%BE%D0%B2%D0%BD%D0%BE%D0%B5_%D0%B4%D0%B5%D1%80%D0%B5%D0%B2%D0%BE
"""

import sys

def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)
    return visited

def make_graph(graph_list):
    graph = {index+1: set() for index in range(len(graph_list))}
    for pair in graph_list:
        a, b = pair
        graph[a].add(b)
        graph[b].add(a)
    return graph

def roadsAndLibraries(n, c_lib, c_road, cities):
    cities_graph = make_graph(cities)
    cities = set(range(1, n+1))
    print(cities)
    print(cities_graph)
    start = 1
    while True:
        visited = dfs(cities_graph, start)
        print(visited)
        cities = cities - visited
        if cities:
            start = list(cities)[0]
            continue
        else:
            break

    return ''

if __name__ == "__main__":
    # q = int(input().strip())
    #
    # for a0 in range(q):
    #     n, m, c_lib, c_road = input().strip().split(' ')
    #     n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
    #     cities = []
    #     for cities_i in range(m):
    #        cities_t = [int(cities_temp) for cities_temp in input().strip().split(' ')]
    #        cities.append(cities_t)

    input_list = ['2', ['3 3 2 1', ['1 2', '3 1', '2 3']], ['6 6 2 5', ['1 3', '3 4', '2 4', '1 2', '2 3', '5 6']]]

    q = int(input_list[0])

    for a0 in range(1, q+1):
        n, m, c_lib, c_road = input_list[a0][0].split()
        n, m, c_lib, c_road = [int(n), int(m), int(c_lib), int(c_road)]
        cities = []
        for cities_i in range(m):
           cities_t = [int(cities_temp) for cities_temp in input_list[a0][1][cities_i].split()]
           cities.append(cities_t)

        result = roadsAndLibraries(n, c_lib, c_road, cities)
        print(result)