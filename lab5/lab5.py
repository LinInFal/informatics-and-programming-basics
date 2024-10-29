import random

print("=======Задание №1=======")
list = [1, 2, 12, 50, 75, 43, 37, 19, 10, 11]
list[2] = 100
print(list)

print("=======Задание №2=======")
list = [1, 7, 12, 37, 50]
list_square = [i**2 for i in list]
print(list_square)

print("=======Задание №3=======")
list = [1, 7, 12, 37, 50]
print(max(list) / len(list))

print("=======Задание №4=======")
def tpl_sort(tpl):
    for i in tpl:
        if not isinstance(i, int):
            return tpl
    return tuple(sorted(tpl))

in_tuple = (1, 5, 7, 10, 8, 2)
tuple_sorted = tpl_sort(in_tuple)
print(tuple_sorted)

print("=======Задание №5=======")
products = {'milk': 5, 'bread': 2, 'cookies': 8}
min = min(products, key=products.get)
max = max(products, key=products.get)
print(max, products[max])
print(min, products[min])

print("=======Задание №6=======")
list = [1, 'odd', 10, 'ok']
dict = {i: i for i in list}
print(dict)

print("=======Задание №7=======")
dict = {'бегать': 'run'}
input_word = input().lower()
if input_word in dict:
    print(dict[input_word])
else:
    print('Нет такого слова')

print("=======Задание №8=======")
options = ['камень', 'ножницы', 'бумага', 'ящерица', 'спок']
rules = {
    'камень': ['ножницы', 'ящерица'],
    'ножницы': ['бумага', 'ящерица'],
    'бумага': ['камень', 'спок'],
    'ящерица': ['бумага', 'спок'],
    'спок': ['камень', 'ножницы'],
}

while True:
    for i in options:
        print(i, end=" ")
    user_choice = input('\nВведите один из вариантов выше: ').lower()
    if user_choice == ' ':
        break
    if user_choice not in options:
        print('Неверный ввод')
        continue
    computer_choice = random.choice(options)
    print('Компьютер выбрал:', computer_choice)
    if user_choice == computer_choice:
        print('Ничья')
    elif computer_choice in rules[user_choice]:
        print('Вы выиграли')
    else:
        print('Вы проиграли')