# senha = '1234'
# senha_digitada = ''
# repeticoes = 0

# while senha_digitada != senha:
#     senha_digitada = input(f'Sua senha ({repeticoes}x): ')

#     repeticoes += 1

# print(repeticoes)
# print('aquele laço acima pode ter repetições infinitas')
texto = 'python'

novo_texto = ''
for letra in texto: # for = cada
    novo_texto += f'*{letra}'
    print(letra)

print(novo_texto + '*')