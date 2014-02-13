CREATE TABLE IF NOT EXISTS Veiculo (
	id SERIAL,
	placa VARCHAR(45) UNIQUE,
	modelo VARCHAR(45),

	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS TipoCarga (
	id SERIAL,
	nome VARCHAR(45) UNIQUE,

	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS VeiculoTipoCarga (
	Veiculo_id INT NOT NULL,
	TipoCarga_id INT NOT NULL,
	
	PRIMARY KEY(Veiculo_id, TipoCarga_id),
	
	FOREIGN KEY (Veiculo_id) REFERENCES Veiculo(id),
	FOREIGN KEY (TipoCarga_id) REFERENCES TipoCarga(id)
);

CREATE TABLE IF NOT EXISTS Endereco (
	id SERIAL,
	cep VARCHAR(45),
	estado VARCHAR(45),
	bairro VARCHAR(45),
	rua VARCHAR(45),
	numero VARCHAR(45),

	PRIMARY KEY(id)
);

CREATE TABLE IF NOT EXISTS Contato (
	id SERIAL,
	Endereco_id INT NOT NULL UNIQUE,

	PRIMARY KEY(id),
	FOREIGN KEY (Endereco_id) REFERENCES Endereco(id)
);

CREATE TABLE IF NOT EXISTS Telefone (
	id SERIAL,
	numero VARCHAR(45) UNIQUE,
	Contato_id INT NOT NULL,

	PRIMARY KEY(id),
	FOREIGN KEY (Contato_id) REFERENCES Contato(id)
);

CREATE TABLE IF NOT EXISTS Motorista (
	id SERIAL,
	nome VARCHAR(45),
	cpf VARCHAR(45) UNIQUE,
	rg VARCHAR(45) UNIQUE,
	cnh VARCHAR(45) UNIQUE,
	disponibilidade BOOL,
	Contato_id INT NOT NULL,
	Veiculo_id INT NOT NULL,

	PRIMARY KEY(id),
	FOREIGN KEY (Contato_id) REFERENCES Contato(id),
	FOREIGN KEY (Veiculo_id) REFERENCES Veiculo(id)
);

CREATE TABLE IF NOT EXISTS Empresa (
	id SERIAL,
	nome VARCHAR(45),
	cnpj VARCHAR(45) UNIQUE,
	Contato_id INT NOT NULL,

	PRIMARY KEY(id),
	FOREIGN KEY (Contato_id) REFERENCES Contato(id)
);

CREATE TABLE IF NOT EXISTS Servico (
	id SERIAL,
	descricao VARCHAR(1000),
	tipoServico VARCHAR(45),
	tipoCarga VARCHAR(45),
	quantidadeCarga VARCHAR(45),
	unidadeCarga VARCHAR(45),
	dataPedido VARCHAR(45),
	distancia VARCHAR(45),
	Empresa_id INT NOT NULL,
	origem INT NOT NULL,
	destino INT NOT NULL,

	PRIMARY KEY(id),
	FOREIGN KEY (Empresa_id) REFERENCES Empresa(id),
	FOREIGN KEY (origem) REFERENCES Endereco(id),
	FOREIGN KEY (destino) REFERENCES Endereco(id)
);

CREATE TABLE IF NOT EXISTS Transporte (
	id SERIAL,
	dataIniciou DATE,
	dataTerminou DATE,
	custoTransporte VARCHAR(45),
	Servico_id INT NOT NULL,
	Motorista_id INT NOT NULL,
	
	PRIMARY KEY(id),
	FOREIGN KEY (Servico_id) REFERENCES Servico(id),
	FOREIGN KEY (Motorista_id) REFERENCES Motorista(id)
);

CREATE TABLE IF NOT EXISTS Acidente (
	id SERIAL,
	descricao VARCHAR(45),
	Transporte_id INT NOT NULL,
	
	PRIMARY KEY(id),
	FOREIGN KEY (Transporte_id) REFERENCES Transporte(id)
);