import re

print("=======Задание №1=======")
temp = int(input())
if temp >= 20:
    print("Кондиционер выключается")
else:
    print("Кондиционер включается")

print("=======Задание №2=======")
in_month = int(input())
if 1 <= in_month <= 2 or in_month == 12:
    print("Зима")
elif 3 <= in_month <= 5:
    print("Весна")
elif 6 <= in_month <= 8:
    print("Лето")
else:
    print("Осень")

print("=======Задание №3=======")
age_input = input("Возраст собаки: ")
if not age_input.isdigit():
    print("Ошибка: не число")
else:
    dog_age = int(age_input)
    if dog_age < 1:
        print("Ошибка: число меньше 1")
    elif dog_age > 22:
        print("Ошибка: число большее 22")
    else:
        if dog_age == 1 or dog_age == 2:
            human_age = 10.5 * dog_age
        else:
            human_age = 21 + (dog_age - 2) * 4
        print(f"Возраст собаки в чел. годах: {human_age}")

print("=======Задание №4=======")
num = input()
last_digit = int(num[-1])
even = last_digit % 2 == 0
digit_sum = sum(int(digit) for digit in num)
sum_div_by_3 = digit_sum % 3 == 0
if even and sum_div_by_3:
    print(f"{num} делится на 6")
else:
    print(f"{num} не делится на 6")

print("=======Задание №5=======")
password = input()
errors = []
if len(password) < 8:
    errors.append("Пароль должен содержать не менее 8 символов")
if not re.search(r'[A-Z]', password):
    errors.append("Пароль должен содержать хотя бы 1 заглавную букву")
if not re.search(r'[a-z]', password):
    errors.append("Пароль должен содержать хотя бы 1 строчную букву")
if not re.search(r'[0-9]', password):
    errors.append("Пароль должен содержать хотя бы 1 цифру")
if not re.search(r'[!@#$%^&*(),.?":{}|<>_-]', password):
    errors.append("Пароль должен содержать хотя бы 1 спец. символ")

if errors:
    print("Пароль не надежен по следующим условиям:")
    for error in errors:
        print(f"- {error}")
else:
    print("Пароль надежен")