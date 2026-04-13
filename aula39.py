"""
Iterando strings com while
"""
#       012345678910
#nome = 'Luiz Otávio'  # Iteráveis
#      1110987654321
nome = input('Digite seu nome: ')
tamanho_nome = len(nome)
indice = 0
novo_nome =''
while indice < tamanho_nome:
    letra = nome[indice]
    novo_nome += f'*{letra}'
    indice += 1

novo_nome += '*'
print(novo_nome)