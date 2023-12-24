""" Classes for multiple triplet representations of Quentin's method """

from collections import namedtuple
import unittest

class Lesson():
    def __init__(self, name: str, variants: dict):
        self.name = name 
        self.variants = variants #variant position : encoded reading

    def get_readings(self):
        return list(self.variants.values()) #row values of excel


Triplet = namedtuple('Triplet',
                      ['lesson1', 'lesson2', 'lesson3']
                      )

class CharacteristicZero(Triplet):
    def __new__(cls, lesson1, lesson2, lesson3, skip_zeros: bool, intermediate = None):
        self = super(CharacteristicZero, cls).__new__(cls, lesson1, lesson2, lesson3)
        self.skip_zeros = skip_zeros
        self.intermediate = self.check()
        return self
   
    def __repr__(self):
        return f"{self.lesson1.name} > {self.lesson2.name} < {self.lesson3.name}"
   
    def __common_readings(self):        
        l1 = self.lesson1.get_readings() #row values of excel
        l3 = self.lesson3.get_readings()
        flag = False
        for i in range(len(l1)):
            if l1[i] == l3[i]:
                flag = True
                continue
        return flag
    
    def __intermediate(self):
        lesson1 = self.lesson1.get_readings()
        possible_intermediate_lesson = self.lesson2.get_readings()
        lesson3 = self.lesson3.get_readings()
        triplet_values = list(zip(lesson1, lesson3, possible_intermediate_lesson))
        if self.skip_zeros:
            for el in triplet_values:
                if (el[0] == el[1] and el[0] != el[2] and el[2] != 0 and el[1] != 0):
                    return False
        if not self.skip_zeros:
            for el in triplet_values:
                if (el[0] == el[1] and el[0] != el[2]):
                    return False
        return True

    def check(self):
        if self.__intermediate() and self.__common_readings():
            return True
        return False

""" a = "A"
values = {1: 0, 2: 1, 3:4}

b = "B"
values1 = {1: 1, 2: 1, 3:4}

c = "C"
values2 = {1: 2, 2: 1, 3:4}

Lesson1 = Lesson(a, values)
Lesson2 = Lesson(b, values1)
Lesson3 = Lesson(c, values2)

tr = CharacteristicZero(Lesson1, Lesson2, Lesson3, True)

print(tr.intermediate) """
