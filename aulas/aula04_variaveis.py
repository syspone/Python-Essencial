# =============================================================================
# Autor.........: Cristian Matias de Souza
# Cargo/Nível...: Analista de Dados (N3)
# Criado em.....: 19/10/2026 06:39
# Versão........: 1.0
# -----------------------------------------------------------------------------
# Descrição.....: Variaveis e Constantes
# Dependências..: Python 3.14
# =============================================================================


# Variaveis de texto
print('==== Variaveis de texto ====')
texto = 'Curso de Python'
print(texto)
print(type(texto))

print('\n')

# Número armazenado como texto (string numérica)
print('==== Número armazenado como texto (string numérica) ====')
varNumero = '100'
print(varNumero)
print(type(varNumero))

print('\n')

# Conversao de texto para numero inteiro
print('==== Conversao de texto para numero inteiro ====')
numero = int(varNumero)
print(numero)
print(type(numero))

print('\n')

# Variaveis para tipos numeros
print('==== Variaveis para tipos numeros ====')
varA = 99
varB = 4.56789
varC = False
varD = 2 + 9j
varE = 'Python'

print(varA, varB, varC, varD, varE)
print(type(varA))
print(type(varB))
print(type(varC))
print(type(varD))
print(type(varE))
print()

# Conversao de Tipos
print('==== Conversao de Tipos ====')
varF = float(varA)
print('Float de varF:', type(varF))
print()

varG = int(varB)
print(f'Conversao de varB para int: {varG}', type(varG))
print()

# Variaveis Booleanas
print('==== Variaveis Booleanas ====')
varH = False
varI = True
varJ = not (False)
varK = not (True)
print(varH, varI, varJ, varK)
