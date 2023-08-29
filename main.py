def main():
    media = dict()

    media['nome'] = str(input('Nome: '))
    media['media'] = float(input('Média: '))
    if media['media'] >= 7:
        media['situação'] = 'Aprovado'
    elif media['media'] >= 5:
        media['situação'] = 'Recuperação'
    else:
        media['situação'] = 'Reprovado'
    print('-=' * 30)
    for k, v in media.items():
        print(f' - {k} é igual a {v}')

main()

while True:
    opcao = input('Deseja continuar? [S/N] ').upper()
    if opcao == 'N':
        break
    elif opcao == 'S':
        main()
    else:
        print('Opção inválida')
