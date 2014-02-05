#!/usr/bin/python3

# Importações.
import random

# Definições.
ARQUIVO_DE_MODELOS = "Dados/modelos.txt"
ARQUIVO_DE_SAIDA = "SQL Gerado/veiculo.sql"

# Funções.
# Retorna um modelo de veículo aleatório.
def modeloAleatorio( modelos ):
	return random.choice(modelos)

# Retorna uma placa aleatória.
def placaAleatoria():
	placa = ""

	# Anexa letras a placa.
	for i in range(3):
		placa += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

	# Anexa o hífen.
	placa += "-"

	# Anexa os números a placa.
	for i in range(4):
		placa += random.choice("0123456789")

	return placa

# Lê os modelos do arquivo e os retorna.
def lerModelos():
	with open(ARQUIVO_DE_MODELOS, "r") as arqModelos:
		# Lê todas as linhas do arquivo.
		modelos = arqModelos.readlines()

		# Limpa os caracteres de quebra de linha e espaços.
		for i in range(len(modelos)):
			modelos[i] = modelos[i].strip()

		return modelos

modelos = lerModelos()

# Gera uma query sql para inserir um veiculo aleatório na tabela de
# veículos.
def insertVeiculoAleatorio():
	sql = "INSERT INTO veiculo(placa, modelo)\n"
	sql +="VALUES ('" + placaAleatoria() + "', '" + modeloAleatorio(modelos) + "');\n"
	return sql

# Dá uma nova seed ao random.
random.seed()

# Escreve todas as queries para um arquivo.
with open(ARQUIVO_DE_SAIDA, "w") as arqSaida:
	for x in range(100):
		arqSaida.write(insertVeiculoAleatorio() + "\n")