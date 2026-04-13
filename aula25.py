"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)
"""

nome = 'Luiz'
preco = 1000.95897643
variavel = '%s, o preço é R$%.2f' % (nome, preco)
print(variavel)
print('O Hexadecimal de %d é %04x' % (1500, 1500))
print(f'O preço é de {preco:.2f}')
print('O preço é de %.2f' % preco)