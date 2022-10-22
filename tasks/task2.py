# 2 Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random

class Gamer:
    def __init__(self, name, game):
        self.name = name
        self.game = game

    def play(self):
        return input()

class Bot(Gamer):

    def play(self):
        if self.game.count <= self.game.max_step:
            return self.game.count
        if len(self.game.steps) == 0:
            current_step = self.game.count % (self.game.max_step + 1)
            if current_step < 1:
                return self.game.max_step
            else:
                return current_step
        else:
            return max(self.game.max_step + 1 - self.game.steps[-1], 1)

class Game:
    def __init__(self, count, max_step):
        self.steps = list()
        self.count = count
        self.max_step = max_step
        self.gamer1 = None
        self.gamer2 = None
        self.current_gamer = None

    def init_gamer(self):
        name_gamer = input("Введите имя: ")
        is_bot = None
        while type(is_bot) != bool:
            string = input(f"{name_gamer} будет ботом? yes/no: ")
            if string.lower() in ("no", "yes"):
                is_bot = string.lower() == "yes"
        if is_bot:
            return Bot(name_gamer, self)
        return Gamer(name_gamer, self)

    def step_is_correct(self, num):
        try:
            num = int(num)
        except:
            return False

        if num > self.count or num > self.max_step or num < 1:
            return False

        return True

    def start(self):
        if self.gamer1 is None:
            self.gamer1 = self.init_gamer()
        if self.gamer2 is None:
            self.gamer2 = self.init_gamer()

        gamers = (self.gamer1, self.gamer2)
        if self.current_gamer is None:
            self.current_gamer = random.choice([self.gamer1, self.gamer2])

        print("Для завершения напишите end")

        while self.count > 0:
            print(f"Остаток: {self.count}, Максимальный шаг: {self.max_step}. ход игрока {self.current_gamer.name}")
            num = self.current_gamer.play()

            if str(num).lower() == "end":
                print("Игра завершена")
                return

            if not self.step_is_correct(num):
                print(f"{num} - Не корректный ход")
                continue
            num = int(num)
            self.steps.append(num)
            print(f"Ход: {num}")
            self.count -= num
            if self.count > 0:
                self.current_gamer = gamers[0] if gamers[0] != self.current_gamer else gamers[1]

        print(f"Игрок {self.current_gamer.name} выйграл")


def task2():
    count = 2021
    step = 28
    game = Game(count, step)
    game.start()

task2()