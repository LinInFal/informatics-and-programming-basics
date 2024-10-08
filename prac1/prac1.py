print("=======Задание №1=======")
int_num = 10
float_num = 2.54
str_num = "text"
bool_val = True
print(int_num, float_num, str_num, bool_val)

print("=======Задание №2=======")
my_name, my_age = "Maxim", 21
print(my_name, my_age)

print("=======Задание №3=======")
x, y, z = 342, 56.2, '43'
print(x + int(y) + int(z))

print("=======Задание №4=======")
a, b = 3, 8
print((a+4*b)*(a-3*b)+a**2)

print("=======Задание №5=======")
a, b = map(int, input().split())
rectanlge_square = a * b
rectanlge_perimeter = 2 * (a + b)
print("Площадь прямоугольника: ", rectanlge_square, "\nПериметр прямоугольника: ", rectanlge_perimeter)

print("=======Задание №6=======")
print("*   *   *")
print(" * * * *")
print("  *  *")

print("=======Задание №7=======")
a, b = 5, 2
print("1. Сложение: ", a + b)
print("2. Вычитание: ", a - b)
print("3. Умножение: ", a * b)
print("4. Деление: ", a / b)
print("5. Деление по модулю: ", a % b)
print("6. Унарный плюс и минус: ", +a, -b)
print("7. Инкремент и декремент: ", a+1, b-1)
print("1. Равно: ", a == b)
print("2. Не равно: ", a != b)
print("3. Больше: ", a > b)
print("4. Меньше: ", a < b)
print("5. Больше или равно: ", a >= b)
print("6. Меньше или равно: ", a <= b)

print("=======Задание №8=======")
print(f"Меня зовут {my_name}, мне {my_age} лет")

print("=======Задание №9=======")
w1, w2, w3, w4, w5, w6, w7, w8 = "Съешь ", "ещё ", "этих ", "мягких ", "французских ", "булок, ", "да выпей ", "чаю"
print(w1+w2+w3+w4+w5+w6+w7+w8)

print("=======Задание №10=======")
str_val = 'Нет! Да!'
print(str_val * 4)

print("=======Задание №11=======")
x, y, z = map(int, input().split())
print(f"Результат вычисления: {(x+z)//y}")

print("=======Задание №12=======")
word = 'трансцендентность'
print(word[:4])
print(word[-2:])
print(word[3:7])
print(word[::-1])



