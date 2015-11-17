# coding: utf-8
# license: GPLv3
from gameunit import *

class Hero(Attacker):
    _health = 100
    _attack = 50
    _experience=0
    _name=''
    def __init__(self,_name):
        self._name=_name
