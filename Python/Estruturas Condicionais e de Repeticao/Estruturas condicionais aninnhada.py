conta_normal = True
conta_universitaria = False

saldo = 2000
saque = float(input('Valor para saque: '))
cheque_especial = 420

if conta_normal:
    if saldo >= saque:
        print('Saque realizado com sucesso!')
    elif saque <= (saldo + cheque_especial):
        print('Saque reaizado com uso do cheque especial!')
    else:
        print('Não foi possivel realizar saque, saldo insuficiente.')