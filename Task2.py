import turtle


def koch_curve(t, order, size):

    # Базовий випадок рекурсії
    if order == 0:
        t.forward(size)
        return

    # Довжина сегмента
    size /= 3

    # Рекурсивна побудова
    koch_curve(t, order - 1, size)

    t.left(60)
    koch_curve(t, order - 1, size)

    t.right(120)
    koch_curve(t, order - 1, size)

    t.left(60)
    koch_curve(t, order - 1, size)


def draw_koch_snowflake(order, size=300):

    # Налаштування вікна
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Сніжинка Коха")

    # Налаштування черепашки
    t = turtle.Turtle()
    t.speed(0)

    # Початкова позиція
    t.penup()
    t.goto(-150, 90)
    t.pendown()

    # Малювання трьох сторін
    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    # Завершення
    turtle.done()


def main():

    # Введення рівня рекурсії
    level = int(input("Введіть рівень рекурсії: "))

    draw_koch_snowflake(level)


if __name__ == "__main__":
    main()