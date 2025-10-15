


CREATE TABLE IS NOT EXISTS cuidadores (
    id_cuidadores INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    turno VARCHAR(50),
    especialidad VARCHAR(100),
);


CREATE TABLE IS NOT EXISTS animal (
    id_animal INT PRIMARY KEY AUTO_INCREMENT, 
    especie VARCHAR(100) NOT NULL,
    edad INT,
    habitat VARCHAR(100),
    id_cuidador INT,
    FOREIGN KEY (id_cuidador) REFERENCES cuidador(id_cuidador)
);


CREATE TABLE IS NOT EXISTS visitantes (
    id_visitante INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    rut VARCHAR(12) UNIQUE,
);


CREATE TABLE IS NOT EXISTS entrada (
    id_entrada INT PRIMARY KEY AUTO_INCREMENT,
    fecha_visita DATE NOT NULL,
    precio FLOAT NOT NULL,
    id_visitante INT,
    FOREIGN KEY (id_visitante) REFERENCES visitante(id_visitante)
);


