"""
Faça um jogo para o usuário adivinhar qual
a palavra secreta.
- Você vai propor uma palavra secreta
qualquer e vai dar a possibilidade para
o usuário digitar apenas uma letra.
- Quando o usuário digitar uma letra, você 
vai conferir se a letra digitada está
na palavra secreta.
    - Se a letra digitada estiver na
    palavra secreta; exiba a letra;
    - Se a letra digitada não estiver
    na palavra secreta; exiba *.
Faça a contagem de tentativas do seu
usuário.
"""
import os

palavra_secreta = 'python'
palavra_secreta = palavra_secreta.lower()
tentativas = 0
palavra_formatada = '******'
i = 0

while True:

    letra = input('Digite uma letra: ').strip().lower()
    if len(letra) > 1:
        print('Digite apenas uma letra!')
        continue
    if letra == '':
        print('Digite uma letra!')
        continue

    tentativas+= 1

    novo_progresso = ''

    for i in range(len(palavra_secreta)):
        if palavra_secreta[i] == letra or palavra_formatada[i] != '*':
            novo_progresso += palavra_secreta[i] 
        else:
            novo_progresso += '*'

    palavra_formatada = novo_progresso
    print(palavra_formatada)

    if palavra_formatada == palavra_secreta:
        os.system('cls')
        print(f'Parabéns! Você acertou a palavra em {tentativas} tentativas.')
        break

