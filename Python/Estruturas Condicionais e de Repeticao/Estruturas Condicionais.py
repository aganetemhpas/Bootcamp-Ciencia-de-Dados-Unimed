# if
saldo = 2000
saque = float(input('Informe o valor do saque: '))

if saldo >= saque:
    print('Realizando saque!')

if saldo < saque:
    print('Saldo insuficiente')

# if - else
if saldo >= saque:
    print('Realizando saque!')
else:
    print('Saldo insuficiente')

# if/ elif/ else
opcao = int(input('Informe uma opcao: [1] Sacar \n[2] Extrato: '))

if opcao == 1:
    valor = float(input('Informe o valor do saque: '))
elif opcao == 2:
    print('Exibindo o extrato...')
else:
    #sys.exist('Opcao invalida')
    print('Opcao invalida')

