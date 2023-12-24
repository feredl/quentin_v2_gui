""" Quentin method facade class """

from data import Data
from triplet import CharacteristicZero, Lesson
from adjacency_matrix import AdjacencyMatrix
from reduced_matrix import ReducedMatrix
from stemma import Stemma

from itertools import permutations

class Quentin: 

    def __init__(self, path : str, skip_zeros : bool):
        self.data = Data(path)
        self.skip_zeros = skip_zeros
        self.ch_zeros = self.get_ch_zeros()
        self.adj_m = self.get_adj_m()
        self.reduced_m = self.get_reduced_m()
        self.stemma = self.get_stemma()

    def get_ch_zeros(self):
        triplets = list(self.data.get_lessons_combinations())
        zeros = []
        for el in triplets:
            perm = list(permutations(el))
            p = perm[:len(perm)//2]
            for triplet_combination in p:
                l1 = triplet_combination[0]
                l2 = triplet_combination[1]
                l3 = triplet_combination[2]
                zero = CharacteristicZero(
                    Lesson(l1, self.data.dict[l1]), 
                    Lesson(l2, self.data.dict[l2]), 
                    Lesson(l3, self.data.dict[l3]), 
                    self.skip_zeros)
                if zero.intermediate is True:
                    zero_triplet = (zero.lesson1.name, zero.lesson2.name, zero.lesson3.name)
                    zeros.append(zero_triplet)
        return zeros

    def get_adj_m(self):
        return AdjacencyMatrix(self.ch_zeros)

    def get_reduced_m(self):
        return ReducedMatrix(self.ch_zeros)

    def get_stemma(self):
        return Stemma(self.reduced_m.df)

    def show_stemma(self):
        return self.stemma.vizualize()

""" quentin_vergiliana = Quentin("qent.xlsx", skip_zeros = True)
print(*quentin_vergiliana.get_ch_zeros())
print(quentin_vergiliana.get_adj_m())
print(quentin_vergiliana.get_reduced_m())
quentin_vergiliana.show_stemma() """