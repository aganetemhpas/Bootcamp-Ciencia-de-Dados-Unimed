# Exemplo sem repetição para adicionar 2 numeros a frente
num = int(input('Infome um número inteiro: '))
print(num)
num += 1
print(num)
num += 1
print(num)

# Estrutura FOR
texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='-')

# Estrutura FOR/ELSE
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='-')
else:
    print('Executa no final do laço')
