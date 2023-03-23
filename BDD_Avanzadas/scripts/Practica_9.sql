CREATE DATABASE escuela;

CREATE TABLE Estudiante
(
    nombre varchar(30)NOT NULL,
    nocuenta int AUTO_INCREMENT,
    carrera char(3) NOT NULL DEFAULT 'LSC' CHECK
    (
        carrera='LSC'||
        carrera='IPI' || 
        carrera='ISW' || 
        carrera='IPL'
    ),
    curp char(16) UNIQUE, 
    sexo set('f','m') DEFAULT 'f' NOT NULL, 
    fechaNac date,
    semestre int NOT NULL check(semestre>=1 && semestre<=20),   
    PRIMARY KEY (nocuenta)
);

DESCRIBE Estudiante;

CREATE TABLE Calificaciones
(
    nocuenta int NOT NULL,
    anio year NOT NULL check(anio<=2020),
    periodo int NOT NULL, 
    oportunidad char(1) NOT NULL,
    Calificacion float DEFAULT 0 check(Calificacion>=0 && Calificacion<=10),
    materia varchar(20) NOT NULL,
    FOREIGN KEY (nocuenta) REFERENCES Estudiante(noCuenta)
);

DESCRIBE Calificaciones;


INSERT INTO Estudiante
(nombre,curp,fechaNac,semestre)     VALUES
('Andres','ABCDEFG','1993/05/12',1);

INSERT INTO Estudiante
(nombre,curp,fechaNac,semestre)     VALUES
('Alvir','BCDEFG','1994/05/12',2);

INSERT INTO Estudiante
(nombre,curp,fechaNac,semestre)     VALUES
('Guzmán','CDEFG','1995/05/12',4);

SELECT * FROM Estudiante;

INSERT INTO Calificaciones
(nocuenta,anio,periodo,oportunidad,materia) VALUES
(4      ,2020   ,3,     'p',        'POO');

INSERT INTO Calificaciones
(nocuenta,anio,periodo,oportunidad,materia) VALUES
(2      ,2017   ,4,     's',        'BDD');

INSERT INTO Calificaciones
(nocuenta,anio,periodo,oportunidad,materia) VALUES
(3      ,2019   ,7,     's',        'THDS');

SELECT * FROM Calificaciones; 


INSERT INTO Estudiante
(nombre, carrera, curp, sexo, fechaNac, semestre) VALUES
('Andres', 'ISW', 'EFG', 'f', '1996/05/12', 1);

INSERT INTO Estudiante
(nombre, carrera, curp, sexo, fechaNac, semestre) VALUES
('Andrea', 'IPI', 'DEFG', 'm', '1993/05/12', 1);

INSERT INTO Estudiante
(nombre, carrera, curp, sexo, fechaNac, semestre) VALUES
('Andrew', 'ISW', 'FG', 'f', '1992/05/12', 1);

SELECT * FROM Estudiante;

INSERT INTO Calificaciones VALUES
(6,2000,7,'p',6.0,'Microcontroladores');

INSERT INTO Calificaciones VALUES
(11,2003,8,'p',5.1,'ISW');

INSERT INTO Calificaciones VALUES
(10,2003,10,'s',10.0,'BDD');

SELECT * FROM Calificaciones;
