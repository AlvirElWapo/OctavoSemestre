DROP DATABASE IF EXISTS escuela;
CREATE DATABASE IF NOT EXISTS escuela;
USE escuela;

CREATE TABLE Estudiante
(
    nombre      VARCHAR(30)     NOT NULL,
    nocuenta    INT             AUTO_INCREMENT /*PK*/,
    carrera     CHAR(3)         NOT NULL        DEFAULT 'LSC',
    curp        CHAR(16)        UNIQUE,
    sexo        CHAR(1)         NOT NULL        DEFAULT '1',
    fecha_nac   DATE,
    PRIMARY KEY(nocuenta)
);

CREATE TABLE Calificaciones
(
    Nocuenta    INT             NOT NULL,
    FOREIGN KEY (Nocuenta) REFERENCES Estudiante(nocuenta),
    año         YEAR            NOT NULL,
    periodo     INT             NOT NULL,
    oportunidad CHAR(1)         NOT NULL,
    Calificación    FLOAT       DEFAULT 0.0,
    materia         VARCHAR(20) NOT NULL,
    UNIQUE(Nocuenta, año, periodo),
    UNIQUE(nocuenta, materia, oportunidad)
);

/*              CAMPOS VACÍOS             */
INSERT INTO Estudiante(nombre, curp, fecha_nac) VALUES
("Andres Alvir","AeGA1234","2001/08/13");

INSERT INTO Estudiante(nombre, curp, fecha_nac) VALUES
("Andres Alvar","AbGA1234","2001/08/13");

INSERT INTO Estudiante(nombre, curp, fecha_nac) VALUES
("Andres Alver","AgGA1234","2001/08/13");

INSERT INTO Calificaciones (nocuenta, año, periodo, oportunidad, materia) VALUES
(1, 2001, 1,'y','Integr Profesional');
INSERT INTO Calificaciones (nocuenta, año, periodo, oportunidad, materia) VALUES
(2, 2005, 3,'n','Compiladores');
INSERT INTO Calificaciones (nocuenta, año, periodo, oportunidad, materia) VALUES
(3, 2008, 4,'y','Administración');

/*              VALORES POR DEFECTO             */

INSERT INTO Estudiante(nombre, carrera, curp, sexo, fecha_nac) VALUES
("Andres Alvir","ISW","AeGAy234",'M' ,"2001/08/13");

INSERT INTO Estudiante(nombre, carrera, curp, sexo, fecha_nac) VALUES
("Andres Alvxr","IPI","AeGAm234",'H' ,"2001/08/14");

INSERT INTO Estudiante(nombre, carrera, curp, sexo, fecha_nac) VALUES
("Andres Alvkr","ISC","AeGAz234",'M' ,"2001/08/15");


INSERT INTO Calificaciones (Nocuenta, año, periodo, oportunidad, Calificación, materia) VALUES
(6, 2005, 8,'y',6.5 ,'Integr Profesional');
INSERT INTO Calificaciones (Nocuenta, año, periodo, oportunidad, Calificación, materia) VALUES
(4, 2009, 10,'n',8.5 ,'Derecho Inf');
INSERT INTO Calificaciones (Nocuenta, año, periodo, oportunidad, Calificación, materia) VALUES
(5, 2023, 3,'n',10.0 ,'BDD Avanzadas');

DROP TABLE Calificaciones;
DROP TABLE Estudiante;
