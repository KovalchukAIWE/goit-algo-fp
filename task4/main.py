import uuid
import networkx as nx
import matplotlib.pyplot as plt

# Клас вузла дерева з додатковими властивостями
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор вузла

# Функція для рекурсивного додавання ребер у граф (для візуалізації)
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        # Додаємо вузол до графу із збереженням кольору та мітки
        graph.add_node(node.id, color=node.color, label=node.val)
        # Обробка лівого піддерева
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer  # Обчислення координати для лівого вузла
            pos[node.left.id] = (l, y - 1)
            add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        # Обробка правого піддерева
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer  # Обчислення координати для правого вузла
            pos[node.right.id] = (r, y - 1)
            add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

# Функція для малювання дерева за допомогою NetworkX та Matplotlib
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}  # Початкова позиція кореня
    tree = add_edges(tree, tree_root, pos)

    # Отримання списку кольорів та міток для вузлів
    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Функція для побудови бінарного дерева з купи (списку)
def build_heap_tree(heap, index=0):
    """
    Рекурсивно будує бінарне дерево з елементів купи.
    heap  - список елементів купи (наприклад, [15, 10, 8, 5, 4, 2, 1])
    index - поточний індекс у списку (за замовчуванням 0 для кореня)
    Для вузла з індексом i:
      лівий нащадок: 2*i + 1,
      правий нащадок: 2*i + 2.
    """
    if index >= len(heap):
        return None
    # Створюємо вузол з поточним значенням
    node = Node(heap[index])
    # Рекурсивно будуємо ліве та праве піддерево
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node

# Функція для візуалізації купи
def draw_heap(heap):
    """
    Побудова та візуалізація бінарної купи.
    heap - список елементів купи.
    """
    root = build_heap_tree(heap)
    draw_tree(root)

# Приклад використання:
if __name__ == "__main__":
    # Приклад купи (максимальна купа)
    heap = [15, 10, 8, 5, 4, 2, 1]
    draw_heap(heap)
