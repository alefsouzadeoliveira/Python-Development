

 

# A manipulação dos dados consiste em organizar variáveis e observações
# Na grande maioria dos casos, as bases de dados precisam ser preparadas

# Vamos utilizar a base de dados com notas do PISA (Programa Internacional de Avaliação de Alunos)
# Fonte: https://pisadataexplorer.oecd.org/ide/idepisa/report.aspx

pisa = pd.read_csv("(2) notas_pisa.csv", delimiter=",")

#%% Visualizar os dados

# Vamos olhar apenas a parte inicial do banco de dados (5 primeiras linhas)

print(pisa.head(5))

#%% Variáveis do dataset

# Quais são os nomes das variáveis disponíveis?

print(pisa.columns)

#%% Detalhes das variáveis do dataset

# Informações mais detalhadas das variáveis do banco de dados

  
#%% Tamanho do banco de dados

# Quantas observações (linhas) existem no banco de dados

print(pisa.shape[0])

# Quantas variáveis (colunas) existem no banco de dados

print(pisa.shape[1])

# Quantas observações e variáveis existem no banco de dados

print(pisa.shape)

#%% Selecionando variáveis

# Vamos especificar nomes de variáveis do banco de dados

print(pisa['country'])

# Podemos armazenar a variável especificada em um novo objeto

paises_pisa = pisa['country']

print(pisa.iloc[0:5,0:2])
# Também poderíamos armazenar mais de uma variável em um novo objeto

print( pisa[[ 'reading_2018','country']])

#%% Removendo variáveis sem uso

# Por exemplo, supondo que não vamos avaliar as variáveis no ano de 2018

pisa_2022 = pisa.drop(columns=['mathematics_2018', 'reading_2018', 'science_2018'])
print(pisa_2022)
# O argumento inplace=True pode ser usado para reescrever o objeto existente

pisa_2022.drop(columns=['group'], inplace=True)


#%%

import pandas as pd
import numpy as np 

pisa = pd.read_csv('(2) notas_pisa.csv',delimiter = ',')
print(pisa)

# transformando colunas texto em numero 

pisa['mathematics_2022'] = pd.to_numeric(pisa['mathematics_2022'], errors='coerce')
pisa['reading_2022']     = pd.to_numeric(pisa['reading_2022']    , errors = 'coerce')
pisa['science_2022']     = pd.to_numeric(pisa['science_2022']    , errors = 'coerce')
pisa['mathematics_2018'] = pd.to_numeric(pisa['mathematics_2018'], errors='coerce')
pisa['reading_2018']     = pd.to_numeric(pisa['reading_2018']    , errors = 'coerce')
pisa['science_2018']     = pd.to_numeric(pisa['science_2018']    , errors = 'coerce')

print(pisa.info())

qtd = pisa['group'].count()



clear()
#%% little teste
pisa_math = pisa['mathematics_2022']

pisa.extend(pisa_math)

pisa_math = pd.DataFrame(pisa_math)

pisanovo = pd.concat([pisa,pisa_math],axis=1)


pisanovo = pisanovo.drop(['mathematics_2022'],axis = 1)
#%% Removendo um objeto do ambiente

# Para remover um objeto do ambiente, pode ser feito da seguinte forma

del pisa_reading_2018

#%% Identificando elementos específicos por posição

# O primeiro argumento é o número da linha (index)
# O segundo argumento é a posição da coluna

# Nota: tanto o index quanto as colunas começam contagem do zero no pandas

# Qual é a nota de matemática em 2022 para o Brasil?

print(pisa.iloc[46, 2])

#%% Identificando uma observação completa por posição

# Quais são os valores de todas as variáveis para o Japão?

print(pisa.iloc[19,])

#%% Identificando algumas observações completas por posição

# Quais são os valores de todas as variáveis para os países de index de 0 a 6?

print(pisa.iloc[0:7, ])

# É necessário adicionar uma posição a mais no final!

#%% Identificando variáveis específicas por posição

# Selecionar as variáveis que estão nas posições 0, 2 e 5

pisa_matematica = pisa.iloc[:, [0,2,5]]

# Selecionar as variáveis que estão nas posições de 0 até 2

pisa_matematica = pisa.iloc[:, 0:3]

# Aqui é necessário adicionar uma posição a mais no final!

#%% Reorganizando a posição das variáveis

# Vamos selecionar algumas variáveis e trocar a ordem delas

pisa_2022_ajuste = pisa.reindex(['group','country', 'science_2022', 'mathematics_2022', 'reading_2022'], axis=1)

#%% Excluindo algumas observações com base no index

# Supondo que não vamos analisar os países de index 38 até 95

pisa_ocde = pisa.drop(pisa.index[38:96])

# Lembrando de adicionar uma posição a mais no final

#%% Detalhando as manipulações de dados

# O banco de dados em análise tem um problema:
# As variáveis de notas, que deveriam ser métricas, estão como textos "object"

# Ajustando variáveis:
# Neste caso, utilizaremos a função "to_numeric"
# Os missings serão ajustados pelo coerce e serão substituídos por nan

pisa['mathematics_2022'] = pd.to_numeric(pisa['mathematics_2022'], errors='coerce')
pisa['reading_2022'] = pd.to_numeric(pisa['reading_2022'], errors='coerce')
pisa['science_2022'] = pd.to_numeric(pisa['science_2022'], errors='coerce')

pisa['mathematics_2018'] = pd.to_numeric(pisa['mathematics_2018'], errors='coerce')
pisa['reading_2018'] = pd.to_numeric(pisa['reading_2018'], errors='coerce')
pisa['science_2018'] = pd.to_numeric(pisa['science_2018'], errors='coerce')

print(pisa.info())

#%% Excluindo linhas com dados faltantes

# É possível eliminar as observações que apresentem valores faltantes

pisa_na = pisa.dropna()

#%% Gerando estatísticas descritivas

# Tabela de estatísticas descritivas para variáveis quantitativas

pisa[['mathematics_2022', 'reading_2022', 'science_2022']].describe()

# Tabela de frequências para variável qualitativa

pisa['group'].value_counts()

pisa_na = pisa2 
del pisa2


# exclui a linha inteira  
pisa2 = pisa2.dropna()

del pisa_math

del new_pisa

#%%

pisa[['mathematics_2022','reading_2022','science_2022']].describe()

print( pisa_na['mathematics_2022'].mean())

brasil = pd.DataFrame(pisa.iloc[46,])
print(brasil)
#%% selecionando linhas baseado em argumentos,ao invés de index
print(pisa[pisa['mathematics_2022'] > 437])


print(pisa[pisa['group'] == 'OECD'])


#%% Filtrando observações por meio de operadores

# É possível filtrar observações por meio dos operadores:
# Alguns operadores úteis para realizar filtros:

# "== igual"
# "> maior"
# ">= maior ou igual"
# "< menor"
# "<= menor ou igual"
# "!= diferente"
# "& indica e"
# "| indica ou"

# Exemplos de filtros:

# Nota de matemática no ano de 2022 maior do que 437

print(pisa[pisa['mathematics_2022'] > 437])
acima_media_mat_2022 = pisa[pisa['mathematics_2022'] > 437] # salvando objeto

# Somente países no grupo da OECD

pisa[pisa['group'] == 'OECD']

# Países no grupo da OECD e com nota em ciências no ano de 2022 menor ou igual a 493

print(pisa[(pisa['group'] == 'OECD') & (pisa['science_2022'] <= 493)])

# Países que não sejam classificados no grupo da OECD

print(pisa[pisa['group'] != 'OECD'])

# Nota em leitura no ano de 2022 menor do que 386 ou maior do que 480

print(pisa[(pisa['reading_2022'] < 386) | (pisa['reading_2022'] > 480)])
extremos_leitura = (pisa[(pisa['reading_2022'] < 386) | (pisa['reading_2022'] > 480)])

#%% Agrupamento dos dados por algum critério

# Agrupando os dados pelo método groupby

pisa_grupo = pisa.groupby(by=['group'])
    

# O pisa_grupo está agrupado e não pode mais ser manipulado como antes
# As informações serão extraídas com base no critério de agrupamento

pisa_grupo.describe().T # o comando .T apenas fez a transposição da tabela

#%% Organizando o dataset com base em critérios

# É possível ordenar as observações com base nos valores das variáveis

# Em ordem decrescente

sort_matem = pisa.sort_values(by=['mathematics_2022'], ascending=False)

# Em ordem crescente

sort_ciencias = pisa.sort_values(by=['science_2022'], ascending=True)

#%% Também poderíamos alterar os nomes das variáveis

nomes = ["pais",
         "grupo",
         "matematica_2022",
         "leitura_2022",
         "ciencias_2022",
         "matematica_2018",
         "leitura_2018",
         "ciencias_2018"]

pisa.columns = nomes

print(pisa.info())

# Para trocar apenas um nome:

pisa = pisa.rename(columns={'grupo':'grupo_paises'})

print(pisa.info())

#%% Data Visualization

# Para a visualização de dados, vamos utilizar os seguintes pacotes:
# Se estiver utilizando pela primeira vez, executar as instalações:
!pip install matplotlib
!pip install seaborn
!pip install plotly

import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.io as pio
pio.renderers.default = 'browser'
import plotly.graph_objects as go

# Se estiver iniciando o Spyder, é importante carregar o pandas e o numpy

import pandas as pd
import numpy as np

#%% Gráfico de barras para contagem

# Para a análise, vamos importar o banco de dados de uma empresa comercial
# Fonte: adaptado de https://www.kaggle.com/datasets/apoorvaappz/global-super-store-dataset

comercio = pd.read_excel("(2) comercio_global.xlsx")

# Vamos iniciar por uma variável qualitativa, o mercado onde ocorreu a venda 
# Como é variável categórica, vamos criar um gráfico de contagem (countplot)
# Neste caso, o gráfico apresentará a contagem em cada categoria da variável

plt.figure(figsize=(15,9), dpi = 600)
sns.countplot(data=comercio, x="market")

# Podemos escolher a ordem de apresentação reorganizando os níveis da variável

plt.figure(figsize=(15,9), dpi = 600)
sns.countplot(data=comercio, x="market", order=["APAC", "LATAM", "EU", "US", "Africa", "EMEA", "Canada"])

# Vamos adicionar algumas formatações ao gráfico básico

plt.figure(figsize=(15,9), dpi = 600)
sns.countplot(data=comercio, x="market", order=["APAC", "LATAM", "EU", "US", "Africa", "EMEA", "Canada"])
plt.title("Análise por Mercado",fontsize=20)
plt.xlabel('Mercado',fontsize=15)
plt.ylabel('Conatgem',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Podemos trocar as cores das barras

plt.figure(figsize=(15,9), dpi = 600)
sns.countplot(data=comercio, x="market", order=["APAC", "LATAM", "EU", "US", "Africa", "EMEA", "Canada"], color="blue")
plt.title("Análise por Mercado",fontsize=20)
plt.xlabel('Mercado',fontsize=15)
plt.ylabel('Conatgem',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Conhecendo algumas paletas de cores do seaborn

# Paleta bright

palette = sns.color_palette("bright")
sns.palplot(palette)

# Paleta viridis

palette = sns.color_palette("viridis")
sns.palplot(palette)

# Paleta Paired

palette = sns.color_palette("Paired")
sns.palplot(palette)

# Paleta Rocket

palette = sns.color_palette("rocket")
sns.palplot(palette)

# Vamos alterar o tema do gráfico e adicionar as contagens

plt.figure(figsize=(15,9), dpi = 600)
ax = sns.countplot(data=comercio, x="market", hue="market", order=["APAC", "LATAM", "EU", "US", "Africa", "EMEA", "Canada"], palette='viridis', legend=False)
for container in ax.containers: ax.bar_label(container, fontsize=12)
plt.title("Análise por Mercado",fontsize=20)
plt.xlabel('Mercado',fontsize=15)
plt.ylabel('Conatgem',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Também poderíamos apresentar o gráfico com os eixos invertidos (var no Y)

plt.figure(figsize=(15,9), dpi = 600)
ax = sns.countplot(data=comercio, y="market", hue="market",
                   order = comercio['market'].value_counts(ascending=False).index,
                   palette = 'viridis', legend=False)
for container in ax.containers: ax.bar_label(container, padding=1, fontsize=12)
plt.title("Análise por Mercado",fontsize=20)
plt.xlabel('Contagem',fontsize=15)
plt.ylabel('Mercado',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% A seguir, podemos apresentar um gráfico de barras

# Vamos ajustar os dados de interesse gerando uma média por grupo

comercio_agrupado = comercio[['category', 'profit']].groupby(by=['category']).mean()
comercio_agrupado = comercio_agrupado.sort_values(by=['profit'], ascending=False).reset_index()

# Gerando o gráfico de barras

plt.figure(figsize=(15,9), dpi = 600)
ax1 = sns.barplot(data=comercio_agrupado, x='category', y='profit', hue='category', palette='rocket')
for container in ax1.containers: ax1.bar_label(container, fmt='%.2f', padding=3, fontsize=12)
plt.title("Lucro Médio por Categoria",fontsize=20)
plt.xlabel('Categorias',fontsize=15)
plt.ylabel('Lucro',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Gráfico de setores - pizza

# Gerando os dados de interesse
pizza = pd.crosstab(index = comercio['segment'], columns = 'segmento', normalize = True).sort_values('segmento', ascending = False)

# Plotando o gráfico
plt.figure(figsize=(15,9), dpi = 600)
plt.pie(pizza['segmento'], 
        labels = pizza.index, 
        colors = sns.color_palette('pastel'), 
        autopct='%.0f%%', # nº de casas decimais 
        textprops={'fontsize': 20}, # tamanho da fonte
        pctdistance = 0.6) # posição dos percentuais
plt.title('Análise por Segmento',fontsize=20)
plt.show()

#%% Histograma

# A seguir, vamos elaborar o histograma do valor das vendas

plt.figure(figsize=(15,9), dpi = 600)
sns.histplot(data=comercio, x="sales", bins=50)
plt.xlabel('Valor das Vendas',fontsize=15)
plt.ylabel('Frequência',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Visualizando apenas um trecho da distribuição da variável

hist_vendas = comercio[comercio['sales'] < 1000]

plt.figure(figsize=(15,9), dpi = 600)
sns.histplot(data=hist_vendas, x="sales", bins=30)
plt.xlabel('Valor das Vendas',fontsize=15)
plt.ylabel('Frequência',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Detalhando um pouco mais o gráfico

plt.figure(figsize=(15,9), dpi = 600)
ax2 = sns.histplot(data = hist_vendas, x = "sales", bins=range(0,1100,100), color='blue', alpha=0.6, kde=True)
ax2.bar_label(ax2.containers[0], fontsize=12)
plt.xlabel('Valor das Vendas',fontsize=15)
plt.xticks(ticks=np.arange(0,1100,100))
plt.ylabel('Frequência',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Gráfico de pontos (scatterplot)

# Vamos elaborar um gráfico de dispersão dos pontos
# Os dados são do atlas ambiental sobre distritos da cidade de São Paulo

atlas_ambiental = pd.read_excel("(2) atlas_ambiental.xlsx")

# Iniciando com o gráfico básico (scatterplot)
# Neste caso, devemos especificar as variáveis dos eixos x e y

plt.figure(figsize=(15,9), dpi = 600)
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade")

# Como há variáveis nos dois eixos, podemos adicionar outras variáveis:

# Na forma de tamanho dos pontos ("size")

plt.figure(figsize=(15,9), dpi = 600)
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade")
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Vamos criar uma nova variável indicando "favel" acima ou abaixo da média

print(atlas_ambiental['favel'].mean())

atlas_ambiental.loc[atlas_ambiental['favel']<5.93, "indica_favel"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental['favel']>=5.93, "indica_favel"] = "Acima"

# Vamos adicionar a variável que será indicada pela cor dos pontos ("hue")

plt.figure(figsize=(15,9), dpi = 600)
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade", hue="indica_favel")
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Vamos criar outra variável indicando "mortalidade" acima ou abaixo da média

print(atlas_ambiental['mortalidade'].mean())

atlas_ambiental.loc[atlas_ambiental['mortalidade'] < 15.99, "mort"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental['mortalidade'] >= 15.99, "mort"] = "Acima"

# Vamos adicionar a variável que será indicada pelo tipo dos pontos ("style")

plt.figure(figsize=(15,9), dpi = 600)
sns.scatterplot(data=atlas_ambiental, x="renda", y="escolaridade", size="idade", hue="indica_favel", style="mort")
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.legend(bbox_to_anchor=(1,1), fontsize=9)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

# Caso queira verificar graficamente o ajuste linear à nuvem de pontos

plt.figure(figsize=(15,9), dpi = 600)
sns.regplot(data=atlas_ambiental, x="renda", y="escolaridade", ci=None)
plt.title("Indicadores dos Distritos do Município de São Paulo",fontsize=20)
plt.xlabel('Renda',fontsize=15)
plt.ylabel('Escolaridade',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.show()

#%% Gráfico de linhas

# Vamos elaborar um gráfico de linhas (lineplot) para dados ao longo do tempo
# Vamos utilizar o banco de dados com as receitas de vendas das empresas

receita = pd.read_excel("(2) receita_empresas.xlsx")

# Como temos 5 empresas no banco de dados, vamos implementar o seguinte gráfico
# Vamos separar cada empresa por meio da cor da linha

plt.figure(figsize=(15,9), dpi = 600)
sns.lineplot(data=receita, x="ano", y="receita", hue="id_empresa")

# Vamos formatar um pouco mais o gráfico

plt.figure(figsize=(15,9), dpi = 600)
sns.lineplot(data=receita, x="ano", y="receita", hue="id_empresa", marker="o")
plt.title("Receita de Vendas",fontsize=20)
plt.xlabel('Ano',fontsize=15)
plt.ylabel('Receita Anual de Vendas',fontsize=15)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
plt.legend(title='Empresa', loc='upper left', fontsize=12)
plt.show()

# A seguir, vamos elaborar um gráfico interativo

# Elaborando o gráfico

fig_line = px.line(receita, 
                   x='ano', 
                   y='receita', 
                   color='id_empresa', 
                   markers=True, 
                   title='Receita de Vendas',
                   labels={"ano": "Ano",
                           "receita": "Receita Anual de Vendas",
                           "id_empresa": "Empresa"})

fig_line.show()

# Salvando a figura

fig_line.write_html('grafico_linhas.html')

#%% Gráfico de calor

# Vamos gerar um gráfico de calor que distingue informações por meio de cores
# O banco de dados contém informações sobre a quantidade vendida em 3 produtos

vendas_regional = pd.read_excel("(2) vendas_regiao.xlsx")

# Inicialmente, vamos selecionar as variáveis quantitativas do banco de dados

vendas_reg = vendas_regional[['produtoA','produtoB','produtoC']]

# Vamos gerar o gráfico de calor no contexto das correlações entre variáveis
# Portanto, primeiramente, vamos criar a matriz de correlações de Pearson
# Lembrando: selecionar apenas as variáveis quantitativas da base de dados

corr = vendas_reg.corr()

# Vamos elaborar um gráfico de calor (heatmap) com o plotly

fig_heat = go.Figure()

fig_heat.add_trace(
    go.Heatmap(
        x = corr.columns,
        y = corr.index,
        z = np.array(corr),
        text=corr.values,
        texttemplate='%{text:.2f}',
        colorscale='ice'))

fig_heat.update_layout(
    height = 600,
    width = 600)

fig_heat.show()

# Salvando a figura

fig_heat.write_html('grafico_calor.html')

# Algumas opções de colorscale:
    # solar
    # viridis
    # speed
    # blues
    # oranges

#%% Gráficos Boxplot

# O boxplot apresenta medidas de posição das variáveis
# Mínimo, máximo, 1º quartil, mediana e 3º quartil
# Vemos a distribuição dos dados nas variáveis e eventuais outliers univariados

# Inicialmente, vamos apresentar o boxplot de uma única variável

# Importando o banco de dados
vendas_regional = pd.read_excel("(2) vendas_regiao.xlsx")

plt.figure(figsize=(15,9), dpi = 600)
sns.boxplot(data=vendas_regional, y='produtoA', width = 0.5, color = "lightblue")
plt.xlabel('Produto A',fontsize=15)
plt.ylabel('Valores',fontsize=15)
plt.show()

# Poderíamos fazer vários boxplot em um mesmo gráfico

var_boxplot = vendas_regional[['produtoA', 'produtoB', 'produtoC']]

plt.figure(figsize=(15,9), dpi = 600)
sns.boxplot(data=var_boxplot, width = 0.6, palette='rocket')
plt.xlabel('Produtos',fontsize=15)
plt.ylabel('Valores',fontsize=15)
plt.show()

# Vamos torná-lo mais informativo

fig_box = px.box(var_boxplot,
                 width = 900)

fig_box.update_layout(title='BOXPLOT',
                      xaxis_title='Produtos',
                      yaxis_title='Valores',
                      plot_bgcolor='lightblue')

fig_box.show()

# Salvando a figura

fig_box.write_html('grafico_boxplot.html')

#%% Pairplot

# O pairplot permite analisar relações entre pares de variáveis
# O resultado é uma matriz de gráficos

# Importando o banco de dados

atlas_ambiental = pd.read_excel("(2) atlas_ambiental.xlsx")

sns.set(rc={"figure.dpi":600})
sns.pairplot(data=atlas_ambiental.iloc[:,[2,4,5]])

# Poderíamos adicionar uma variável categórica por meio de cores:

atlas_ambiental.loc[atlas_ambiental['mortalidade'] < 15.99, "mort"] = "Abaixo"
atlas_ambiental.loc[atlas_ambiental['mortalidade'] >= 15.99, "mort"] = "Acima"

sns.set(rc={"figure.dpi":600})
sns.pairplot(data=atlas_ambiental.iloc[:,[2,4,5,11]], hue='mort')
plt.savefig('grafico_pairplot.png')

#%% FIM!