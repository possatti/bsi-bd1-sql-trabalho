# Definições.
ARQUIVO_DE_SAIDA = "SQL Gerado/Contato.sql"
NUMERO_DE_CONTATOS = 200;

# Variável de controle do id dos telefones.
__idContato = 1 # Primeiro id.

# Retorna o próximo id de contato.
def nextIdContato():
	global __idContato
	id = __idContato
	__idContato += 1
	return id;

def insert():
	# Será usado tanto para chave primária, quanto para chave
	# estrangeira.
	id = str(nextIdContato())
	sql = "INSERT INTO Contato(id, Endereco_id)"
	sql +=" VALUES (" + id + ", " + id + ");\n"
	return sql

# Abre o arquivo onde será escrito o SQL.
with open(ARQUIVO_DE_SAIDA, "w") as arqSaida:
	# Coloca um cabeçalho para o arquivo.
	arqSaida.write("-- Popula a tabela Contato.\n\n")

	# Escreve todas as queries para um arquivo.
	for x in range(NUMERO_DE_CONTATOS):
		arqSaida.write(insert())