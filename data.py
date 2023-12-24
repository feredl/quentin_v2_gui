""" Classification input """

import re 
from itertools import combinations
import pandas as pd

class Data:

    def __init__(self, path, df = None):
        self._path = path
        self.df = self.variant_df(path)
        self.dict = self.df.to_dict('index')

    @property
    def file_path(self):
        return self._path
    
    @file_path.setter
    def file_path(self, path):
        try:
            bool(re.search(".xlsx|.xls", path, )) is True
        except:
            print("Wrong file path!")
        else: 
            self._path = path

    def variant_df(self, path):
        df = pd.DataFrame(pd.read_excel(path, header = None, index_col=0))
        df.index.name=None
        return df 
    
    def get_lessons_list(self):
        return list(self.df.index.values)
    
    def get_lessons_combinations(self):
        return list(combinations(list(self.df.index.values), 3))