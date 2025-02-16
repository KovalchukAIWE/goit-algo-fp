import heapq

def dijkstra(graph, start):
    """
    Алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі.

    :param graph: Зважений граф, представлений у вигляді словника, де ключ – вершина,
                  а значення – список кортежів (сусідня_вершина, вага_ребра)
    :param start: Початкова вершина
    :return: Словник з найкоротшими відстанями від початкової вершини до кожної вершини графа
    """
    # Ініціалізуємо відстані до всіх вершин як нескінченність
    distances = {node: float('inf') for node in graph}
    distances[start] = 0  # Відстань до початкової вершини рівна нулю

    # Створюємо бінарну купу (мін-купа) з початковою парою (відстань, вершина)
    priority_queue = [(0, start)]
    
    while priority_queue:
        # Вибираємо вершину з мінімальною поточною відстанню
        current_distance, current_node = heapq.heappop(priority_queue)

        # Якщо знайдена відстань більше за зафіксовану, пропускаємо її
        if current_distance > distances[current_node]:
            continue
        
        # Переглядаємо всіх сусідів поточної вершини
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            # Якщо знайдено коротший шлях до сусіда, оновлюємо відстань
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances

if __name__ == '__main__':
    # Приклад зваженого графа. Граф представлено у вигляді словника,
    # де ключ – вершина, а значення – список кортежів (сусідня_вершина, вага_ребра)
    graph = {
        'A': [('B', 5), ('C', 1)],
        'B': [('A', 5), ('C', 2), ('D', 1)],
        'C': [('A', 1), ('B', 2), ('D', 4), ('E', 8)],
        'D': [('B', 1), ('C', 4), ('E', 3), ('F', 6)],
        'E': [('C', 8), ('D', 3)],
        'F': [('D', 6)]
    }

    start_node = 'A'
    shortest_distances = dijkstra(graph, start_node)

    print("Найкоротші відстані від вершини '{}':".format(start_node))
    for vertex, distance in shortest_distances.items():
        print("Вершина {}: {}".format(vertex, distance))
