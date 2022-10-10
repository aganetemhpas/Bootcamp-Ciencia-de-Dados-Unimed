
nome = 'Matheus'
idade = 28
profissao = 'Analista de Dados'
linguagem = 'Python'

# Old style %
print('Olá, me chamo %s. Eu tenho %d anos de idade, trabalho com %s e estou matriculado no curso de %s.' % (nome, idade, profissao, linguagem))

# Metodo format
print('Olá, me chamo {}. Eu tenho {} anos de idade, trabalho com {} e estou matriculado no curso de {}.' .format(nome, idade, profissao, linguagem))

print('Olá, me chamo {3}. Eu tenho {2} anos de idade, trabalho com {1} e estou matriculado no curso de {0}.' .format(linguagem, profissao, idade, nome))

print('Olá, me chamo {n}. Eu tenho {i} anos de idade, trabalho com {p} e estou matriculado no curso de {l}.' .format(n=nome, i=idade, p=profissao, l=linguagem))

dados = {'n': 'Matheus', 'i': 28, 'p': 'Analista de Dados', 'l': 'Python'}
print('-Olá, me chamo {n}. Eu tenho {i} anos de idade, trabalho com {p} e estou matriculado no curso de {l}.' .format(**dados)) # **dados é um dicionario

# F-String
print(f'Olá, me chamo {nome}. Eu tenho {idade} anos de idade, trabalho com {profissao} e estou matriculado no curso de {linguagem}.')

PI = 3.14159
print(f'O Valor de PI: {PI:.2f}') # duas casas decimais

print(f'O Valor de PI: {PI:10.2f}') # 10 é o numero de espaços em branco