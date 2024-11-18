print('teste')

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math

varA = np.arange(1,11)
varB = np.arange(-10,0)
varc = np.arange(0,100,10)


def converter(reais) :
    dolar = (reais / 4.11)
    return dolar 

valor = converter(100)
print(f'seu valor em reais é {valor}')

%## function testing 

def comparar(a,b):
    if a > b :
        print(f'{a} é maior')
    else:
        print(f'{b} é maior ')

print(comparar(10,5))



def comparar2(a,b):
    if a > b :
        return a
    else:
        return b

maior = comparar2(100,5)

print(f'o parâmetro {maior} é maior ')


