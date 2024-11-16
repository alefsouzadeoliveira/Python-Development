

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


#%%
'''
dataset = pd.DataFrame(
    {
     'ID':[1,2,3,4],
     'AGE':[28,38,48,60]
     }
    
    )
'''


user  = pd.DataFrame(
    {
    'name':     ['alef','moritz','aaron'],
    'languages':[['R','Python','SQL','dax','M'],['Python','javascript'],['sql','javascrip']]
     }
    )

print(user)

user.describe()



varA = np.arange(1,11)
varB = np.arange(-10,0)
varc = np.arange(0,100,10)


print(varA)

print(varB)

print(varc)


table = pd.DataFrame({
    'varA':varA,
    'varB':varB,
    'varc':varc
    })


print('-' * 40)
print(table)
print('-' * 40)

#%% READING EXCEL

receita = pd.read_excel('(2) receita_empresas.xlsx')
print(receita)


receita_column = pd.DataFrame({'receita':receita.receita,'ano':receita.ano})

receita_column = pd.DataFrame({
    'company': receita.receita,
    'year': receita.ano
})



print(receita_column)
clear()

#%%  READING CSV and Excel 

fonte_notas = pd.read_csv('(2) notas_pisa.csv',sep=',',decimal = '.')

fonte  = pd.read_excel('(2) vendas_regiao.xlsx')

fonte_display = pd.DataFrame(fonte)

display(fonte_display)


#%%

ipca = pd.read_csv("https://api.bcb.gov.br/dados/serie/bcdata.sgs.433/dados?formato=csv&dataInicial=01/01/2022&dataFinal=30/09/2024", sep = ';',decimal = ",")

display(ipca)



ipca.to_csv("new_file.csv",index = True)

NewFileCsv = pd.read_csv('new_file.csv',sep = ',',decimal = ',')
display(NewFileCsv)

clear()

display(NewFileCsv)

#%% exporting to excel 

NewFileCsv.to_excel('new_file_excel.xlsx',index = False)



#%% testing


dicionario = {
    'varA':varA,
    'varb' :varB,
    'varc' : varB
    }


newtable = pd.DataFrame(dicionario)

newtable.to_excel('novatabela.xlsx',index = False)

