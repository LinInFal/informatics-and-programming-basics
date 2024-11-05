print("=======Задание №1=======")
# def hms_convert(num, time1, time2):
#     time_dict = {'s': 1, 'm': 60, 'h': 3600}
#
#     num_in_seconds = int(num) * time_dict[time1]
#     converted_time = num_in_seconds / time_dict[time2]
#     return round(converted_time, 3)
#
# num, time1, time2 = map(str, input().split())
# res = hms_convert(num, time1, time2)
# print(f"{res}{time2}")

print("=======Задание №2=======")
def calculate_profit(deposit, years):
    if deposit < 30000:
        print("Мин. вклад должен быть не меньше 30000")

    if 30000 <= deposit < 40000:
        percent = 0
    elif deposit < 50000:
        percent = 0.003
    elif deposit < 60000:
        percent = 0.006
    elif deposit < 70000:
        percent = 0.009
    elif deposit < 80000:
        percent = 0.012
    elif deposit < 90000:
        percent = 0.015
    elif deposit < 100000:
        percent = 0.018
    else:
        percent = 0.05

    if years <= 3:
        total_percent = 0.03 + percent
    elif years <= 6:
        total_percent = 0.05 + percent
    else:
        total_percent = 0.02 + percent

    final_sum = deposit * ((1 + total_percent) ** years)
    print(final_sum)
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


print("=======Задание №5=======")
# def is_palindrome(s):
#     lower_string = ''.join(s.split()).lower()
#     if lower_string == lower_string[::-1]:
#         return 'Да'
#     else:
#         return 'Нет'
#
# res = is_palindrome(input())
# print(res)