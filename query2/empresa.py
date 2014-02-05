#!/usr/bin/python3

# Importações.
import random
import libcontato
from libendereco import Endereco

# Definições.
ARQUIVO_DE_NOMES = "Dados/Nomes de Empresas.txt"
ARQUIVO_DE_SAIDA = "SQL Gerado/empresas e seus contatos.sql"

# Monta uma querie para enserir uma empresa e os seus contatos.
def insertEmpresaAleatoria():
	# FIXME: Acertar a query.
	sql = "INSERT INTO veiculo(placa, modelo)\n"
	sql +="VALUES ('asd', 'asd');\n"
	return sql

# Dá uma nova seed ao random.
random.seed()

for x in range(10):
	end = libcontato.enderecoAleatorio()
	print(end.cep, end.bairro, end.rua)

## Escreve todas as queries para um arquivo.
## FIXME: Acertar para gravar as queries corretas.
#with open(ARQUIVO_DE_SAIDA, "w") as arqSaida:
#	for x in range(100):
#		arqSaida.write(insertVeiculoAleatorio() + "\n")