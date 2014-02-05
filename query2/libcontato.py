from libendereco import Endereco

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

def enderecoAleatorio():
	# FIXME: Não está tão aleatório assim, né?
	return Endereco("31173-053", "Smallville", "Street 1")