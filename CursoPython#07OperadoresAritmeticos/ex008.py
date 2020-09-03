# Exercício Python #008 - Conversor de Medidas
# Escreva um programa  que leia um valor em metros e o exiba convertido em centimetros e milímetros:

if __name__ == '__main__':
    n = float(input('Uma distância em metros: '))
    cm = n * 100
    mm = n * 1000
    print('O valor informado {} m, corresponde a {} cm e {} mm'.format(n, cm, mm))