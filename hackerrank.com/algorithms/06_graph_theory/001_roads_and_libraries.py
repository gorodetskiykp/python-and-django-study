"""
https://www.hackerrank.com/challenges/torque-and-development/problem
"""

import sys


def roadsAndLibraries(n, c_lib, c_road, cities):
    cities_list = list(range(1, n+1))
    print('Города:', cities_list)
    city = cities_list[0]
    print('Город:', city)
    print('Дороги:', cities)
    for _ in range(2):
        for road in cities:
            print('Дорога:', road)
            print(city, city in road)
            if city in road:
                if city in cities_list:
                    cities_list.remove(city)
                    print('Города:', cities_list)
                cities.remove(road)
                print('Дороги:', cities)
                road.remove(city)
                city = road[0]
                print('Город:', city)
                break
    return '--'


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
