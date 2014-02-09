## Junta os dois arquivos de nomes de frutas.

with open('frutas1.txt', "r") as frutas1:
	frutas = frutas1.readlines()

with open('frutas2.txt', "r") as frutas2:
	frutas += frutas2.readlines()

# Limpa as quebras de linhas nos nomes das frutas.
for i in range(len(frutas)):
	frutas[i] = frutas[i].strip()

# Converte a lista para um set. Deixando apenas nomes idênticos.
frutas = set(frutas)

# Grava o arquivo com as frutas sem repetição.
with open('Nomes de Frutas.txt', "w") as frutasFile:
	for fruta in frutas:
		frutasFile.write(fruta + "\n")
