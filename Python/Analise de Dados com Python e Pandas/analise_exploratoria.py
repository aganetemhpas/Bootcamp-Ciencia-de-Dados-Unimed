# -*- coding: utf-8 -*-
"""Analise Exploratoria.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IkwmTCyyHZBr4tiHoLMeFf7JbXGvtEtq
"""

#Imprtando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

#Upload do arquivo
from google.colab import files
arq = files.upload()

#Criando nosso DataFrame
df = pd.read_excel('AdventureWorks.xlsx')

#Visualizando as 5 primeiras linas
df.head()

#Quantidade de Linhas e Colunas
df.shape

#Verificando os Tipos de dados
df.dtypes

#Qual a Receita Total?
df['Valor Venda'].sum()

#Qual o Custo Total?
df['Custo'] = df['Custo Unitário'].mul(df['Quantidade']) # Criando coluna custo

df.head(1)

#Agora que temos a receita e o custo total, podemos achar o lucro total
#Vamos criar uma coluna de Lucro que será Receita - Custo
df['Lucro'] = df['Valor Venda'] - df['Custo']

df.head(1)

#Total de Lucro
round(df['Lucro'].sum(), 2)

#Criando uma coluna com total de Dias para enviar o produto
df['Tempo de Envio'] = df['Data Envio'] - df['Data Venda']

df.head(2)

"""####Agora, queremos saber a média do tempo de envio para cada marca, e para isso precisamos transformar a coluna Tempo_envio em númerica"""

df.dtypes

#Extraindo apenas dias
df['Tempo de Envio'] = (df['Data Envio'] - df['Data Venda']).dt.days

#Verificando o tipo da coluna Tempo de Envio
df['Tempo de Envio'].dtypes

#Média de tempo de envio por Marca
df.groupby('Marca')['Tempo de Envio'].mean()

"""###Verificar Volores Ausentes"""

df.isnull().sum()

"""### E, se quiser saber o Lucro por Ano e por Marca?"""

#Vamos agrupar por Ano e Marca
df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum()

pd.options.display.float_format = '{:20,.2f}'.format # Formatação para FLOAT

#Resetando o Index
lucro_ano = df.groupby([df['Data Venda'].dt.year, 'Marca'])['Lucro'].sum().reset_index()
lucro_ano

#Qual o total de produtos vendidos?
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=False)

#Gráfico Total de Produtos Vendidos
df.groupby('Produto')['Quantidade'].sum().sort_values(ascending=True).plot.barh(title='Total Produtos Vendidos')
plt.xlabel('Ano')
plt.ylabel('Receita');

#Lucro por Ano
df.groupby(df['Data Venda'].dt.year)['Lucro'].sum().plot.bar(title='Lucro x Ano')
plt.xlabel('Ano')
plt.ylabel('Receita');

#Lucro por Ano
df.groupby(df['Data Venda'].dt.year)['Lucro'].sum()

#Selecionando apenas as vendas de 2009
df_2009 = df[df['Data Venda'].dt.year == 2009]

df_2009.head(4)

#Grafico Lucro por Mes
df_2009.groupby(df['Data Venda'].dt.month)['Lucro'].sum().plot(title='Lucro x Mes')
plt.xlabel('Mes')
plt.ylabel('Lucro');

#Grafico Lucro por Marca
df_2009.groupby('Marca')['Lucro'].sum().plot.bar(title='Lucro x Marca')
plt.xlabel('Mes')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal');

#Grafico Lucro por Classe
df_2009.groupby('Classe')['Lucro'].sum().plot.bar(title='Lucro x Classe')
plt.xlabel('Classe')
plt.ylabel('Lucro')
plt.xticks(rotation='horizontal');

df['Tempo de Envio'].describe()

#Gráfico de Boxplot
plt.boxplot(df['Tempo de Envio']);

#Histograma
plt.hist([df['Tempo de Envio']]);

#Tempo Minino de Envio
df['Tempo de Envio'].min()

#Tempo Maximo de Envio
df['Tempo de Envio'].max()

#Identificar a Linha do Máximo
df[df['Tempo de Envio'] == 20]

#Salvando em CSV
df.to_csv('df_vendas_novo.csv', index=False)
