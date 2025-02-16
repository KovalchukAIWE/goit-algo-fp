# Клас для вузла однозв'язного списку
class Node:
    def __init__(self, data):
        self.data = data  # дані вузла
        self.next = None  # посилання на наступний вузол


# Клас для однозв'язного списку
class LinkedList:
    def __init__(self):
        self.head = None  # початок списку

    def append(self, data):
        """Додає елемент у кінець списку."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        """Виводить список на екран."""
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def reverse(self):
        """Реверсує список, змінюючи посилання між вузлами."""
        prev = None
        current = self.head
        while current:
            nxt = current.next    # зберігаємо наступний вузол
            current.next = prev   # змінюємо напрямок посилання
            prev = current        # рухаємо prev вперед
            current = nxt         # рухаємо current вперед
        self.head = prev

    def sort(self):
        """Сортує список за допомогою алгоритму злиття."""
        self.head = merge_sort(self.head)


def merge_sorted_lists(l1, l2):
    """
    Об’єднує два відсортованих списки, повертаючи голову нового списку.
    """
    dummy = Node(0)  # допоміжний вузол
    tail = dummy
    while l1 and l2:
        if l1.data < l2.data:
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next

    # Додаємо залишок одного зі списків
    if l1:
        tail.next = l1
    else:
        tail.next = l2

    return dummy.next


def merge_sort(head):
    """
    Рекурсивна функція для сортування списку за алгоритмом злиття.
    Повертає голову відсортованого списку.
    """
    if head is None or head.next is None:
        return head

    # Знаходимо середину списку методом повзунів (slow-fast pointer)
    slow, fast = head, head.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    mid = slow.next
    slow.next = None  # розриваємо список на дві частини

    left = merge_sort(head)
    right = merge_sort(mid)

    return merge_sorted_lists(left, right)


def merge_two_sorted_lists(list1, list2):
    """
    Об’єднує два відсортованих LinkedList в один відсортований список.
    Повертає новий об’єкт LinkedList.
    """
    merged_list = LinkedList()
    merged_list.head = merge_sorted_lists(list1.head, list2.head)
    return merged_list


# Приклад використання:
if __name__ == "__main__":
    # Створюємо однозв'язний список та додаємо елементи
    ll = LinkedList()
    for value in [3, 1, 5, 2, 4]:
        ll.append(value)
    print("Початковий список:")
    ll.print_list()

    # Реверсуємо список
    ll.reverse()
    print("Список після реверсування:")
    ll.print_list()

    # Сортуємо список
    ll.sort()
    print("Список після сортування:")
    ll.print_list()

    # Створюємо два відсортованих списки для об'єднання
    ll1 = LinkedList()
    for value in [1, 3, 5, 7]:
        ll1.append(value)
    ll2 = LinkedList()
    for value in [2, 4, 6, 8]:
        ll2.append(value)

    print("Відсортований список 1:")
    ll1.print_list()
    print("Відсортований список 2:")
    ll2.print_list()

    # Об'єднуємо два відсортованих списки
    merged = merge_two_sorted_lists(ll1, ll2)
    print("Об'єднаний відсортований список:")
    merged.print_list()
