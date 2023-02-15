CREATE TABLE Automovil 
(
    precio INT NOT NULL,
    placas VARCHAR(7) NOT NULL,
    marca VARCHAR(30) NOT NULL,
    color VARCHAR(20) NOT NULL,
    PRIMARY KEY(placas)  
);

CREATE TABLE registro
(
    fechaEntrada DATE NOT NULL,
    fechaSalida DATE NOT NULL,
    placas_auto VARCHAR(6),
    n_cuenta_estudiante INT, 
    FOREIGN KEY (placas_auto) REFERENCES Automovil(placas),
    FOREIGN KEY(n_cuenta_estudiante) REFERENCES estudiante(No_Cuenta)
); 

CREATE TABLE estudiante
(
    No_Cuenta INT NOT NULL, 
    carrera VARCHAR(50) NOT NULL,
    nombre VARCHAR(20) NOT NULL, 
    primer_apellido VARCHAR(20) NOT NULL,
    segundo_apellido VARCHAR(20) NOT NULL
    PRIMARY KEY(No_Cuenta) 
); 
