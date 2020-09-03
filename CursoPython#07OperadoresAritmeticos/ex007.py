# Exercício Python #007 - Média Aritmética
# Desenvolva um programa que leia as duas notas de um aluno e calcule e mostre a sua média:

if __name__ == '__main__':
    nt1 = float(input('Digite a primeira nota: '))
    nt2 = float(input('Digite a segunda nota: '))
    media = (nt1 + nt2) / 2
    if media >= 7:
        print('Sua media é {}. Parabéns, você está aprovado. '.format(media))
    elif  media < 7:
        print("Sua media é {}. Que pena, estude mais!".format(media))