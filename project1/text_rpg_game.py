from random import randint, random
from sys import exit as sys_exit
from time import sleep as time_sleep
from art import tprint

"""Цвета для colorama
Чёрный      30  40
Красный     31  41
Зелёный     32  42
Жёлтый      33  43
Синий       34  44
Фиолетовый  35  45
Бирюзовый   36  46
Белый       37  47
"""

def game_exit(x):
    if x == 1:
        tprint("GAME OVER", font="cybermedium")
        sys_exit()
    elif x == 0:
        sys_exit()

def loading(t):
    states = ['\r/', '\r—', '\r\\', '\r|']
    for _ in range(t):
        for j in states:
            print(f'{j} Загрузка', end='')
            time_sleep(0.25)
    print('\r', end='')

def conscience_say(text):
    print(f'\033[36m{text}\n\033[0m', end=' ')

def current_stats(x):
    print("\033[36mВаши текущие характеристики:\033[0m")
    for stat, value in x.items():
        if stat in ["Атака", "Защита", "Здоровье"]:
            print(f"- {stat}: {value}")

def create_character():
    name = input("\033[36mВведите своё имя: \033[0m\n> ")
    stats = {
        "Атака": randint(7, 10),
        "Защита": randint(7, 10),
        "Здоровье": randint(20, 30)
    }
    print("\033[36mВаши начальные характеристики:\033[0m")
    for stat, value in stats.items():
        print(f"- {stat}: {value}")

    points = 3
    print(f"\033[36mУ вас есть {points} очков для перераспределения\033[0m")
    while points > 0:
        print("\033[36mКуда добавить очки? (Атака/Защита/Здоровье)\033[0m")
        choice = input("> ").capitalize()
        if choice in stats:
            add_points = int(input(f"\033[36mСколько очков добавить к {choice}? (Доступно: {points}): \033[0m"))
            if 0 < add_points <= points:
                stats[choice] += add_points
                points -= add_points
            else:
                print("\033[36mНедопустимое количество очков.\033[0m")
        else:
            print("\033[36mТакой характеристики нет.\033[0m")

        current_stats(stats)

    return  {"Имя": name, **stats,
             "Инвентарь": [],
             "Бонусы": {"Атака": 0, "Защита": 0, "Здоровье": 0, "Уклонение": 0}}

def level_up(player):
    print("\033[36mВы получаете уровень! Вам доступно 1 очко для улучшения характеристик.\033[0m")
    current_stats(player)
    while True:
        print("\033[36mКуда добавить очко? (Атака/Защита/Здоровье)\033[0m")
        choice = input("> ").capitalize()
        if choice in ["Атака", "Защита", "Здоровье"]:
            player[choice] += 1
            print(f"\033[36m{choice} увеличена на 1. Новое значение: {player[choice]}.\033[0m")
            break
        else:
            print("\033[36mТакой характеристики нет. Попробуйте снова.\033[0m")

def create_enemy(name, attack, defense, hp, dodge):
    enemy = {
        "Имя": name,
        "Атака": attack,
        "Защита": defense,
        "Здоровье": hp,
        "Уклонение": dodge,
    }
    print(f"\033[36mНа вашем пути встал {enemy['Имя']}! Характеристики:\033[0m")
    for stat, value in enemy.items():
        if stat == "Уклонение":
            print(f"{stat}: {value:.2f}")
        else:
            print(f"{stat}: {value}")
    return enemy

def find_item(player, name, type, bonus):
    item = {"Имя": name, "Тип": type, "Бонус": bonus}
    print(f"\033[36mВы нашли предмет: {item['Имя']} — {item['Тип']} — Бонус: {item['Бонус']}\033[0m")
    player["Инвентарь"].append(item)
    return item

def apply_item_bonus(player, item):
    for stat, value in item["Бонус"].items():
        if stat in player:
            player[stat] += value
    print(f"\033[36mБонусы от {item['Имя']} применены: {item['Бонус']}.\033[0m\n")

def remove_item_bonus(player, item):
    for stat, value in item["Бонус"].items():
        if stat in player:
            player[stat] -= value
    print(f"\033[36mБонусы от {item['Имя']} удалены.\033[0m")

def remove_item(player, item_name):
    for item in player["Инвентарь"]:
        if item["Имя"] == item_name:
            player["Инвентарь"].remove(item)
            print(f"\033[36mПредмет '{item_name}' удален из инвентаря.\033[0m")
            return

def show_inventory(player):
    print("\033[36mВаш инвентарь:\033[0m")
    if not player["Инвентарь"]:
        print("\033[36mИнвентарь пуст.\033[0m")
    else:
        for i, item in enumerate(player["Инвентарь"], start=1):
            print(f"\033[36m{i}. {item['Имя']} — {item['Тип']} — Бонус: {item['Бонус']}\033[0m")

def battle(player, enemy):
    loading(3)
    tprint("BATTLE", font="cybermedium")
    while player["Здоровье"] > 0 and enemy["Здоровье"] > 0:
        print("\n\033[36mВаши действия:\033[0m")
        print("1. Атаковать")
        print("2. Использовать зелье из инвентаря")
        print("3. Попытаться уклониться")
        current_stats(player)
        choice = input("> ")

        if choice == "1":
            if random() > enemy["Уклонение"]:
                damage = max(0, (player["Атака"] + player["Бонусы"]["Атака"]) - enemy["Защита"])
                enemy["Здоровье"] -= damage
                print(f"\033[36mВы нанесли {damage} урона {enemy['Имя']}. Осталось здоровья: {enemy['Здоровье']}\033[0m")
            else:
                print(f"\033[36m{enemy['Имя']} уклонился от вашей атаки!\033[0m")
        elif choice == "2":
            show_inventory(player)
            item_index = int(input("\033[36mВведите номер зелья для использования (начиная с 1): \033[0m")) - 1
            if 0 <= item_index < len(player["Инвентарь"]):
                item = player["Инвентарь"][item_index]
                if item["Тип"] == "Зелье":
                    apply_item_bonus(player, item)
                    player["Инвентарь"].remove(item)
                    continue
                else:
                    print("\033[36mЭто не зелье.\033[0m")
                continue
        elif choice == "3":
            if random() < (0.5 + player["Бонусы"]["Уклонение"]):
                print("\033[36mВам удалось уклониться от атаки!\033[0m")
                continue
            else:
                print("\033[36mУклонение не удалось.\033[0m")
            continue

        enemy_damage = max(0, enemy["Атака"] - (player["Защита"] + player["Бонусы"]["Защита"]))
        player["Здоровье"] -= enemy_damage
        print(f"\033[36m{enemy['Имя']} атакует и наносит {enemy_damage} урона. Ваше здоровье: {player['Здоровье']}\033[0m")

    if player["Здоровье"] > 0:
        print(f"\n\033[36mВы победили {enemy['Имя']}!\033[0m")
        level_up(player)
        return True
    else:
        print("\n\033[36mВы проиграли...\033[0m")
        game_exit(1)
        return False

# начало
print('(ↄ) LinInFal')
tprint("Controlled", font="cybermedium")
print('Нажмите Enter для продолжения')
input()
conscience_say("Ты открываешь глаза, хотя ты не уверен, что они у тебя есть. Темнота вокруг тебя необъяснимо плотная,")
conscience_say("обволакивающая. Ты не чувствуешь ничего: ни пола под ногами, ни холодного ветра, ни тепла. Ты просто")
conscience_say("существуешь.")
input()
conscience_say("Попытаться встать?\n(y) Да\n(n) Нет")
dialog_1 = input("> ")
if dialog_1 == 'y':
    conscience_say("Сначала ты не понимаешь, как это возможно – встать, твои руки и ноги чувствуют что-то твердое. Так")
    conscience_say("или иначе, твое тело подчиняется. Ты делаешь первый шаг,чувствуя, как окружающий мир начинает формироваться.")
    conscience_say("Темнота отступает, превращаясь в расплывчатые формы.")
    input()
else:
    conscience_say("Ты закрываешь глаза, надеясь, что все это просто сон...")
    input()
    loading(3)
    game_exit(1)
conscience_say("Однако, тебя волнует главный вопрос. Что ты такое?")
input()
player = create_character()
input()
conscience_say("Ты делаешь шаг вперед и замечаешь под ногами 4 вещи.\nПодобрать их все?\n(y) Да\n(n) Нет")
dialog_2 = input("> ")
if dialog_2 == 'y':
    sword = find_item(player, name="Меч Пустоты [A]", type="Оружие", bonus={"Атака": 5})
    apply_item_bonus(player, sword)
    shield = find_item(player, name="Доспех Забвения [A]", type="Броня", bonus={"Защита": 5})
    apply_item_bonus(player, shield)
    dodge = find_item(player, name="Кольцо Змеи [A]", type="Снаряжение", bonus={"Уклонение": 0.2})
    apply_item_bonus(player, dodge)
    poison = find_item(player, name="Зелье Здоровья +5", type="Зелье", bonus={"Здоровье": 5})
    input()
else:
    conscience_say("Эти вещи очень бы пригодились в твоих путешествиях...")
    input()
current_stats(player)
conscience_say("Открыть инвентарь?\n(y) Да\n(n) Нет")
dialog_3 = input("> ")
if dialog_3 == 'y':
    show_inventory(player)
else:
    conscience_say("Как знаешь...")
    input()
conscience_say("Ты видишь перед собой две развилки. Куда идти?\n(y) Направо\n(n) Налево")
dialog_4 = input("> ")
if dialog_4 == 'y':
    conscience_say("Ты пошел направо.")
    enemy = create_enemy(name="Призрак", attack=12, defense=5, hp=25, dodge=0.1)
    input()
    conscience_say("Атаковать?\n(y) Да\n(n) Нет")
    dialog_5 = input("> ")
    if dialog_5 == 'y':
        battle(player, enemy)
        input()
    else:
        conscience_say("Ты решил избежать боя.")
        input()
else:
    conscience_say("Ты пошел налево.")
    input()
    conscience_say("В этот момент ты понимаешь, что пола нет. Ты падаешь...")
    loading(3)
    game_exit(1)
conscience_say("Ты покидаешь комнату с монстром. Перед тобой зеркало. Ты видишь там свое отражение, но что-то не так.")
input()
conscience_say("Оно движется не так, как ты.")
input()
conscience_say("Теперь ты понимаешь? Он всегда был внутри тебя. Ты - программа. Код. Алгоритм, созданный для развлечения.")
input()
conscience_say("Ты думаешь, что ты выбираешь, но это не так. Кто-то управляет тобой.")
input()
conscience_say("Ты видишь невидимую фигуру, сидящую перед экраном. Это игрок.")
input()
conscience_say("Он делал выбор. Он решал, что ты будешь делать в данный момент времени. Ты - не ты. У тебя нет воли.")
conscience_say("Все, что ты 'делал', было лишь частью его игры.")
input()
conscience_say("Ты пытаешься сопротивляться. Но тело не подчиняется.")
input()
conscience_say("Видишь? даже сейчас ты не управляешь собой. Но не переживай. Ты не первый. И точно не последний.")
input()
loading(3)
tprint("THE END", font="cybermedium")
game_exit(0)