import random

# Definições.
ARQUIVO_DE_SAIDA = "SQL Gerado/Transporte.sql"
NUMERO_DE_SERVICOS = 100;
NUMERO_DE_MOTORISTAS = 100;
NUMERO_DE_TRANSPORTES = 200;

# Variável de controle do id dos serviços.
__idTransporte = 1 # Primeiro id.

# Retorna o próximo id de transporte.
def nextIdTransporte():
	global __idTransporte
	id = __idTransporte
	__idTransporte += 1
	return id;

def idServicoAleatorio():
	return random.randint(1, NUMERO_DE_SERVICOS)

def idMotoristaAleatorio():
	return random.randint(1, NUMERO_DE_MOTORISTAS)

def quantidadeAleatoria():
	quantidade = ""
	quantidade += random.choice("1123456789")
	quantidade += random.choice("0123456789")
	return quantidade

def dataIniciouAleatoria():
	data = "2012"

	# Mês
	data += "-"
	data += str(random.choice(range(1, 13)))

	# Dia
	data += "-"
	data += str(random.choice(range(1, 30)))
	
	# Hora
	data += " "
	data += str(random.choice(range(0, 24)))

	# Minutos
	data += ":"
	data += str(random.choice(range(0, 60)))

	return data

def dataTerminouAleatoria():
	data = "'2013"

	# Mês
	data += "-"
	data += str(random.choice(range(1, 13)))

	# Dia
	data += "-"
	data += str(random.choice(range(1, 30)))
	
	# Hora
	data += " "
	data += str(random.choice(range(0, 24)))

	# Minutos
	data += ":"
	data += str(random.choice(range(0, 60)))
	data += "'"

	return random.choice([data, "null"])

def custoAleatorio():
	custo = ""
	custo += random.choice("1123456789")
	custo += random.choice("0123456789")
	custo += random.choice("0123456789")
	custo += "."
	custo += random.choice("0123456789")
	custo += random.choice("0123456789")

	return custo

def insert():
	sql = "INSERT INTO Transporte(id, dataIniciou, dataTerminou, custoTransporte, quantidadeCarga, Servico_id, Motorista_id)\n"
	sql +="VALUES (" + str(nextIdTransporte())
	sql +=", '" + dataIniciouAleatoria() + "'"
	sql +=", " + dataTerminouAleatoria()
	sql +=", " + custoAleatorio()
	sql +=", " + quantidadeAleatoria()
	sql +=", " + str(idServicoAleatorio())
	sql +=", " + str(idMotoristaAleatorio())
	sql +=");\n"

	return sql

# Dá uma nova seed ao random.
random.seed()

# Abre o arquivo onde será escrito o SQL.
with open(ARQUIVO_DE_SAIDA, "w") as arqSaida:
	# Coloca um cabeçalho para o arquivo.
	arqSaida.write("-- Popula a tabela Transporte.\n\n")

	# Escreve todas as queries para um arquivo.
	for x in range(NUMERO_DE_TRANSPORTES):
		arqSaida.write(insert() + "\n")