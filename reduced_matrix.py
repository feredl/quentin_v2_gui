""" Reduced matrix class"""

from adjacency_matrix import AdjacencyMatrix

class ReducedMatrix(AdjacencyMatrix):
    
    def __init__(self, ch_zeros, df = None):
        super().__init__(ch_zeros)
        self.df = self.reduce()

    def __repr__(self):
        return repr(self.df)

    def reduction_check(self):
        deuces = []
        for el in self.ch_zeros:
            deuces.append((el[0], el[1]))
            deuces.append((el[1], el[2]))
        deuces = list(set(deuces))
        return deuces

    def reduce(self):
        deuces = self.reduction_check()
        for el_d in deuces:
            for el_t in self.ch_zeros:
                if(el_d[0] == el_t[0] and el_d[1] == el_t[2] or el_d[0] == el_t[2] and el_d[1] == el_t[0]):
                    self.df.loc[el_d[0], el_d[1]] = 0.0
                    self.df.loc[el_d[1], el_d[0]] = 0.0
        return self.df
        
""" zeros = [Triplet('G', 'H', 'AR'), Triplet('G', 'RO','H'), Triplet('G', 'RO', 'AR'), Triplet('AR', 'H', 'RO')]

adj = ReducedMatrix(zeros)
print(adj)
 """