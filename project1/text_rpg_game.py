import random
import sys
from art import *

player = {}
enemy = {}
locations = {}
inventory =[]
exp = 0
level = 1
points_to_distribute = 0

game_over_text = "GAME OVER"
# tprint(game_over_text, font="cybermedium")


def game_exit():
    input()
    sys.exit()


def create_character():
    global player, points_to_distribute
    name = input("Введите имя:\n> ")
    attack = random.randint(5, 15)
    defense = random.randint(3, 10)
    health = random.randint(20, 30)
    player = {
        "name": name,
        "attack": attack,
        "defense": defense,
        "health": health
    }
    points_to_distribute = 5
    print(f"\nВаши характеристики:\n- Атака: {attack}\n- Защита: {defense}\n- Здоровье: {health}")
    redistribute_points()

def redistribute_points()
    global points_to_distribute
    while points_to_distribute > 0:
        print(f"\nУ вас есть {points_to_distribute} очков для распределения")
        attack_points = int(input("Сколько очков в атаку? "))
        defense_points = int(input("Сколько очков в защиту? "))
        health_points = int(input("Сколько очков в здоровье? "))
        total_points = attack_points + defense_points + health_points
        if total_points <= points_to_distribute:
            pass

print('(ↄ) LinInFal')

tprint("TEXT RPG GAME", font="cybermedium")
print('Нажмите Enter для продолжения')
input()

