DROP DATABASE escuela;
CREATE DATABASE IF NOT EXISTS escuela;
USE escuela;

CREATE TABLE Estudiante
(
    nombre VARCHAR(30),
    nocuenta INT,
    carrera CHAR(3),
    curp CHAR(16),
    sexo CHAR(1),
    fechaNac DATE,
    PRIMARY KEY(nocuenta)
);

CREATE TABLE Calificaciones
(
    nocuenta INT,
    año SMALLINT,
    periodo INT,
    oportunidad CHAR(1),
    Calificación FLOAT,
    materia VARCHAR(20),
    FOREIGN KEY (nocuenta) REFERENCES Estudiante(nocuenta)
);


CREATE TABLE Estudiante1
(
    nombre VARCHAR(30),
    año SMALLINT,
    consecutivo INT,
    carrera CHAR(3),
    curp CHAR(16),
    sexo CHAR(1),
    fechaNac DATE,
    PRIMARY KEY(año),
    PRIMARY KEY(consecutivo)
);

CREATE TABLE Calificaciones2
(
    consecutivo INT,
    año SMALLINT;
    periodo INT,
    oportunidad CHAR(1),
    Calificación FLOAT,
    materia VARCHAR(20),
    folio INT NOT NULL UNIQUE AUTO_INCREMENT
    FOREIGN KEY (nocuenta) REFERENCES Estudiante(nocuenta)
);





