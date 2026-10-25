# =============================================================================
# Autor.........: Cristian Matias de Souza
# Cargo/Nível...: Analista de Dados (N3)
# Empresa.......: syspone
# Criado em.....: 24/10/2026 14:48
# Versão........: 1.0
# -----------------------------------------------------------------------------
# Descrição.....: Exercício da aula sobre métodos
# Dependências..: Python 3.14
# =============================================================================

print(type('texto'))
print('texto de exemplo'.capitalize())

print('==== Concatenação de textos ====')
textoA = 'Curso'
textoB = 'Python'
textoC = 'Cristian'
resultado = textoC + ' ' + textoA + ' de ' + textoB + '.'
# metodos
print(resultado.upper())                                        # maiúsculo
print(resultado.lower())                                        # minúsculo
print(resultado.title())                                        # cada palavra em maiúsculo
print(resultado.capitalize())                                   # só a primeira letra em maiúsculo
print(resultado.swapcase())                                     # inverte maiúsculo e minúsculo
print(len(resultado))                                           # tamanho da string
print('\n')

print('==== Busca e Contagem ====')
frase = "O python é uma linguagem de programação multiparadigma, orientada a objetos e interpretada. O Python é uma linguagem de programação muito popular."
print(frase.count('Python'))                                    # conta quantas vezes a palavra 'Python' aparece na frase
print(frase.find('programação'))                                # encontra a posição da primeira ocorrência da palavra 'programação'
print(frase.replace('Python', 'Java'))                          # substitui todas as ocorrências da palavra 'Python' por 'Java'
print(frase.replace('Python', 'Java', 1))                       # substitui apenas a primeira ocorrência da palavra 'Python' por 'Java'

print('\n')

print('==== Divisão ====')
data = '24/10/2026'
print(data.split('/'))                                          # divide a string em uma lista de strings

varA, varB = 99, 199
print('Resultado ' +  str(varA + varB))
print()

print('\n')

print('==== Preenchimento de caracteres de Strings=====')
varTexto = 'Curso de Python Cristian'
print(varTexto.ljust(50, '*'))                                   # preenche com asteriscos à direita
print(varTexto.rjust(50, '*'))                                   # preenche com asteriscos à esquerda
print(varTexto.center(50, '*'))                                  # preenche com asteriscos ao centro

print('==== Extração de Texto (Slicing) ====')
print(varTexto[0])                                              # extrai o primeiro caractere
print(varTexto[0:5])                                            # extrai os 5 primeiros caracteres
print(varTexto[-1])                                             # extrai o último caractere
print(len(varTexto[0:5]))                                       # tamanho da string

print('\n')

print('===== Eliminar espaços em branco =====')
varTexto = '   Curso de Python Cristian   '

# Antes da limpeza: os colchetes mostram onde o texto começa e termina
print('Tamanho antes da limpeza:', len(varTexto))
print(f'[{varTexto}]')

# strip() devolve um texto NOVO sem os espaços do início e do fim.
# Guardamos esse texto numa variável, porque a original não muda.
varTextoLimpo = varTexto.strip()

print('Tamanho depois da limpeza:', len(varTextoLimpo))
print(f'[{varTextoLimpo}]')

# Bônus: as outras variações
print(f'lstrip (só à esquerda): [{varTexto.lstrip()}]')
print(f'rstrip (só à direita):  [{varTexto.rstrip()}]')


print('===== Eliminar caracteres específicos =====')
varTexto = 'Curso de Python Cristian'
print(varTexto.replace('Python', 'Java'))                           # substitui todas as ocorrências da palavra 'Python' por 'Java'


