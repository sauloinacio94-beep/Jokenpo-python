import random
opcoes = ['1', '2', '3']
escolhaJ = input('Escolha 1-pedra, 2-papel ou 3-tesoura: ')
escolhaC= random.choice(opcoes)
print(f"O computador escolheu: {escolhaC}")

if escolhaJ == '1' and escolhaC == '3':
    print('Você ganhou.')
elif escolhaJ == '2' and escolhaC == '1':
    print('Você ganhou.')
elif escolhaJ == '3' and escolhaC == '2':
    print('Você ganhou')
elif escolhaJ == escolhaC:
    print('Parece que empatamos.')
else:
    print('Você perdeu.')