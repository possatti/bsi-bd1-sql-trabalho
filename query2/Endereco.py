import random

# Definições.
ARQUIVO_DE_NOMES_DE_BAIRROS = "Dados/Nomes de Frutas.txt"
ARQUIVO_DE_SAIDA = "SQL Gerado/Endereco.sql"
NUMERO_DE_CONTATOS = 200;

# Variável de controle da seleção de bairros.
__numeroBairro = 0 # Primeiro índice da lista.

# Variável de controle do id dos telefones.
__idEndereco = 1 # Primeiro id.

# Retorna o próximo id de endereco.
def nextIdEndereco():
	global __idEndereco
	id = __idEndereco
	__idEndereco += 1
	return id;

def cepAleatorio():
	cep = ""
	cep += random.choice("0123456789")
	cep += random.choice("0123456789")
	cep += random.choice("0123456789")
	cep += random.choice("0123456789")
	cep += random.choice("0123456789")
	cep += "-"
	cep += random.choice("0123456789")
	cep += random.choice("0123456789")
	cep += random.choice("0123456789")
	return cep

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


def insert( bairros ):
	# Este id será usado tanto para a chave primária, e a chave estrangeira
	# para a tabela de contatos. Assim haverá apenas um endereço para cada
	# contato.
	id = str(nextIdEndereco())

	"31173-053", "Smallville", "Street 1"
	sql = "INSERT INTO Endereco(id, cep, bairro, rua, Contato_id)\n"
	sql +="VALUES (" + id
	sql +=", '" + cepAleatorio() + "'"
	sql +=", '" + bairroSequencial(bairros) + "'"
	sql +=", '" + ruaAleatoria() + "'"
	sql +=", " + id + ");\n"
	return sql

# Carrega os nomes de bairros.
bairros = []
with open(ARQUIVO_DE_NOMES_DE_BAIRROS, "r") as arqBairros:
	bairros = arqBairros.readlines()

# Limpa as quebras de linhas nos nomes dos bairros.
for i in range(len(bairros)):
	bairros[i] = bairros[i].strip()

# Dá uma nova seed ao random.
random.seed()

# Abre o arquivo onde será escrito o SQL.
with open(ARQUIVO_DE_SAIDA, "w") as arqSaida:
	# Coloca um cabeçalho para o arquivo.
	arqSaida.write("-- Popula a tabela Endereco.\n\n")

	# Escreve todas as queries para um arquivo.
	for x in range(NUMERO_DE_CONTATOS):
		arqSaida.write(insert(bairros) + "\n")