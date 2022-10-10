# Maiúscula, minúscula e título
curso = 'pYtHon'
curso_maiusculo = curso.upper()
curso_minusculo = curso.lower()
curso_titulo = curso.title()
print(curso_maiusculo, curso_minusculo, curso_titulo)

# Removendo espaços em branco
curso = '      Python  '
remove_espacos_todos = curso.strip()
remove_espacos_esquerda = curso.lstrip()
remove_espacos_direita = curso.rstrip()
print(remove_espacos_todos, remove_espacos_esquerda, remove_espacos_direita)

# Junção e Centralização
curso = 'Python'
centralizado = curso.center(10, '#') # Total de caracter (geral), caracter desejado
juncao = ".".join(curso)
print(centralizado, juncao)

