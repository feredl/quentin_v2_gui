""" Class for undirected stemma """

import pandas as pd
import matplotlib.pyplot as plt
import networkx as nx

class Stemma:

    def __init__(self, reduced_matrix : pd.DataFrame, graph = None):
        self.reduced_matrix = reduced_matrix
        self.stemma = self.draw()

    def draw(self):
        return nx.from_pandas_adjacency(self.reduced_matrix)

    def vizualize(self):
        nx.draw(self.stemma, with_labels=True)
        plt.show()

    #TODO: visualize isolated lessons 
        #isolated_lessons = list(nx.isolates(G))

""" zeros = [('A', 'B', 'C'), ('A', 'D','F'), ('B', 'M', 'N')]

adj = ReducedMatrix(zeros)

stemma = Stemma(adj.reduced_df)
stemma.vizualize() """