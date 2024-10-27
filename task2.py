from random import choice
from collections import deque


def find_node_in_graph():
    metro_graph = get_graph_adjacency()
    stations_list = list(metro_graph.keys())
    goal = choice(stations_list)

    print(f'Searching for {goal} station')
    print(f'DFS path {dfs_recursive(metro_graph, stations_list[0], goal)}')
    bfs_queue = deque()
    bfs_queue.append(stations_list[0])
    print(f'BFS path {bfs_recursive(metro_graph, bfs_queue, goal)}')


def get_graph_adjacency() -> dict:
    return {
        "Академмістечко": ["Житомирська"],
        "Житомирська": ["Академмістечко", "Святошин"],
        "Святошин": ["Житомирська", "Нивки"],
        "Нивки": ["Святошин", "Берестейська"],
        "Берестейська": ["Нивки", "Шулявська"],
        "Шулявська": ["Берестейська", "Політехнічний інститут"],
        "Політехнічний інститут": ["Шулявська", "Вокзальна"],
        "Вокзальна": ["Політехнічний інститут", "Університет"],
        "Університет": ["Вокзальна", "Театральна"],
        "Театральна": ["Університет", "Хрещатик", "Золоті ворота"],
        "Хрещатик": ["Театральна", "Арсенальна", "Майдан Незалежності"],
        "Арсенальна": ["Хрещатик", "Дніпро"],
        "Дніпро": ["Арсенальна", "Гідропарк"],
        "Гідропарк": ["Дніпро", "Лівобережна"],
        "Лівобережна": ["Гідропарк", "Дарниця"],
        "Дарниця": ["Лівобережна", "Чернігівська"],
        "Чернігівська": ["Дарниця", "Лісова"],
        "Лісова": ["Чернігівська"],

        "Героїв Дніпра": ["Мінська"],
        "Мінська": ["Героїв Дніпра", "Оболонь"],
        "Оболонь": ["Мінська", "Почайна"],
        "Почайна": ["Оболонь", "Тараса Шевченка"],
        "Тараса Шевченка": ["Почайна", "Контрактова площа"],
        "Контрактова площа": ["Тараса Шевченка", "Поштова площа"],
        "Поштова площа": ["Контрактова площа", "Майдан Незалежності"],
        "Майдан Незалежності": ["Поштова площа", "Хрещатик", "пл. Українських Героїв"],
        "пл. Українських Героїв": ["Майдан Незалежності", "Олімпійська", "Палац Спорту"],
        "Олімпійська": ["пл. Українських Героїв", "Палац Україна"],
        "Палац Україна": ["Олімпійська", "Либідська"],
        "Либідська": ["Палац Україна", "Деміївська"],
        "Деміївська": ["Либідська", "Голосіївська"],
        "Голосіївська": ["Деміївська", "Васильківська"],
        "Васильківська": ["Голосіївська", "Виставковий центр"],
        "Виставковий центр": ["Васильківська", "Іподром"],
        "Іподром": ["Виставковий центр", "Теремки"],
        "Теремки": ["Іподром"],

        "Сирець": ["Дорогожичі"],
        "Дорогожичі": ["Сирець", "Лук’янівська"],
        "Лук’янівська": ["Дорогожичі", "Золоті ворота"],
        "Золоті ворота": ["Лук’янівська", "Театральна", "Палац Спорту"],
        "Палац Спорту": ["Золоті ворота", "Кловська", "пл. Українських Героїв"],
        "Кловська": ["Палац Спорту", "Печерська"],
        "Печерська": ["Кловська", "Дружби народів"],
        "Дружби народів": ["Печерська", "Видубичі"],
        "Видубичі": ["Дружби народів", "Славутич"],
        "Славутич": ["Видубичі", "Осокорки"],
        "Осокорки": ["Славутич", "Позняки"],
        "Позняки": ["Осокорки", "Харківська"],
        "Харківська": ["Позняки", "Вирлиця"],
        "Вирлиця": ["Харківська", "Бориспільська"],
        "Бориспільська": ["Вирлиця", "Червоний хутір"],
        "Червоний хутір": ["Бориспільська"]
    }


def bfs_recursive(graph: dict, queue: deque, goal, visited=None):
    if visited is None:
        visited = set()
    if not queue:
        return None

    vertex = queue.popleft()

    if vertex == goal:
        # print(f'Found {vertex}')
        return [vertex]

    if vertex not in visited:
        # print(f'Current node {vertex}')
        # print(f'Visited nodes {visited}')
        visited.add(vertex)
        queue.extend(set(graph[vertex]) - visited)

    found = bfs_recursive(graph, queue, goal, visited)
    if found:
        return [vertex] + found

    return None


def dfs_recursive(graph: dict, vertex, goal, visited=None):
    if vertex == goal:
        # print(f'Found {vertex}')
        return [vertex]

    if visited is None:
        visited = set()
    visited.add(vertex)
    # print(f'Current node {vertex}')

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            found = dfs_recursive(graph, neighbor, goal, visited)
            if found:
                return [vertex] + found

    return None


if __name__ == "__main__":
    find_node_in_graph()