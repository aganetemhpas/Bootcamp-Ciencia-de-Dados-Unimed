# -*- coding: utf-8 -*-
"""Estrutura de Dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1rnHQbA_jg5xGmj4yRkPPgAzb9vDAOPg3

#Listas
"""

animais = [1,2,3]
animais

animais = ['cachorro', 'gato', 123, 4]
animais

#Imprimindo o primeiro elemento da lista
animais[0]

#Imprimindo o quarto elemento da lista
animais[3]

#Substituindo o primeiro elemento
animais[0] = 'Macaco'
animais

#Remove elemento
animais.remove(123)
animais

#Tamanho da lista
len(animais)

#verifica elemento pertecente a lista
'gato' in animais

#Adicionar elemento
animais.append('Leao')
animais

#Adicionar mais de um elemento de uma vez
animais.extend(['Cobra', 4])
animais

lista = [500, 40, 60, 2, 10]

#Maior elemento
max(lista)

#Minimo
min(lista)

#Ordenar lista do menor para o maior
lista.sort()
lista

"""#Tuplas"""

#Tuplas são imutaveis
tp = ('Banana', 'Maça', 8, 50)

#Retornando o primeiro elemento
tp[0]

tp.count(9)

tp[0:2]

"""#Dicionarios"""

dc = {'Maça': 20, 'Banana': 10, 'Uva': 5} #Dicionarios trabalham com o conceito de CHAVE e VALOR

dc

#Acessando o VALOR atravez da CHAVE
dc['Maça']

#Atualizando o valor de Maça
dc['Maça'] = 25
dc

#Retornando todas as CHAVES do dicionario
dc.keys()

#Retornando todas as VALORES do dicionario
dc.values()

#Verificando se já existe uma chava no dicionario e caso nao exista inserir
dc.setdefault('Limao',22)
dc

dc.setdefault('Maça', 24)
dc

