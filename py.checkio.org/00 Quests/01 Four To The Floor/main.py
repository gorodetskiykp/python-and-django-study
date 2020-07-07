"""
Даются размеры комнаты и список PIR-датчиков, установленных на потолке. 
Требуется определить, вся ли комната входит в зону видимости датчиков (вернуть True) или нет (вернуть False). 
Нижний левый угол прямоугольника (комнаты) совпадает с точкой начала координат O, верхний правый угол определяется длиной W и шириной H. 
Каждый датчик определяется координатами xi и yi точки, где он установлен, и его радиусом действия Ri.
Входные данные: Два аргумента:
список, содержащий значения длины и ширины комнаты (целочисленные) [W, H]
список, содержащий информацию координаты и радиусы датчиков (целочисленные)
[[xi, yi, Ri], [xi+1, yi+1, Ri+1], ....., [xn, yn, Rn]]
Выходные данные: True or False.
Примеры:
is_covered([200, 150], [[100, 75, 130]]) == True                                   #example #1
is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) == True                    #example #2
is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) == False    #example #3
"""


def is_covered(room, sensors):
    is_covered_flag = True
    for x in range(room[0]+1):
        for y in range(room[1]+1):
            if is_covered_flag == False:
                return is_covered_flag
            for sensor in sensors:
                rxy = ((x - sensor[0])**2 + (y - sensor[1])**2)**0.5
                if rxy > sensor[2]:
                    is_covered_flag = False
                else:
                    is_covered_flag = True
                    break
    return is_covered_flag


if __name__ == '__main__':
    print("Example:")
    print(is_covered([200, 150], [[100, 75, 130]]))

    assert is_covered([200, 150], [[100, 75, 130]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 75, 100]]) == True
    assert is_covered([200, 150], [[50, 75, 100], [150, 25, 50], [150, 125, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 60], [0, 110, 60], [200, 40, 60], [200, 110, 60]]) == True
    assert is_covered([200, 150], [[100, 75, 100], [0, 40, 50], [0, 110, 50], [200, 40, 50], [200, 110, 50]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 110]]) == False
    assert is_covered([200, 150], [[100, 75, 110], [105, 75, 20]]) == False
    assert is_covered([3, 1], [[1, 0, 2], [2, 1, 2]]) == True
    assert is_covered([30, 10], [[0, 10, 10], [10, 0, 10], [20, 10, 10], [30, 0, 10]]) == True
    assert is_covered([30, 10], [[0, 10, 8], [10, 0, 7], [20, 10, 9], [30, 0, 10]]) == False