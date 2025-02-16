import matplotlib.pyplot as plt
from collections import deque

# %% 1. Створення структури вузла та побудова дерева

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        # Для візуалізації: координати вузла
        self.x = None
        self.y = None

def insert(root, val):
    """Вставка значення у бінарне дерево пошуку."""
    if root is None:
        return Node(val)
    else:
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
    return root

def build_tree(values):
    """Побудова дерева з послідовності значень."""
    root = None
    for v in values:
        root = insert(root, v)
    return root

# %% 2. Присвоєння координат вузлам для візуалізації

def assign_positions(node, depth=0, pos=[0]):
    """
    In-order обхід для присвоєння координат:
      - x: порядковий номер у in-order обході,
      - y: від'ємна глибина (щоб корінь був у верхній частині).
    """
    if node is None:
        return
    assign_positions(node.left, depth + 1, pos)
    node.x = pos[0]
    node.y = -depth
    pos[0] += 1
    assign_positions(node.right, depth + 1, pos)

# %% 3. Ітеративні обходи дерева

def dfs_iterative(root):
    """Ітеративний обхід у глибину (pre-order) за допомогою стеку."""
    stack = []
    order = []  # список вузлів у порядку відвідування
    if root is not None:
        stack.append(root)
    while stack:
        node = stack.pop()
        order.append(node)
        # Для pre-order: спочатку додаємо праве, потім ліве (щоб ліве оброблялося першим)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return order

def bfs_iterative(root):
    """Ітеративний обхід у ширину за допомогою черги."""
    q = deque()
    order = []  # список вузлів у порядку відвідування
    if root is not None:
        q.append(root)
    while q:
        node = q.popleft()
        order.append(node)
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return order

# %% 4. Генерація кольорів для вузлів

def get_color(index, total, base_color=(18, 150, 240), lower_factor=0.3, upper_factor=1.0):
    """
    Обчислення кольору для вузла залежно від порядкового номера відвідування.
    Повертає колір у вигляді hex (наприклад, "#1296F0").
    """
    fraction = index / (total - 1) if total > 1 else 1
    factor = lower_factor + fraction * (upper_factor - lower_factor)
    r = int(base_color[0] * factor)
    g = int(base_color[1] * factor)
    b = int(base_color[2] * factor)
    return f"#{r:02X}{g:02X}{b:02X}"

# %% 5. Функції візуалізації

def draw_tree(root, traversal_order, title="Tree Traversal"):
    """
    Статична візуалізація дерева:
      - малює всі вузли та зв'язки,
      - кожному вузлу присвоюється колір залежно від порядку обходу.
    """
    # Визначаємо порядковий номер відвідання для кожного вузла
    order_index = {node: i for i, node in enumerate(traversal_order)}
    total = len(traversal_order)
    
    # Збираємо всі вузли (можна обійти рекурсивно — це прийнятно для візуалізації)
    nodes = []
    def collect_nodes(node):
        if node:
            nodes.append(node)
            collect_nodes(node.left)
            collect_nodes(node.right)
    collect_nodes(root)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Малюємо ребра (зв'язки між вузлами)
    for node in nodes:
        if node.left:
            ax.plot([node.x, node.left.x], [node.y, node.left.y], 'k-')
        if node.right:
            ax.plot([node.x, node.right.x], [node.y, node.right.y], 'k-')
    
    # Малюємо вузли
    for node in nodes:
        idx = order_index.get(node, 0)
        color = get_color(idx, total)
        circle = plt.Circle((node.x, node.y), 0.3, color=color, ec='black', zorder=3)
        ax.add_artist(circle)
        ax.text(node.x, node.y, str(node.val), ha='center', va='center',
                color='white', fontsize=10, zorder=4)
    
    ax.set_title(title, fontsize=14)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.show()
    plt.close(fig)  # Закриваємо фігуру після відображення

def animate_traversal(root, traversal_order, title="Traversal Animation"):
    """
    Анімація обходу дерева:
      - спочатку малюється дерево зі сірими вузлами,
      - потім, крок за кроком, змінюється колір вузлів згідно з порядком обходу.
    """
    # Збираємо всі вузли для малювання
    nodes = []
    def collect_nodes(node):
        if node:
            nodes.append(node)
            collect_nodes(node.left)
            collect_nodes(node.right)
    collect_nodes(root)
    
    fig, ax = plt.subplots(figsize=(8, 5))
    
    # Малюємо ребра
    for node in nodes:
        if node.left:
            ax.plot([node.x, node.left.x], [node.y, node.left.y], 'k-')
        if node.right:
            ax.plot([node.x, node.right.x], [node.y, node.right.y], 'k-')
    
    # Створюємо патчі для вузлів — спочатку всі вузли сірі
    node_patch = {}
    for node in nodes:
        patch = plt.Circle((node.x, node.y), 0.3, color='gray', ec='black', zorder=3)
        ax.add_artist(patch)
        node_patch[node] = patch
        ax.text(node.x, node.y, str(node.val), ha='center', va='center',
                color='white', fontsize=10, zorder=4)
    
    ax.set_title(title, fontsize=14)
    ax.set_aspect('equal')
    ax.axis('off')
    plt.draw()
    plt.pause(1)  # Пауза перед стартом анімації
    
    total = len(traversal_order)
    # Анімація: по одному вузлу змінюємо його колір
    for i, node in enumerate(traversal_order):
        color = get_color(i, total)
        patch = node_patch[node]
        patch.set_color(color)
        ax.set_title(f"{title} - Крок {i+1}: вузол {node.val}", fontsize=14)
        plt.draw()
        plt.pause(0.5)
    
    plt.show()
    plt.close(fig)  # Закриваємо фігуру після завершення анімації

# %% 6. Головна частина програми

if __name__ == "__main__":
    # Створюємо дерево з фіксованим набором значень
    values = [50, 30, 70, 20, 40, 60, 80]
    root = build_tree(values)
    
    # Присвоюємо вузлам координати для візуалізації (in-order)
    assign_positions(root)
    
    # Отримуємо порядок обходу
    dfs_order = dfs_iterative(root)
    bfs_order = bfs_iterative(root)
    
    # Статична візуалізація обходів
    draw_tree(root, dfs_order, title="DFS (обхід у глибину, pre-order)")
    draw_tree(root, bfs_order, title="BFS (обхід у ширину)")
    
    # Анімація обходів
    animate_traversal(root, dfs_order, title="Анімація DFS (pre-order)")
    animate_traversal(root, bfs_order, title="Анімація BFS")
