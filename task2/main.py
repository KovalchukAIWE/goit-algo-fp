import turtle
import math

def draw_pythagoras_tree(x, y, s, angle, theta, level):
    """
    Рекурсивна функція для побудови дерева Піфагора.
    
    Параметри:
      x, y   - координати нижнього лівого кута квадрату (базового блоку)
      s      - довжина сторони квадрату
      angle  - орієнтація квадрату (кут у градусах, який визначає напрямок сторони AB)
      theta  - кут для розгалуження (розквіт) (у градусах)
      level  - поточний рівень рекурсії (якщо 0 – рекурсію завершено)
    """
    if level == 0:
        return

    # Обчислюємо вершини квадрату.
    # Нехай A = (x, y) – нижній лівий кут.
    # Вектор AB має довжину s і напрямок angle:
    rad = math.radians(angle)
    A = (x, y)
    B = (x + s * math.cos(rad), y + s * math.sin(rad))
    # Щоб отримати перпендикулярну сторону, обчислюємо вектор, що є поворотом вектора AB на 90°:
    # Вектор перпендикулярний до (cos(angle), sin(angle)) – це (-sin(angle), cos(angle)).
    D = (x - s * math.sin(rad), y + s * math.cos(rad))
    # Третя вершина – C, отримана як B плюс той самий перпендикулярний вектор:
    C = (B[0] - s * math.sin(rad), B[1] + s * math.cos(rad))
    
    # Малюємо квадрат (A -> B -> C -> D -> A)
    turtle.penup()
    turtle.goto(A)
    turtle.pendown()
    turtle.goto(B)
    turtle.goto(C)
    turtle.goto(D)
    turtle.goto(A)
    
    # Рекурсивно будуємо дві “гілки” дерева:
    # 1. Ліва “гілка” прикріплена до вершини D.
    #    Нова довжина сторони: s_left = s * cos(theta),
    #    нова орієнтація: angle_left = angle + theta.
    new_s_left = s * math.cos(math.radians(theta))
    new_angle_left = angle + theta
    draw_pythagoras_tree(D[0], D[1], new_s_left, new_angle_left, theta, level - 1)
    
    # 2. Права “гілка” прикріплена до вершини C.
    #    Нова довжина сторони: s_right = s * sin(theta),
    #    нова орієнтація: angle_right = angle - (90 - theta)
    new_s_right = s * math.sin(math.radians(theta))
    new_angle_right = angle - (90 - theta)
    draw_pythagoras_tree(C[0], C[1], new_s_right, new_angle_right, theta, level - 1)

def main():
    # Налаштування вікна та черепашки
    turtle.title("Фрактал: дерево Піфагора")
    turtle.speed(0)         # максимально швидко
    turtle.hideturtle()     # приховуємо черепашку для чистоти малюнку
    turtle.tracer(False)    # вимикаємо анімацію для пришвидшення малювання
    
    # Запитуємо у користувача рівень рекурсії
    level_input = turtle.numinput("Рівень рекурсії", 
                                  "Введіть рівень рекурсії (наприклад, 5):", 
                                  default=5, minval=0, maxval=15)
    if level_input is None:
        return
    level = int(level_input)
    
    # Параметри базового квадрату:
    s = 100              # довжина сторони базового квадрату
    x = -s / 2           # нижній лівий кут: обираємо так, щоб квадрат був по центру по горизонталі
    y = -250             # нижнє положення (можна змінити за бажанням)
    base_angle = 0       # орієнтація базового квадрату: 0° → сторона направлена вправо
    theta = 45           # кут розгалуження (розквіт), зазвичай 45°
    
    # Побудова дерева Піфагора
    draw_pythagoras_tree(x, y, s, base_angle, theta, level)
    
    turtle.tracer(True)
    turtle.done()

if __name__ == '__main__':
    main()
