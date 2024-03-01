import heapq


def minimal_cost_to_combine_cables(cable_lengths):
    # Ініціалізуємо мінімальну купу з довжин кабелів
    heapq.heapify(cable_lengths)

    total_cost = 0
    # Поки в купі більше одного кабелю
    while len(cable_lengths) > 1:
        # Видалити з купи два кабелі з найменшою довжиною
        first_min = heapq.heappop(cable_lengths)
        second_min = heapq.heappop(cable_lengths)

        # Обчислити витрати на їх з'єднання (сума довжин)
        cost = first_min + second_min

        # Додати витрати на з'єднання до загальних витрат
        total_cost += cost

        # Вставити новий кабель (суму довжин) назад до купи
        heapq.heappush(cable_lengths, cost)

    # Загальні витрати представлятимуть мінімальну суму витрат на з'єднання всіх кабелів
    return total_cost


# Тестові дані
cable_lengths = [5, 4, 2, 8]

# Виклик функції
minimal_cost_to_combine_cables(cable_lengths)
