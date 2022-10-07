from xml.etree.ElementInclude import LimitedRecursiveIncludeError


# Oculpa a mesma região de memoria

curso = "Curso de Python"
nome_curso = curso
saldo, limite = 200, 200

print(curso is nome_curso)

print(curso is not nome_curso)

print(saldo is limite)