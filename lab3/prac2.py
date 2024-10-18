print("=======Задание №1=======")
name, age = input(), int(input())
for i in range(1, 11):
    print(f"Меня зовут {name} и мне {age} лет")

print("=======Задание №2=======")
num = int(input("Введите число от 1 до 9: "))
if 1 <= num <= 9:
    for i in range(1, 10):
        print(num * i, end=' ')

print("\n=======Задание №3=======")
for i in range(0, 101, 3):
    print(i, end=' ')

print("\n=======Задание №4=======")
num = int(input("Введите число: "))
fact = 1
for num in range(2, num + 1):
    fact *= num
    print(fact, end=' ')

print("\n=======Задание №5=======")
x = 21
while x > 0:
    x -= 1
    print(x, end=' ')

print("\n=======Задание №6=======")
fib1 = fib2 = 1
n = int(input())
print(fib1, fib2, end=' ')
for i in range(2, n):
    fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end=' ')

print("\n=======Задание №7=======")
in_str = str(input("Введите строку: "))
new_str = ""
for i in range(len(in_str)):
    new_str += in_str[i]
    new_str += str(i+1)
print(new_str)  # привет => п1р2и3в4е5т6

print("\n=======Задание №8=======")
in_num1, in_num2 = map(int, input("Введите два числа через пробел: ").split())
while True:
    print("Сумма равна: ", in_num1 + in_num2)
    in_num1, in_num2 = map(int, input("Введите два числа через пробел: ").split())