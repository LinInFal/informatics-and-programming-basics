import json
from datetime import datetime

"""
Консольный трекер расходов и доходов
"""

categories = {
    "Еда": "расход",
    "Транспорт": "расход",
    "Развлечения": "расход",
    "Зарплата": "доход",
}

records = []
DATA = "data.json"

def load_data():
    global categories, records
    try:
        with open(DATA, "r", encoding="utf-8") as file:
            data = json.load(file)
            categories = data.get("categories", categories)
            records = data.get("records", records)
    except FileNotFoundError:
        save_data()  # Создать файл, если его нет

def save_data():
    with open(DATA, "w", encoding="utf-8") as file:
        json.dump({"categories": categories, "records": records}, file, ensure_ascii=False, indent=4)

def add_category():
    name = input("Введите название новой категории: ")
    category_type = input("Это доход или расход?: ").strip().lower()
    categories[name] = category_type
    print(f"[!] Категория '{name}' добавлена как '{category_type}'.")
    save_data()

def delete_category():
    name = input(f"Введите название категории для удаления ({', '.join(categories.keys())}): ")
    if name in categories:
        del categories[name]
        print(f"[!] Категория '{name}' удалена.")
        global records
        records = [r for r in records if r['category'] != name]
        print("[!] Все записи с этой категорией также удалены.")
        save_data()
    else:
        print("[!] Категория не найдена.")

def view_categories():
    print("\nКатегории:")
    for name, category_type in categories.items():
        print(f"{name}: {category_type}")

def add_record():
    amount = float(input("Введите сумму: "))
    category = input(f"Введите категорию ({', '.join(categories.keys())}): ")
    date = input("Введите дату (ГГГГ-ММ-ДД или пустым для текущей даты): ") or datetime.now().strftime("%Y-%m-%d")
    date = datetime.strptime(date, "%Y-%m-%d").date()
    description = input("Введите описание (опционально): ")
    record_type = categories[category]
    records.append({"amount": amount, "category": category, "date": str(date), "description": description, "type": record_type})
    print("[!] Запись добавлена.")
    save_data()

def delete_record():
    view_records()
    record_index = int(input("\nВведите номер записи для удаления: "))
    if 0 <= record_index < len(records):
        records.pop(record_index)
        print(f"[!] Запись удалена")
        save_data()
    else:
        print("[!] Неверный номер записи.")

def view_records():
    print("\nВсе записи:")
    for i, record in enumerate(records):
        print(f"{i}: {record['date']}: {record['category']} ({record['type']}): {record['amount']} руб. - {record['description']}")

def filter_records():
    print("Фильтр записей:")
    category_filter = input(f"Введите категорию для фильтрации ({', '.join(categories.keys())} или оставьте пустым для всех): ")
    date_filter = input("Введите дату для фильтрации (ГГГГ-ММ-ДД или пустым для всех): ")
    filtered_records = records

    if category_filter:
        filtered_records = [r for r in filtered_records if r['category'] == category_filter]
    if date_filter:
        date_filter = datetime.strptime(date_filter, "%Y-%m-%d").date()
        filtered_records = [r for r in filtered_records if r['date'] == str(date_filter)]

    print("\nОтфильтрованные записи:")
    for record in filtered_records:
        print(f"{record['date']}: {record['category']} ({record['type']}): {record['amount']} руб. - {record['description']}")

def calculate_balance():
    income = sum(r['amount'] for r in records if r['type'] == "доход")
    expenses = sum(r['amount'] for r in records if r['type'] == "расход")
    balance = income - expenses
    print(f"\nДоходы: {income} руб.\nРасходы: {expenses} руб.\nИтоговый баланс: {balance} руб.")

def analyze_expenses():
    print("\nАнализ расходов:")
    category_totals = {}
    for record in records:
        if record['type'] == "расход":
            category_totals[record['category']] = category_totals.get(record['category'], 0) + record['amount']

    if not category_totals:
        print("[!] Нет данных для анализа.")
        return

    print("Расходы по категориям:")
    for category, total in category_totals.items():
        print(f"{category}: {total} руб.")

    sorted_totals = sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
    print("\nТоп категорий расходов:")
    for i, (category, total) in enumerate(sorted_totals, start=1):
        print(f"{i}. {category} ({total} руб.)")

def main():
    load_data()
    while True:
        print("\nМеню:")
        print("1. Добавить категорию")
        print("2. Удалить категорию")
        print("3. Просмотреть категории")
        print("4. Добавить запись")
        print("5. Удалить запись")
        print("6. Просмотреть записи")
        print("7. Фильтровать записи")
        print("8. Итоговый баланс")
        print("9. Анализ расходов")
        print("10. Выйти")

        choice = input("\nВведите номер операции:\n> ")

        if choice == "1":
            add_category()
        elif choice == "2":
            delete_category()
        elif choice == "3":
            view_categories()
        elif choice == "4":
            add_record()
        elif choice == "5":
            delete_record()
        elif choice == "6":
            view_records()
        elif choice == "7":
            filter_records()
        elif choice == "8":
            calculate_balance()
        elif choice == "9":
            analyze_expenses()
        elif choice == "10":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор.")

if __name__ == "__main__":
    main()