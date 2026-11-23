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
print('==== Encontrando o raio ====\n')

# Importando bibliotecas

import math as m

varNome = input('Digite seu nome: ')
print('olá ', varNome + '!\n')

print('Calcular a área de uma circuferencia\n')

varRaio = int(input('Digite o raio: '))  # convertendo o input para int
vaResultadoArea = m.pi * (varRaio**2)

print(f'Área é {vaResultadoArea}')
print('Comprimento:', 2 * m.pi * varRaio)


print('\n')
print('==== Encontrando temperatura em Fahrenheit a partir de Celsius ====\n')

varTempCelsius = float(input('Digite a temperatura em Celsius: '))
varResultado = (varTempCelsius * 1.8) + 32
print(f'A temperatura em Fahrenheit é {varResultado}')


# Metodos Format
print('\n')
print('==== Metodo Format ====\n')

varTexto = '{0}, Seja bem-vindo(a)!'
print(varTexto.format(varNome))
print()

varIdade = 51
varProfissao = 'Analista de Suporte e Desenvolvimento'
varTexto = '{0}, seja bem-vindo(a)! \nIdade: {1} \nProfissão: {2}'
print(varTexto.format(varNome, varIdade, varProfissao))
print()


# Formatar o resultado
print('\n')
print('==== Formatar o resultado ====\n')

varResultado = m.pi * float(varRaio) ** 2
print('Área:', varResultado)
print('Comprimento:', 2 * m.pi * float(varRaio))
print()

Res_Final = 'Área: {0:.1f}°C'
print(Res_Final.format(varResultado))
print()