DROP DATABASE Ferreteria;
CREATE DATABASE IF NOT EXISTS Ferreteria;
USE Ferreteria;


CREATE TABLE IF NOT EXISTS Cliente
(
    nombre VARCHAR(30) NOT NULL,
    no_cliente INT NOT NULL, 
    rfc CHAR(10) NOT NULL UNIQUE,
    CURP CHAR(16) UNIQUE,
    telefono INT NOT NULL, 
    correo VARCHAR(20),


    PRIMARY KEY(no_cliente)
);
CREATE TABLE IF NOT EXISTS  Productos 
(
    clave INT NOT NULL,
    nombre VARCHAR(30) NOT NULL,
    fecha_cad DATE,

    PRIMARY KEY(clave)


);

CREATE TABLE IF NOT EXISTS Pedidos
(
    clave INT FOREIGN KEY REFERENCES(Productos.clave),
    no_cliente INT FOREIGN KEY REFERENCES(Cliente.no_cliente)
);


