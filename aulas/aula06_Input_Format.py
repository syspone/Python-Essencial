# =============================================================================
# Autor.........: Cristian Matias de Souza
# Cargo/Nível...: Analista de Dados (N3)
# Empresa.......: syspone
# Criado em.....: 22/11/2026 16:09
# Versão........: 1.0
# -----------------------------------------------------------------------------
# Descrição.....: Input para obter dados
# Dependências..: Python 3.14
# =============================================================================

print('\n')
print('==== Calcula a área e o comprimento de uma circunferência a partir do raio ====\n')

# Importando bibliotecas

import math as m

varNome = input('Digite seu nome: ')
print('olá ', varNome + '!\n')

print('Calcular a área de uma circuferencia\n')

varRaio = int(input('Digite o raio: '))             # convertendo o input para int
vaResultadoArea = m.pi * (varRaio ** 2)

print(f'Área é {vaResultadoArea}' )
print('Comprimento:', 2 * m.pi * varRaio)
