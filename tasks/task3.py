
import random

class Gamer:
    def __init__(self, name, game, description):
        self.name = name
        self.game = game
        self.description = description

    def play(self):
        return input()

class Game:

    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)


    def __init__(self, size=3):

        if size < 2:
            raise "Некорректная размерность поля"
        self.size = size
        self.pole = list()
        self.gamer_x = None
        self.gamer_o = None
        self.current_gamer = None

        self.init_pole()

    def init_gamer(self, description):
        name_gamer = input("Введите имя: ")
        return Gamer(name_gamer, self, description)

    def init_pole(self):
        self.pole = [[None for _1 in range(self.size)] for _ in range(self.size)]

    @classmethod
    def tern90(cls, matrix):
        result_matrix = cls.transpose(matrix)
        result_matrix = result_matrix[::-1]
        return result_matrix

    @classmethod
    def transpose(cls, matrix):
        res = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return res

    def pole_is_full(self):
        for i in self.pole:
            for j in i:
                if j is None:
                    return False
        return True

    def print_pole(self):
        for i in range(len(self.pole)):
            for j in range(len(self.pole[i])):
                if self.pole[i][j] is None:
                    print(str((i * self.size + 1) + j).ljust(3), end=" ")
                else:
                    print(self.pole[i][j].description.ljust(3), end = " ")
            print()

    def get_winer(self):
        for i in range(self.size):
            if self.pole[i][0] is None:
                continue
            if all(c == self.pole[i][0] for c in self.pole[i]):
                return self.pole[i][0]

        copy_pole = self.pole.copy()
        copy_pole = self.tern90(copy_pole)

        for i in range(len(copy_pole)):
            if copy_pole[i][0] is None:
                continue
            if all(c == copy_pole[i][0] for c in copy_pole[i]):
                return copy_pole[i][0]

        if self.pole[0][0] is not None:
            if all(self.pole[0][0] == self.pole[i][i] for i in range(len(self.pole))):
                return self.pole[0][0]

        if self.pole[0][-1] is not None:
            if all(self.pole[0][-1] == self.pole[i][-1 - i] for i in range(len(self.pole))):
                return self.pole[0][0]

        return None

    def step_is_correct(self, num):
        try:
            num = int(num)
        except:
            return False

        if num > self.size ** 2:
            return False

        coordinats = ((num - 1) // (self.size), (num - 1) % (self.size))

        if self.pole[coordinats[0]][coordinats[1]] is not None:
            return False

        return True

    def set_value(self, num, gamer):
        coordinats = ((num - 1) // (self.size), (num - 1) % (self.size))
        self.pole[coordinats[0]][coordinats[1]] = gamer

    def start(self):
        if self.gamer_x is None:
            self.gamer_x = self.init_gamer("x")
        if self.gamer_o is None:
            self.gamer_o = self.init_gamer("o")
        gamers = (self.gamer_x, self.gamer_o)
        self.current_gamer = random.choice(gamers)

        winer = None
        self.print_pole()
        while winer is None and not self.pole_is_full():

            print(f"Ход игрока {self.current_gamer.name}")

            num = self.current_gamer.play()
            if not self.step_is_correct(num):
                print("Некорректное значение")
                continue
            num = int(num)
            self.set_value(num, self.current_gamer)
            self.print_pole()
            winer = self.get_winer()
            if not self.pole_is_full() or winer is None:
                self.current_gamer = gamers[0] if gamers[0] != self.current_gamer else gamers[1]

        if winer is not None:
            print(f"Выйграл игрок {winer.name}")
        else:
            print("Ничья")

def task3():
    game = Game()
    game.start()

task3()