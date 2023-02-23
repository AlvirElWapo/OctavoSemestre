DROP DATABASE estacionamientoV3;
CREATE DATABASE IF NOT EXISTS estacionamientoV3;

SHOW DATABASES;

USE estacionamientoV3;

CREATE TABLE Automovil
(
	Placas VARCHAR(8) ,
	Precio INT NOT NULL,
	Color VARCHAR(20),
	Marca VARCHAR(50),
	PRIMARY KEY(Placas)
);

CREATE TABLE Estudiante
(
	No_Cuenta INT ,
	Carrera VARCHAR(4),
	Nombre VARCHAR(50),
	Primer_Apellido VARCHAR(50),
	Segundo_Apellido VARCHAR(50),
	PRIMARY KEY(No_Cuenta)
);

CREATE TABLE Registro
(
	Fecha_Entrada DATE NOT NULL,
	Fecha_Salida DATE NOT NULL,
	Placas VARCHAR(8),
	No_Cuenta INT,
	FOREIGN KEY (Placas) REFERENCES Automovil(Placas),
	FOREIGN KEY (No_Cuenta) REFERENCES Estudiante(No_Cuenta)
);

DESCRIBE Automovil;
DESCRIBE Estudiante;
DESCRIBE Registro;

SHOW CREATE TABLE Automovil;
SHOW CREATE TABLE Estudiante;
SHOW CREATE TABLE Registro;


INSERT INTO Automovil VALUES('ABC-DEFG', 500000, 'VERDE','CHEVROLET');
INSERT INTO Automovil VALUES('CDE-DEFG', 550000, 'AZUL','CHEVROLET');
INSERT INTO Automovil VALUES('HIJ-DEFG', 555000, 'AMARILLO','CHEVROLET');
INSERT INTO Automovil VALUES('KLM-DEFG', 555500, 'ROSA','CHEVROLET');
INSERT INTO Automovil VALUES('NOP-DEFG', 599990, 'MORADO','CHEVROLET');


INSERT INTO Estudiante  VALUES(1, 'ISW', 'Andrés','Alvir','Guzmen');
INSERT INTO Estudiante  VALUES(2, 'IPI', 'Andrew','Alvar','Guzmln');
INSERT INTO Estudiante  VALUES(3, 'IPI', 'Andréx','Alver','Guzmin');
INSERT INTO Estudiante  VALUES(4, 'ISC', 'Andréws','Alvor','Guzmen');
INSERT INTO Estudiante  VALUES(5, 'ISC', 'Andriux','Alvur','Guzmxn');

INSERT INTO Registro VALUES('2023-01-08', '2024-12-08', 'HIJ-DEFG',1);
INSERT INTO Registro VALUES('2023-11-01', '2023-12-08', 'KLM-DEFG',5);
INSERT INTO Registro VALUES('2023-12-03', '2024-12-08', 'NOP-DEFG',3);
INSERT INTO Registro VALUES('2023-05-02', '2025-12-08', 'ABC-DEFG',2);
INSERT INTO Registro VALUES('2023-08-01', '2022-12-08', 'CDE-DEFG',4);

SELECT * FROM Automovil;
SELECT * FROM Estudiante;
SELECT * FROM Registro;

DELETE FROM Registro;
DELETE FROM Automovil;
DELETE FROM Estudiante;

DROP TABLE Registro;
DROP TABLE Automovil;
DROP TABLE Estudiante;

DROP DATABASE estacionamientoV3;
