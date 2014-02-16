import random

# Definições.
ARQUIVO_DE_SAIDA = "SQL Gerado/Servico.sql"
NUMERO_DE_SERVICOS = 100;
UNIDADES = ["cabeças", "unidades", "gramas", "kilogramas"]
TIPO_DE_SERVICOS = ["NORMAL", "ECONOMICO", "EXPRESSO"]
NUMERO_DE_EMPRESAS = 100
NUMERO_DE_TIPOS_DE_CARGA = 10

# Variável de controle do id dos serviços.
__idServico = 1 # Primeiro id.

# Variável de controle do id dos endereços. Que serão usados
# como chave estrangeira para definir a origem e o destino do
# serviço.
__idEndereco = 201 # Primeiro id.

# Retorna o próximo id de telefone.
def nextIdServico():
	global __idServico
	id = __idServico
	__idServico += 1
	return id;

def nextIdEndereco():
	global __idEndereco
	id = __idEndereco
	__idEndereco += 1
	return id

def idTipoCargaAleatorio():
	return random.randint(1, NUMERO_DE_TIPOS_DE_CARGA)

def idEmpresaAleatorio():
	return random.choice(range(1, NUMERO_DE_EMPRESAS + 1))

def tipoServicoAleatorio():
	return random.choice(TIPO_DE_SERVICOS)

def quantidadeAleatoria():
	quantidade = ""
	quantidade += random.choice("123456789")
	quantidade += random.choice("0123456789")
	quantidade += random.choice("0123456789")
	return quantidade

def unidadeAleatoria():
	return random.choice(UNIDADES)

def dataAleatoria():
	data = "2011"

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

def distanciaAleatoria():
	distancia = str(random.choice(range(1, 70)))
	distancia += " Km"
	return distancia

def getDescricao( quantidade, unidade, tipoServico ):
	return "Transportar " + str(quantidade) + " " + unidade + ", usando o serviço " + tipoServico + "."

def insert():
	id = str(nextIdServico())

	quantidade = quantidadeAleatoria()
	unidade = unidadeAleatoria()
	dataPedido = dataAleatoria()
	tipoServico = tipoServicoAleatorio()
	distancia = distanciaAleatoria()

	sql = "INSERT INTO Servico(id, tipoServico, TipoCarga_id, "
	sql +="quantidadeCarga, unidadeCarga, dataPedido, distancia, "
	sql +="Empresa_id, origem, destino, descricao)\n"
	sql +="VALUES (" + str(id)
	sql +=", '" + tipoServico + "'"
	sql +=", " + str(idTipoCargaAleatorio())
	sql +=", '" + quantidade + "'"
	sql +=", '" + unidade + "'"
	sql +=", '" + dataPedido + "'"
	sql +=", '" + distancia + "'"
	sql +=", " + str(idEmpresaAleatorio())
	sql +=", " + str(nextIdEndereco())
	sql +=", " + str(nextIdEndereco())
	sql +=", '" + getDescricao(quantidade, unidade, tipoServico) + "');\n"
	return sql

# Dá uma nova seed ao random.
random.seed()

# Abre o arquivo onde será escrito o SQL.
with open(ARQUIVO_DE_SAIDA, "w") as arqSaida:
	# Coloca um cabeçalho para o arquivo.
	arqSaida.write("-- Popula a tabela Servico.\n\n")

	# Escreve todas as queries para um arquivo.
	for x in range(NUMERO_DE_SERVICOS):
		arqSaida.write(insert() + "\n")