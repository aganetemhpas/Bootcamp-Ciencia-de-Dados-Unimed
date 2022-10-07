# WHILE

opcao = -1

while opcao != 0:
    opcao=int(input('[1] Sacar \n[2] Sair \n[0] Sair: '))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo extrato...')

# WHILE COM ELSE
opcao = -1

while opcao != 0:
    opcao = int(input('[1] Sacar \n[2] Sair \n[0] Sair: '))

    if opcao == 1:
        print('Sacando...')
    elif opcao == 2:
        print('Exibindo extrato...')
else:
    print('Obrigado e volte logo.')