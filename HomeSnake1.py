# Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным

day = int(input('Укажите номер дня недели '))

if day < 1 or day > 7:
    print('Бог создал в неделе только семь дней, не выёживайся')
elif day < 6:
    print ('День будний. Иди работай, а не читай мои глупые шутки')
else:
    print ('Это выходной, можешь смело отдыхать, уря!')


# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x = bool(input('Укажите X '))
y = bool(input('Укажите Y '))
z = bool(input('Укажите Z '))

left = not(x or y or z)
right = not(x) and not(y) and not(z)

if left == right:
    print('True')
else:
    print('False')

# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер 
# четверти плоскости, в которой находится эта точка (или на какой оси она находится).

x = int(input('Укажите ненулевую координату по оси абсцисс: '))
y = int(input('Укажите ненулевую координату по оси ординат: '))

if x > 0 and y > 0:
    print('Точка находится в четверти №1')
elif x < 0 and y > 0:
    print('Точка находится в четверти №2')
elif x < 0 and y < 0:
    print('Точка находится в четверти №3')
elif x > 0 and y < 0:
    print('Точка находится в четверти №4')


# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

qwerty = int(input('Укажите номер четверти: '))

if qwerty == 1:
    print('По оси абсцисс от 0 до +∞, по оси ординат от 0 до +∞')
elif qwerty == 2:
    print('По оси абсцисс от 0 до -∞, по оси ординат от 0 до +∞')
elif qwerty == 3:
    print('По оси абсцисс от 0 до -∞, по оси ординат от 0 до -∞')
elif qwerty == 4:
    print('По оси абсцисс от 0 до +∞, по оси ординат от 0 до -∞')

# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

ax = int(input('Укажите координату точки A по оси абсцисс: '))
ay = int(input('Укажите координату точки A по оси ординат: '))
bx = int(input('Укажите координату точки B по оси абсцисс: '))
by = int(input('Укажите координату точки B по оси ординат: '))

result = ((bx - ax) ** 2 + (by - ay) ** 2) ** (0.5)
print(result)