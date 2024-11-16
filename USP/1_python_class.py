

#%% Atividade nº 1


#%% Importando os pacotes

!pip install pandas
!pip install numpyII
!pip install matplotlib
!pip install seaborn
!pip install xlrd

#%% Aplicar funções que são frequentemente utilizadas na manipulação de dados
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import math


lista = [ 1,2,3,4]
#print(lista[0] + lista[3])

cores = pd.Series(['Vermelho','Amarelo','Azul','Verde','Roxo'])

print(cores)

 #%%  função contagem
print(len(cores))

# função arange

print(np.arange(1,10))

sequence = np.arange(0,10.5,0.5)
print(sequence)

