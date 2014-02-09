import random

# Definições.
ARQUIVO_DE_SAIDA = "SQL Gerado/Telefone.sql"
NUMERO_DE_CONTATOS = 200;

# Variável de controle do id dos telefones.
__idTelefone = 1 # Primeiro id.

# Retorna o próximo id de telefone.
def nextIdTelefone():
	global __idTelefone
	id = __idTelefone
	__idTelefone += 1
	return id;

def telefoneFixoAleatorio():
	# DDD
	telefone = "(0"
	telefone += random.choice("123456789")
	telefone += random.choice("123456789")
	telefone += ") "

	# Número
	telefone += "3"
	telefone += random.choice("0123456789")
	telefone += random.choice("0123456789")
	telefone += random.choice("0123456789")
	telefone += "-"
	telefone += random.choice("0123456789")
	telefone += random.choice("0123456789")
	telefone += random.choice("0123456789")
	telefone += random.choice("0123456789")
	return telefone



def insert():
	# Este id será usado tanto para a chave primária, e a chave estrangeira
	# para a tabela de contatos. Assim haverá apenas um telefone para cada
	# contato.
	id = str(nextIdTelefone())

	sql = "INSERT INTO Telefone(id, numero, Contato_id)\n"
	sql +="VALUES (" + id + ", '" + telefoneFixoAleatorio() + "', " + id + ");\n"
	return sql

# Dá uma nova seed ao random.
random.seed()

# Abre o arquivo onde será escrito o SQL.
with open(ARQUIVO_DE_SAIDA, "w") as arqSaida:
	# Coloca um cabeçalho para o arquivo.
	arqSaida.write("-- Popula a tabela Telefone.\n\n")

	# Escreve todas as queries para um arquivo.
	for x in range(NUMERO_DE_CONTATOS):
		arqSaida.write(insert() + "\n")