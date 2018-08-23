qnt = int(input('Quantas linhas vai ter sua matriz? '))
cont = 0
matriz = []
lista = []
while cont<qnt:
	linha = list(map(int,input('Digite todos os numeros da linha separados com um espaço em branco: ').split()))
	matriz.append(linha)
	cont +=1

for i in range(len(matriz)):
	temp = []
	for j in range(len(matriz[i])):
		temp.append(matriz[j][i])
	lista.append(temp)
print(lista)