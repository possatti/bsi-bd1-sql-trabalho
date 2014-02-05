-- Código para aprender a popular as tabelas.
INSERT INTO TipoCarga(nome)
VALUES ('Madeira');

INSERT INTO TipoCarga(nome)
VALUES ('Eletrônicos');

INSERT INTO TipoCarga(nome)
VALUES ('Animais');

INSERT INTO Veiculo(placa, modelo)
VALUES ('ASD-1234', 'Ford Focus')
/*RETURNING id AS ultimoVeiculo*/;

INSERT INTO VeiculoTipoCarga(Veiculo_id, TipoCarga_id)
VALUES ((SELECT id FROM Veiculo WHERE placa = 'ASD-1234'), (SELECT id FROM TipoCarga WHERE nome = 'Madeira'));