print("=======Задание №1=======")
tasks = [("Проверить почту", 3), ("Написать отчёт", 1), ("Позвонить клиенту", 2)]

priority = (lambda task: task[1])
sorted_tasks = sorted(tasks, key=priority)

print(sorted_tasks)

print("=======Задание №2=======")
purchases = [
    {"item": "Laptop", "price": 1000, "quantity": 2},
    {"item": "Mouse", "price": 25, "quantity": 5},
    {"item": "Keyboard", "price": 45, "quantity": 3}
]

total_price = list(map(lambda purchase: purchase["price"] * purchase["quantity"], purchases))
max_purchase_total_price = max(purchases, key=lambda purchase: purchase["price"] * purchase["quantity"])

print(total_price)
print(max_purchase_total_price)

print("=======Задание №3=======")
clients = [
    {"name": "Alice", "income": 50000},
    {"name": "Bob", "income": 120000},
    {"name": "Charlie", "income": 70000}
]

categorized_clients = list(map(lambda client: {**client, "category": "High" if client["income"] > 100000
                                               else "Medium" if 50000 <= client["income"] <= 100000
                                               else "Low"}, clients))
print(categorized_clients)

print("=======Задание №4=======")
flights = [
    {"flight": "A1", "departure": 9, "arrival": 12},
    {"flight": "B2", "departure": 14, "arrival": 18},
    {"flight": "C3", "departure": 6, "arrival": 8}
]

filtered_flights = list(filter(lambda flight: flight["arrival"] < 12, flights))
print(filtered_flights)

print("=======Задание №5=======")
messages = [
    {"user": "Исследователь А", "message": "Отчёт готов. Ссылка: http://foundation.org"},
    {"user": "Доктор Б", "message": "Документы можно найти здесь: https://classified.com"},
    {"user": "Охранник В", "message": "Нет аномальной активности за смену."},
    {"user": "Агент Г", "message": "Срочно изучите материалы по объекту 173 на http://statue-database.net"},
    {"user": "Д-р Кляйн", "message": "Обновлённый протокол эксперимента доступен: https://safezone.scp"},
    {"user": "Сотрудник Д", "message": "Просьба ознакомиться с https://docs.anomalies-secure.com перед сменой."},
    {"user": "Старший учёный Л", "message": "Все записи переданы. Никаких аномалий на объекте 096."},
    {"user": "Техник З", "message": "Проблема с сервером устранена. Подробнее: http://fix-report.internal"}
]

filtered_messages = list(filter(lambda msg: "http" in msg["message"], messages))
print(filtered_messages)
result = [
    {
    "user": msg["user"],
    "message": msg["message"].replace(msg["message"].split("http")[1], "[ДАННЫЕ УДАЛЕНЫ]")
    }
    for msg in filtered_messages
]

print(result)