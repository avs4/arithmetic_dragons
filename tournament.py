# coding: utf-8
# license: GPLv3
from gameunit import *
from random import randint, choice

class Enemy(Attacker):
    pass


def generate_random_enemy():
    RandomEnemyType = choice(enemy_types)
    enemy = RandomEnemyType()
    return enemy


def generate_dragon_list(enemy_number):
    enemy_list = [generate_random_enemy() for i in range(enemy_number)]
    return enemy_list


class Dragon(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer


class GreenDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'зелёный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '+' + str(y)
        self.set_answer(x + y)
        return self.__quest

class RedDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'красный'

    def question(self):
        x = randint(1,100)
        y = randint(1,100)
        self.__quest = str(x) + '-' + str(y)
        self.set_answer(x - y)
        return self.__quest

class BlackDragon(Dragon):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._color = 'чёрный'

    def question(self):
        x = randint(1,100)
        y = randint(1,10)
        self.__quest = str(x) + '*' + str(y)
        self.set_answer(x * y)
        return self.__quest

class Troll(Enemy):
    def set_answer(self, answer):
        self.__answer = answer

    def check_answer(self, answer):
        return answer == self.__answer

'''class U_troll(Troll):
    def __init__(self):
        self._health = 50
        self._attack = 10
        self._type='U'

    def question(self):
        x = randint(1,5)
        self.__quest = 'x in range(5) = ?'
        self.set_answer(x)
        return self.__quest

class P_troll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._type='P'

    def question(self):
        x = randint(1,100)
        self.__quest = str(x)
        Q=0
        if x>1:
            for i in range(2,x,1):
                if x%i==0:
                    Q=1
                    break
        self.set_answer(Q)
        return self.__quest'''

class M_troll(Troll):
    def __init__(self):
        self._health = 200
        self._attack = 10
        self._type='M'

    def question(self):
        x = randint(1,50)
        self.__quest = str(x)
        C=[]
        i=2
        x=int(input())
        while i<=x:
            if x%i==0:
                C=C+[i]
                x=x/i
                i=2
            else:
                i+=1
        S=''
        for i in range(len(C)):
            S=S+str(C[i])
        R=int(S)
        self.set_answer(R)
        return self.__quest

#enemy_types = [GreenDragon, RedDragon, BlackDragon]
enemy_types = [M_troll]
