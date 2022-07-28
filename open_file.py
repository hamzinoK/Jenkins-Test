import os  

def read_txt(file):
    if file.endswith('.txt'):
        f = open(file, 'r')
        df = print(f.read())
    else:
        raise ValueError(f'Unsupported filetype: {file}')
    return df



read_txt('random.txt')


# import numpy as np
# import pandas as pd
# df = pd.read_csv(file, header = None, sep = '\t')



