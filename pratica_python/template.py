# programa que realiza a contagem de 20 segundos
import time
contagem_regressiva = 20
while contagem_regressiva > 0:
    print(f'Tempo restante: {contagem_regressiva}s')
    contagem_regressiva -= 1
    time.sleep(1)  # Aguarda 1 segundo
print('Tempo esgotado!')
print("FIM DO 1º PROGRAMA")



# programa que lê um valor de início e valor de fim, imprimindo na saída os valores do intervalo.
inicio = int(input('Digite o valor de início: '))
fim = int(input('Digite o valor de fim: '))
while inicio <= fim:
    print(inicio)
    inicio += 1
print("FIM DO 2º PROGRAMA")



# Programa que realiza a contagem de 1 até 100
# Apenas números impares
# Ao final exiba o total de números impares e a soma de todos eles
contagem_impares = 0
soma_impares = 0
for n in range(1, 101):
    if n % 2 != 0:
        print(n)
        contagem_impares += 1
        soma_impares += n
print(f"Total de números ímpares encontrados: {contagem_impares}")
print(f"Soma de todos os números ímpares: {soma_impares}")
print("FIM DO 3º PROGRAMA")
