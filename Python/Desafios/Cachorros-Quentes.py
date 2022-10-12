# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
valores = input().split() 

# TODO:  Calcule a média de cachorros quentes consumidas por participante e imprima o valor com DUAS casas decimais

total_participantes = int(valores[0])
total_hotdog = int(valores[1])

if ((total_hotdog >= 1 and total_participantes <= 10000) ):
    
    numero_medio_cachorro_quente = total_hotdog / total_participantes
    numero_medio_cachorro_quente = round(numero_medio_cachorro_quente,2)
    print(f"{numero_medio_cachorro_quente:.2f}")