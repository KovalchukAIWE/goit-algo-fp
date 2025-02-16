# Дані про страви
items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

def greedy_algorithm(items, budget):
    """
    Жадібний алгоритм: сортуємо страви за спаданням співвідношення калорії/вартість
    та послідовно додаємо їх, якщо дозволяє бюджет.
    """
    # Створимо список із кортежів: (назва, cost, calories, ratio)
    item_list = []
    for name, info in items.items():
        cost = info["cost"]
        calories = info["calories"]
        ratio = calories / cost
        item_list.append((name, cost, calories, ratio))
    
    # Сортуємо за ratio в порядку спадання
    item_list.sort(key=lambda x: x[3], reverse=True)
    
    chosen = []
    total_cost = 0
    total_calories = 0
    remaining_budget = budget

    for name, cost, calories, ratio in item_list:
        if cost <= remaining_budget:
            chosen.append(name)
            total_cost += cost
            total_calories += calories
            remaining_budget -= cost

    result = {
        "chosen_items": chosen,
        "total_cost": total_cost,
        "total_calories": total_calories
    }
    return result

def dynamic_programming(items, budget):
    """
    Динамічне програмування для задачі 0/1 рюкзака:
    знаходимо набір страв із максимальною сумарною калорійністю, не перевищуючи бюджет.
    """
    # Перетворимо словник на список кортежів: (name, cost, calories)
    item_list = []
    for name, info in items.items():
        item_list.append((name, info["cost"], info["calories"]))
    n = len(item_list)
    
    # Створимо DP-таблицю розміром (n+1) x (budget+1)
    # dp[i][w] — максимальна калорійність, досягнута з першими i стравами при бюджеті w
    dp = [[0 for _ in range(budget + 1)] for _ in range(n + 1)]
    
    # Заповнюємо таблицю
    for i in range(1, n + 1):
        name, cost, calories = item_list[i-1]
        for w in range(budget + 1):
            if cost > w:
                dp[i][w] = dp[i-1][w]
            else:
                dp[i][w] = max(dp[i-1][w], dp[i-1][w - cost] + calories)
    
    # Відновлюємо вибір страв
    w = budget
    chosen = []
    total_cost = 0
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            name, cost, calories = item_list[i-1]
            chosen.append(name)
            total_cost += cost
            w -= cost

    # Оскільки ми відновлювали вибір з кінця, можемо перевернути список
    chosen.reverse()

    result = {
        "chosen_items": chosen,
        "total_cost": total_cost,
        "total_calories": dp[n][budget]
    }
    return result

# Приклад використання
if __name__ == "__main__":
    budget = 100  # встановлений бюджет

    print("Жадібний алгоритм:")
    greedy_result = greedy_algorithm(items, budget)
    print("Обрані страви:", greedy_result["chosen_items"])
    print("Загальна вартість:", greedy_result["total_cost"])
    print("Загальна калорійність:", greedy_result["total_calories"])

    print("\nДинамічне програмування:")
    dp_result = dynamic_programming(items, budget)
    print("Обрані страви:", dp_result["chosen_items"])
    print("Загальна вартість:", dp_result["total_cost"])
    print("Загальна калорійність:", dp_result["total_calories"])
