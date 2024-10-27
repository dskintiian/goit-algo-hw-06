from random import choice


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


def get_graph_real() -> dict:
    return {
        "Академмістечко": {"Житомирська": 5},
        "Житомирська": {"Академмістечко": 5, "Святошин": 3},
        "Святошин": {"Житомирська": 3, "Нивки": 6},
        "Нивки": {"Святошин": 6, "Берестейська": 4},
        "Берестейська": {"Нивки": 4, "Шулявська": 7},
        "Шулявська": {"Берестейська": 7, "Політехнічний інститут": 8},
        "Політехнічний інститут": {"Шулявська": 8, "Вокзальна": 5},
        "Вокзальна": {"Політехнічний інститут": 5, "Університет": 2},
        "Університет": {"Вокзальна": 2, "Театральна": 3},
        "Театральна": {"Університет": 3, "Хрещатик": 6, "Золоті ворота": 1},
        "Хрещатик": {"Театральна": 6, "Арсенальна": 4, "Майдан Незалежності": 1},
        "Арсенальна": {"Хрещатик": 4, "Дніпро": 5},
        "Дніпро": {"Арсенальна": 5, "Гідропарк": 7},
        "Гідропарк": {"Дніпро": 7, "Лівобережна": 6},
        "Лівобережна": {"Гідропарк": 6, "Дарниця": 5},
        "Дарниця": {"Лівобережна": 5, "Чернігівська": 4},
        "Чернігівська": {"Дарниця": 4, "Лісова": 3},
        "Лісова": {"Чернігівська": 3},

        "Героїв Дніпра": {"Мінська": 7},
        "Мінська": {"Героїв Дніпра": 7, "Оболонь": 6},
        "Оболонь": {"Мінська": 6, "Почайна": 5},
        "Почайна": {"Оболонь": 5, "Тараса Шевченка": 4},
        "Тараса Шевченка": {"Почайна": 4, "Контрактова площа": 8},
        "Контрактова площа": {"Тараса Шевченка": 8, "Поштова площа": 3},
        "Поштова площа": {"Контрактова площа": 3, "Майдан Незалежності": 6},
        "Майдан Незалежності": {"Поштова площа": 6, "Хрещатик": 1, "Площа Українських Героїв": 2},
        "Площа Українських Героїв": {"Майдан Незалежності": 2, "Олімпійська": 5, "Палац Спорту": 1},
        "Олімпійська": {"Площа Українських Героїв": 5, "Палац Україна": 7},
        "Палац Україна": {"Олімпійська": 7, "Либідська": 4},
        "Либідська": {"Палац Україна": 4, "Деміївська": 6},
        "Деміївська": {"Либідська": 6, "Голосіївська": 5},
        "Голосіївська": {"Деміївська": 5, "Васильківська": 7},
        "Васильківська": {"Голосіївська": 7, "Виставковий центр": 8},
        "Виставковий центр": {"Васильківська": 8, "Іподром": 3},
        "Іподром": {"Виставковий центр": 3, "Теремки": 4},
        "Теремки": {"Іподром": 4},

        "Сирець": {"Дорогожичі": 5},
        "Дорогожичі": {"Сирець": 5, "Лук’янівська": 7},
        "Лук’янівська": {"Дорогожичі": 7, "Золоті ворота": 6},
        "Золоті ворота": {"Лук’янівська": 6, "Театральна": 1, "Палац Спорту": 4},
        "Палац Спорту": {"Золоті ворота": 4, "Кловська": 3, "Площа Українських Героїв": 1},
        "Кловська": {"Палац Спорту": 3, "Печерська": 6},
        "Печерська": {"Кловська": 6, "Дружби народів": 4},
        "Дружби народів": {"Печерська": 4, "Видубичі": 5},
        "Видубичі": {"Дружби народів": 5, "Славутич": 7},
        "Славутич": {"Видубичі": 7, "Осокорки": 6},
        "Осокорки": {"Славутич": 6, "Позняки": 5},
        "Позняки": {"Осокорки": 5, "Харківська": 4},
        "Харківська": {"Позняки": 4, "Вирлиця": 8},
        "Вирлиця": {"Харківська": 8, "Бориспільська": 6},
        "Бориспільська": {"Вирлиця": 6, "Червоний хутір": 3},
        "Червоний хутір": {"Бориспільська": 3}
    }


def get_graph_unreal():
    return {
        "Академмістечко": {"Житомирська": 5, "Політехнічний інститут": 9, "Дарниця": 13, "Лук’янівська": 11},
        "Житомирська": {"Академмістечко": 5, "Святошин": 3, "Лук’янівська": 10, "Харківська": 14, "Олімпійська": 8},
        "Святошин": {"Житомирська": 3, "Нивки": 6, "Іподром": 12, "Героїв Дніпра": 9, "Червоний хутір": 7},
        "Нивки": {"Святошин": 6, "Берестейська": 4, "Славутич": 10, "Осокорки": 13, "Мінська": 8},
        "Берестейська": {"Нивки": 4, "Шулявська": 7, "Майдан Незалежності": 10, "Либідська": 15, "Театральна": 9},
        "Шулявська": {"Берестейська": 7, "Політехнічний інститут": 8, "Голосіївська": 12, "Вирлиця": 11,
                      "Печерська": 7},
        "Політехнічний інститут": {"Шулявська": 8, "Вокзальна": 5, "Мінська": 13, "Площа Українських Героїв": 10,
                                   "Дарниця": 8},
        "Вокзальна": {"Політехнічний інститут": 5, "Університет": 2, "Осокорки": 11, "Деміївська": 14,
                      "Поштова площа": 9},
        "Університет": {"Вокзальна": 2, "Театральна": 3, "Кловська": 15, "Мінська": 12, "Лук’янівська": 9},
        "Театральна": {"Університет": 3, "Хрещатик": 6, "Позняки": 12, "Виставковий центр": 8, "Контрактова площа": 14},
        "Хрещатик": {"Театральна": 6, "Арсенальна": 4, "Контрактова площа": 15, "Вокзальна": 8, "Славутич": 9},
        "Арсенальна": {"Хрещатик": 4, "Дніпро": 5, "Осокорки": 14, "Героїв Дніпра": 9, "Майдан Незалежності": 8},
        "Дніпро": {"Арсенальна": 5, "Гідропарк": 7, "Тараса Шевченка": 10, "Площа Українських Героїв": 12,
                   "Чернігівська": 9},
        "Гідропарк": {"Дніпро": 7, "Лівобережна": 6, "Дарниця": 13, "Харківська": 10, "Олімпійська": 11},
        "Лівобережна": {"Гідропарк": 6, "Дарниця": 5, "Майдан Незалежності": 14, "Васильківська": 12,
                        "Золоті ворота": 8},
        "Дарниця": {"Лівобережна": 5, "Чернігівська": 4, "Політехнічний інститут": 13, "Сирець": 10, "Оболонь": 7},
        "Чернігівська": {"Дарниця": 4, "Лісова": 3, "Золоті ворота": 15, "Дорогожичі": 12, "Позняки": 9},
        "Лісова": {"Чернігівська": 3, "Вокзальна": 14, "Славутич": 9, "Поштова площа": 10, "Контрактова площа": 11},

        "Героїв Дніпра": {"Мінська": 7, "Святошин": 10, "Дніпро": 9, "Славутич": 12, "Театральна": 6},
        "Мінська": {"Героїв Дніпра": 7, "Оболонь": 6, "Палац Україна": 8, "Святошин": 11, "Вирлиця": 10},
        "Оболонь": {"Мінська": 6, "Почайна": 5, "Дарниця": 9, "Палац Спорту": 11, "Арсенальна": 12},
        "Почайна": {"Оболонь": 5, "Тараса Шевченка": 4, "Лівобережна": 10, "Іподром": 9, "Гідропарк": 8},
        "Тараса Шевченка": {"Почайна": 4, "Контрактова площа": 8, "Голосіївська": 10, "Палац Україна": 9,
                            "Поштова площа": 7},
        "Контрактова площа": {"Тараса Шевченка": 8, "Поштова площа": 3, "Палац Спорту": 9, "Кловська": 11,
                              "Дніпро": 12},
        "Поштова площа": {"Контрактова площа": 3, "Майдан Незалежності": 6, "Театральна": 5, "Вирлиця": 10,
                          "Славутич": 8},
        "Майдан Незалежності": {"Поштова площа": 6, "Хрещатик": 1, "Площа Українських Героїв": 2, "Золоті ворота": 7,
                                "Оболонь": 10},
        "Площа Українських Героїв": {"Майдан Незалежності": 2, "Олімпійська": 5, "Палац Спорту": 1, "Героїв Дніпра": 6,
                                   "Іподром": 8},
        "Олімпійська": {"Площа Українських Героїв": 5, "Палац Україна": 7, "Театральна": 9, "Сирець": 10, "Мінська": 11},
        "Палац Україна": {"Олімпійська": 7, "Либідська": 4, "Васильківська": 10, "Теремки": 9, "Золоті ворота": 12},
        "Либідська": {"Палац Україна": 4, "Деміївська": 6, "Голосіївська": 5, "Шулявська": 8, "Харківська": 11},
        "Деміївська": {"Либідська": 6, "Голосіївська": 5, "Печерська": 9, "Виставковий центр": 10, "Теремки": 12},
        "Голосіївська": {"Деміївська": 5, "Васильківська": 7, "Іподром": 11, "Шулявська": 9, "Оболонь": 10},
        "Васильківська": {"Голосіївська": 7, "Виставковий центр": 8, "Іподром": 12, "Хрещатик": 10, "Кловська": 11},
        "Виставковий центр": {"Васильківська": 8, "Іподром": 3, "Теремки": 4, "Бориспільська": 10, "Печерська": 8},
        "Іподром": {"Виставковий центр": 3, "Теремки": 4, "Гідропарк": 9, "Сирець": 10, "Кловська": 6},
        "Теремки": {"Іподром": 4, "Героїв Дніпра": 8, "Васильківська": 10, "Деміївська": 12, "Мінська": 7},

        "Сирець": {"Дорогожичі": 5, "Лук’янівська": 8, "Васильківська": 10, "Палац Спорту": 12, "Арсенальна": 9},

        "Дорогожичі": {"Сирець": 5, "Лук’янівська": 4, "Шулявська": 10, "Золоті ворота": 8, "Героїв Дніпра": 9},
        "Лук’янівська": {"Дорогожичі": 4, "Золоті ворота": 6, "Кловська": 8, "Театральна": 9, "Святошин": 7},
        "Золоті ворота": {"Лук’янівська": 6, "Палац Спорту": 5, "Хрещатик": 10, "Оболонь": 11,
                          "Тараса Шевченка": 8},
        "Палац Спорту": {"Золоті ворота": 5, "Театральна": 6, "Контрактова площа": 9, "Голосіївська": 11,
                         "Харківська": 10},
        "Кловська": {"Лук’янівська": 8, "Театральна": 7, "Печерська": 5, "Вирлиця": 11, "Славутич": 9},
        "Печерська": {"Кловська": 5, "Голосіївська": 7, "Дружби народів": 10, "Арсенальна": 8, "Лісова": 12},
        "Дружби народів": {"Печерська": 10, "Видубичі": 6, "Гідропарк": 9, "Тараса Шевченка": 11, "Сирець": 8},
        "Видубичі": {"Дружби народів": 6, "Славутич": 8, "Лісова": 9, "Почайна": 12, "Мінська": 7},
        "Славутич": {"Видубичі": 8, "Осокорки": 6, "Позняки": 5, "Тараса Шевченка": 11, "Героїв Дніпра": 9},
        "Осокорки": {"Славутич": 6, "Позняки": 3, "Лівобережна": 10, "Хрещатик": 8, "Майдан Незалежності": 12},
        "Позняки": {"Осокорки": 3, "Харківська": 7, "Голосіївська": 12, "Дніпро": 10, "Мінська": 11},
        "Харківська": {"Позняки": 7, "Вирлиця": 5, "Бориспільська": 10, "Героїв Дніпра": 12, "Театральна": 14},
        "Вирлиця": {"Харківська": 5, "Бориспільська": 6, "Дніпро": 8, "Лівобережна": 12, "Голосіївська": 10},
        "Бориспільська": {"Вирлиця": 6, "Червоний хутір": 7, "Дніпро": 9, "Героїв Дніпра": 11, "Печерська": 10},
        "Червоний хутір": {"Бориспільська": 7, "Харківська": 8, "Тараса Шевченка": 9, "Гідропарк": 10,
                           "Славутич": 12},
    }


if __name__ == "__main__":
    print('Real data')
    metro_graph = get_graph_real()

    start = choice(list(metro_graph.keys()))
    print(f'Startpoint {start}')
    print(dijkstra(metro_graph, start))

    print('Not real data :D')
    metro_graph = get_graph_unreal()

    start = choice(list(metro_graph.keys()))
    print(f'Startpoint {start}')
    print(dijkstra(metro_graph, start))
