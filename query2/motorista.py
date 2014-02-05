#!/usr/bin/python3

# Definições.
ARQUIVO_COM_NOMES = "Dados/nomes.txt"
ARQUIVO_DE_SAIDA = "SQL Gerado/motorista.sql"

# Lê

# Retorna uma query sql para inserir um motorista na tabela.
def insertMotorista( nome ):
   sql = '''INSERT 
   '''
   return sql

# Abre os arquivos.
arqNomes = open(ARQUIVO_COM_NOMES, "r")
arqSaida = open(ARQUIVO_DE_SAIDA, "w")

print("funciona")
#with open(ARQUIVO_COM_NOMES, "r") as nomes:
#    for nome in nomes:
#    	nome.strip()
        

## Teste.
#for x in range(101):
#	nome = arqNomes.readline()
#	nome = nome.strip()
#	print(arqNomes.tell())
#	print(nome)

# Fecha os arquivos abertos.
arqSaida.close()
arqNomes.close()