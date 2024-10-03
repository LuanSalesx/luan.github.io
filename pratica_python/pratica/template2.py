'''frase_palavra = input("Digite uma frase ou palavra: ")
palavra_antiga = input("Digite a palavra a ser substituída: ")
palavra_nova = input("Digite a nova palavra: ")
frase_palavra = frase_palavra.replace(palavra_antiga, palavra_nova)'''

lista1 = [20, 40, 30, 10]
print("Lista 1:", lista1)
lista2 = lista1
print("Lista 2:", lista2)
lista1[0] = 50
print("Lista 1:", lista1)
print("Lista 2:", lista2)
lista2.append(60)
print("Lista 1:", lista1)
print("Lista 2:", lista2)