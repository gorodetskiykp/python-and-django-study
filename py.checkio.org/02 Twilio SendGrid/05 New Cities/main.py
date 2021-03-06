"""
Иногда поврежденные вышки не подлежат восстановлению. В этом случае люди, которые были подключены к разрушенной вышке, должны переселиться в другой район на время, 
пока администрация пытается удалить неисправности.
Но если разрушенная вышка отключает несколько районов друг от друга, сеть разделяется на две подсети, и каждая из них должна иметь своего мэра. 
Мэры должны использовать голубей, чтобы слать друг другу сообщения. В случае, когда сеть разделена, Вам не нужны сотни голубей.
Ваша миссия - выяснить, сколько нужно мэров, чтобы контролировать весь город, когда некоторые вышки разрушены. Другими словами, 
Вам необходимо выяснить, сколько подсетей будет сформировано после того, как некоторые вышки разрушатся и не будут восстановлены.
Входные данные: Два параметра: структура сети (как список соединений между вышками) и список разрушенных вышек.
Выходные данные: Int. Количество подсетей, сформированных после разрушения вышек.
Пример:
    subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2
    subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3
    subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1
"""

def subnetworks(net, crushes):
    cities = 0
    checked = []
    normal_points = set(item for pair in net for item in pair).difference(crushes)
    for point in normal_points:
        if point not in checked:
            cities += 1
            for pair in net:
                if point in pair:
                    checked.append(set(pair).difference(point).pop())
    return cities

if __name__ == '__main__':
    print(subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D'],
            ['D', 'F']
        ], ['B']))
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['B']) == 2, "First"
    assert subnetworks([
            ['A', 'B'],
            ['A', 'C'],
            ['A', 'D'],
            ['D', 'F']
        ], ['A']) == 3, "Second"
    assert subnetworks([
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D']
        ], ['C', 'D']) == 1, "Third"

