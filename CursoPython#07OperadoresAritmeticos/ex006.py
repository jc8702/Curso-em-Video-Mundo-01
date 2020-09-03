# Exercício Python #006 - Dobro, Triplo, Raiz Quadrada
# Crie um algorítimo que leia um número e mostre o seu drobro, o seu triplo e sua raiz quadrada.

if __name__ == '__main__':
    n = int(input('Digite um valor: '))
    dobro = n * 2
    triplo = n * 3
    raiz = n **(1/2)
    print('Analizando o número informado {}, o seu dobro é {}, o seu triplo é {} e a sua raiz quadrada é {}'.format(n, dobro, triplo, raiz))