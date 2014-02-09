# Importações.
import random

# Definições.
ARQUIVO_DE_SAIDA = "SQL Gerado/VeiculoTipoCarga.sql"
NUMERO_DE_VEICULOS = 100
NUMERO_DE_TIPOS = 10
NUMERO_MAXIMO_DE_TIPOS_POR_VEICULO = 3

# Variável de incremento dos veículos
__idVeiculo = 1

def idTipoCargaAleatorio():
	return random.randint(1, NUMERO_DE_TIPOS)

def nextVeiculo():
	global __idVeiculo
	id = int(__idVeiculo) # Faz uma cópia, ao invés de ligar os objetos.
	__idVeiculo += 1
	return id

def insert( Veiculo_id, TipoCarga_id ):
	sql = "INSERT INTO VeiculoTipoCarga(Veiculo_id, TipoCarga_id)\n"
	sql +="VALUES (" + str(Veiculo_id) + ", " + str(TipoCarga_id) + ");\n"
	return sql

# Dá uma nova seed ao random.
random.seed()

# Escreve todas as queries para um arquivo.
with open(ARQUIVO_DE_SAIDA, "w") as arqSaida:
	# Imprime cabeçalho do arquivo
	arqSaida.write("-- Popula a tabela VeiculoTipoCarga.\n\n")

	for x in range(NUMERO_DE_VEICULOS):
		idVeiculo = nextVeiculo()

		# Gambiarra muito loca para que não se repitam tipos por veiculo.
		numeroPequenoAleatorio = random.randint(1, 8)
		
		# Repete aleatóriamente, inserindo, TALVEZ, mais de um tipo por veículo.
		for y in range(random.randint(1, NUMERO_MAXIMO_DE_TIPOS_POR_VEICULO)):
			# Gambiarra muito loca para que não se repitam tipos por veiculo.
			idTipoCarga = numeroPequenoAleatorio + y
			
			# Escreve no arquivo
			arqSaida.write(insert(idVeiculo, idTipoCarga) + "\n")
