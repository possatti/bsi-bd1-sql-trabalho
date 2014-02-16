import random

# Definições.
ARQUIVO_DE_SAIDA = "SQL Gerado/Acidente.sql"
NUMERO_DE_ACIDENTES = 100;
NUMERO_DE_TRANSPORTES = 200;
DESCRICOES = [
'Colisão com um carro esporte.',
'Atropelamento de um político.',
'Atropelamento de um Chocobo.',
'O veículo entrou no meio de um fogo cruzado entre gangues.',
'Um meteoro pegou de raspão no veículo.',
'Houve um tsunami no local de entrega',
'Um prédio caiu no meio da estrada, bloqueando as estradas num raio de 50 metros.',
'Um transformer se apaixonou pelo veículo, e interronpeu o caminho para ficar cantando o veículo',
'A carga entrou em combustão espontânea. Apenas foi possível salvar 50% da carga',
'Uma manada de elefantes saiu atropelando tudo o que tinha no caminho. Felizmente os motoristas sobreviveram, mas o veículo e a carga se encontram em péssimo estado.',
'80% da carga foi roubada em um semáforo fechado.'
]


# Variável de controle do id dos telefones.
__idAcidente = 1 # Primeiro id.

# Retorna o próximo id de acidente.
def nextIdAcidente():
	global __idAcidente
	id = __idAcidente
	__idAcidente += 1
	return id;

def descricaoAleatoria():
	return random.choice(DESCRICOES)

def idTransporteAleatorio():
	# Sorteia um inteiro pertencente ao intervalo inclusivo.
	return random.randint(1, NUMERO_DE_TRANSPORTES)

def insert():
	sql = "INSERT INTO Acidente(id, descricao, Transporte_id)\n"
	sql +="VALUES (" + str(nextIdAcidente())
	sql +=", '" + descricaoAleatoria() + "'"
	sql +=", " + str(idTransporteAleatorio()) + ");\n"
	return sql

# Dá uma nova seed ao random.
random.seed()

# Abre o arquivo onde será escrito o SQL.
with open(ARQUIVO_DE_SAIDA, "w") as arqSaida:
	# Coloca um cabeçalho para o arquivo.
	arqSaida.write("-- Popula a tabela Acidente.\n\n")

	# Escreve todas as queries para um arquivo.
	for x in range(NUMERO_DE_ACIDENTES):
		arqSaida.write(insert() + "\n")
	arqSaida.write("\n")