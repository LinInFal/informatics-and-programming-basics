print("=======Задание №1=======")
def hms_convert(num, time1, time2):
    time_dict = {'s': 1, 'm': 60, 'h': 3600}

    num_in_seconds = int(num) * time_dict[time1]
    converted_time = num_in_seconds / time_dict[time2]
    return round(converted_time, 3)

num, time1, time2 = map(str, input().split())
res = hms_convert(num, time1, time2)
print(f"{res}{time2}")

print("=======Задание №2=======")
def calculate_profit(deposit, years):
    if deposit < 30000:
        print("Мин. вклад должен быть не меньше 30000")

    if years <= 3:
        base_percent = 3.0
    elif 4 <= years <= 6:
        base_percent = 5.0
    else:
        base_percent = 2.0

    additional_percent = min((deposit // 10000) * 0.3, 5.0)
    total_percent = base_percent + additional_percent

    final_sum = deposit * (1 + total_percent / 100) ** years
    profit = final_sum - deposit
    return round(profit, 2)

print(calculate_profit(30000, 3))
print(calculate_profit(100000, 5))
print(calculate_profit(200000, 8))

print("=======Задание №3=======")
def print_primes_in_range(start, end):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5)+1):
            if n % i == 0:
                return False
        return True

    if start == 0 or end == 1:
        print("Error!")

    primes = []
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)
    if primes:
        return ' '.join(map(str, primes))

print(print_primes_in_range(1, 10))
print(print_primes_in_range(15, 120))

print("=======Задание №4=======")
def matrix_addition(size, matrix1, matrix2):
    if size < 2:
        return "Error!"

    # Проверка, что обе матрицы имеют размерность size x size
    if any(len(row) != size for row in matrix1) or any(len(row) != size for row in matrix2):
        return "Error!"

    res_matrix = []
    for i in range(size):
        row = []
        for j in range(size):
            # Складываем элементы матриц
            row.append(matrix1[i][j] + matrix2[i][j])
        res_matrix.append(row)
    return res_matrix

size1 = 2
matrix1_1 = [
    [2, 5],
    [5, 3]
]
matrix2_1 = [
    [5, 2],
    [4, 1]
]
print(matrix_addition(size1, matrix1_1, matrix2_1))

size2 = 3
matrix1_2 = [
    [0, -1, 4],
    [6, 12, -4],
    [4, 1, 10]
]
matrix2_2 = [
    [5, 1, 12],
    [-4, 2, -8],
    [0, 1, 4]
]
print(matrix_addition(size2, matrix1_2, matrix2_2))

size3 = 1
matrix1_3 = [
    [4]
]
matrix2_3 = [
    [5]
]
print(matrix_addition(size3, matrix1_3, matrix2_3))

print("=======Задание №5=======")
def is_palindrome(s):
    lower_string = ''.join(s.split()).lower()
    if lower_string == lower_string[::-1]:
        return 'Да'
    else:
        return 'Нет'

res = is_palindrome(input())
print(res)