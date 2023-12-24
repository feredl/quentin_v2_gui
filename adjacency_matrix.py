""" Adjacency matrix class """

import numpy as np
import pandas as pd

class AdjacencyMatrix():

    def __init__(self, ch_zeros : list, df = None):
        self.ch_zeros = ch_zeros
        self.df = self.fill() #list of 3-tuples

    def __repr__(self):
        return repr(self.df)

    def empty_df(self):
        sorted_unique_lessons = sorted(list(set([lesson for x in self.ch_zeros for lesson in x])))
        amount = len(sorted_unique_lessons)
        empty_mtrx = np.zeros(shape=(amount, amount))
        adj_mtrx = pd.DataFrame(empty_mtrx, index = sorted_unique_lessons, columns = sorted_unique_lessons)
        return adj_mtrx
    
    def fill(self):
        adj_mtrx_df = self.empty_df()
        for el in self.ch_zeros:
            adj_mtrx_df.loc[el[0], el[1]] = 1
            adj_mtrx_df.loc[el[1], el[0]] = 1 
            adj_mtrx_df.loc[el[1], el[2]] = 1
            adj_mtrx_df.loc[el[2], el[1]] = 1 
        return adj_mtrx_df