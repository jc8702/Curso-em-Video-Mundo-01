# Exercício Python #003 - Somando dois números
#Crie um programaque leia dois númerose mostre a soma entre eles

if __name__ == '__main__':
    n1 = int(input("Digite um valor:"))
    n2 = int(input('Digite outro valor:'))
    s = n1 + n2
    print('A soma entre {} e {} é igual a {}!'.format(n1, n2, s))