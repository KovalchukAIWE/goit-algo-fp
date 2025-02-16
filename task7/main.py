import random
import matplotlib.pyplot as plt

# Кількість кидків кубиків
num_rolls = 1_000_000

# Ініціалізація лічильників для сум від 2 до 12
counts = {total: 0 for total in range(2, 13)}

# Симуляція кидків двох кубиків
for _ in range(num_rolls):
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    total = die1 + die2
    counts[total] += 1

# Обчислення симуляційної ймовірності для кожної суми
simulated_probabilities = {total: counts[total] / num_rolls for total in counts}

# Аналітичні (теоретичні) ймовірності для суми при киданні двох кубиків
# Формула: кількість сприятливих випадків / 36
theoretical_probabilities = {
    2: 1/36,
    3: 2/36,
    4: 3/36,
    5: 4/36,
    6: 5/36,
    7: 6/36,
    8: 5/36,
    9: 4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36
}

# Виведення таблиці результатів
print("Сума\tСимуляційна ймовірність\tАналітична ймовірність")
for total in range(2, 13):
    sim_prob = simulated_probabilities[total]
    theo_prob = theoretical_probabilities[total]
    print(f"{total}\t{sim_prob:.4f}\t\t\t{theo_prob:.4f}")

# Побудова графіка для порівняння ймовірностей
sums = list(range(2, 13))
sim_values = [simulated_probabilities[total] for total in sums]
theo_values = [theoretical_probabilities[total] for total in sums]

plt.figure(figsize=(10, 6))
# Будуємо стовпчикові діаграми: зсунути один набір стовпчиків відносно іншого
width = 0.35
plt.bar([s - width/2 for s in sums], sim_values, width=width, label='Симуляційна', alpha=0.8)
plt.bar([s + width/2 for s in sums], theo_values, width=width, label='Аналітична', alpha=0.8)

plt.xlabel('Сума чисел на кубиках')
plt.ylabel('Ймовірність')
plt.title('Порівняння симуляційної та аналітичної ймовірностей при киданні двох кубиків')
plt.xticks(sums)
plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
