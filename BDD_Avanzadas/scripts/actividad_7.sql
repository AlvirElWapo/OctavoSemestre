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
    anio SMALLINT,
    consecutivo INT,
    carrera CHAR(3),
    curp CHAR(16),
    sexo CHAR(1),
    fechaNac DATE,
    PRIMARY KEY(anio, consecutivo)
);

CREATE TABLE Calificaciones2
(
    anio SMALLINT,
    consecutivo INT,
    periodo INT UNIQUE,
    oportunidad CHAR(1),
    Calificación FLOAT,
    materia VARCHAR(20) UNIQUE,
    folio INT NOT NULL UNIQUE AUTO_INCREMENT,
    FOREIGN KEY (anio, consecutivo) REFERENCES Estudiante1(anio, consecutivo)
);

INSERT INTO Estudiante VALUES('Andres Alvir', 123,'ISW', 'AIGA123', 'H','2001-08-13');
INSERT INTO Estudiante VALUES('Andres Alvir2', 234,'IPI', 'AIGA456', 'M','2001-08-14');
INSERT INTO Estudiante VALUES('Andres Alvir3', 456,'ISC', 'AIGA1789', 'H','2001-08-15');

INSERT INTO Estudiante1 VALUES('Andres Alvir',2023,8, 'ISW', 'AIGA123', 'M', '2001-08-13');
INSERT INTO Estudiante1 VALUES('Andres Alvir2',2020,7, 'ISW', 'AIGA456', 'H', '2001-08-15');
INSERT INTO Estudiante1 VALUES('Andres Alvir3',2022,6, 'ISW', 'AIGA1789', 'M', '2001-08-14');

/*
nocuenta INT,
    año SMALLINT,
    periodo INT,
    oportunidad CHAR(1),
    Calificación FLOAT,
    materia VARCHAR(20),
    FOREIGN KEY (nocuenta) REFERENCES Estudiante(nocuenta)
 */

INSERT INTO Calificaciones VALUES(123, 2023, 8,'y',8.5,'SOFTWARE');
INSERT INTO Calificaciones VALUES(234, 2022, 6,'n',6.0,'SEGURIDAD');
INSERT INTO Calificaciones VALUES(456, 2020, 4,'y',6.1,'PRODUCCION');
/*
anio SMALLINT,
    consecutivo INT,
    periodo INT UNIQUE,
    oportunidad CHAR(1),
    Calificación FLOAT,
    materia VARCHAR(20) UNIQUE,
    folio INT NOT NULL UNIQUE AUTO_INCREMENT,
    FOREIGN KEY (anio, consecutivo) REFERENCES Estudiante1(anio, consecutivo)
 */
INSERT INTO Calificaciones2 VALUES(8,2003,'y',8.5,'SOFTWARE',1);
INSERT INTO Calificaciones2 VALUES(7,2001,'n',6.0,'SEGURIDAD',2);
INSERT INTO Calificaciones2 VALUES(6,2005,'y',6.1,'PRODUCCION',3);



