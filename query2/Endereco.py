import random

# Definições.
ARQUIVO_DE_NOMES_DE_ESTADOS = "Dados/Nomes de Estados.txt"
ARQUIVO_DE_NOMES_DE_BAIRROS = "Dados/Nomes de Frutas.txt"
ARQUIVO_DE_SAIDA = "SQL Gerado/Endereco.sql"
NUMERO_DE_CONTATOS = 200;

# Variável de controle da seleção de bairros.
__numeroBairro = 0 # Primeiro índice da lista.

# Variável de controle do id dos telefones.
__idEndereco = 1 # Primeiro id.

# Variável que controla o incremento do cep.
__incrementoCep = 123 # Apenas para que tenha 3 digitos.

# Retorna o próximo id de endereco.
def nextIdEndereco():
	global __idEndereco
	id = __idEndereco
	__idEndereco += 1
	return id;

def cepAleatorioEUnico():
	cep = ""
	cep += random.choice("0123456789")

	# Digitos não aleatórios.
	global __incrementoCep
	digitosDoMeio = __incrementoCep
	__incrementoCep += 1
	cep += str(digitosDoMeio)

	cep += random.choice("0123456789")
	cep += "-"
	cep += random.choice("0123456789")
	cep += random.choice("0123456789")
	cep += random.choice("0123456789")
	return cep

def estadoAleatorio( estados ):
	return random.choice(estados)

def bairroSequencial( bairros ):
	global __numeroBairro
	bairro = bairros[__numeroBairro]
	__numeroBairro += 1
	return bairro

def ruaAleatoria():
	rua = "Rua "
	rua += random.choice("123456789")
	rua += random.choice("0123456789")
	return rua

def numeroAleatorio():
	numero = ""
	numero += random.choice("123456789")
	numero += random.choice("0123456789")
	return numero

def insert( estados, bairros ):
	sql = "INSERT INTO Endereco(id, cep, estado, bairro, rua, numero)\n"
	sql +="VALUES (" + str(nextIdEndereco())
	sql +=", '" + cepAleatorioEUnico() + "'"
	sql +=", '" + estadoAleatorio(estados) + "'"
	sql +=", '" + bairroSequencial(bairros) + "'"
	sql +=", '" + ruaAleatoria() + "'"
	sql +=", '" + numeroAleatorio() + "');\n"
	return sql

def lerLinhaPorLinha( caminho ):
	# Puxa cada linha para uma lista.
	with open(caminho, "r") as arq:
		linhas = arq.readlines()

	# Limpa as quebras de linhas nos nomes dos linhas.
	for i in range(len(linhas)):
		linhas[i] = linhas[i].strip()

	return linhas

# Carrega os nomes de bairros.
bairros = lerLinhaPorLinha(ARQUIVO_DE_NOMES_DE_BAIRROS)

# Carrega os nomes de estados.
estados = lerLinhaPorLinha(ARQUIVO_DE_NOMES_DE_ESTADOS)

# Dá uma nova seed ao random.
random.seed()

# Abre o arquivo onde será escrito o SQL.
with open(ARQUIVO_DE_SAIDA, "w") as arqSaida:
	# Coloca um cabeçalho para o arquivo.
	arqSaida.write("-- Popula a tabela Endereco.\n\n")

	# Escreve todas as queries para um arquivo.
	for x in range(NUMERO_DE_CONTATOS):
		arqSaida.write(insert(estados, bairros) + "\n")