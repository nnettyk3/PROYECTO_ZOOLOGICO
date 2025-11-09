

CREATE TABLE IF NOT EXISTS animal (
    id_animal INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    especie VARCHAR(100) NOT NULL,
    edad INT,
    habitat VARCHAR(100)
);

CREATE TABLE IF NOT EXISTS cuidadores (
    id_cuidador INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    turno VARCHAR(50),
    especialidad VARCHAR(100)
);


CREATE TABLE IF NOT EXISTS visitantes (
    id_visitante INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100) NOT NULL,
    rut VARCHAR(12) UNIQUE
);

CREATE TABLE IF NOT EXISTS cuidados_medicos (
    id_cuidado_medico INT PRIMARY KEY AUTO_INCREMENT,
    id_animal INT NOT NULL,
    fecha DATE NOT NULL,
    tipo_cuidado VARCHAR(50) NOT NULL,
    descripcion TEXT NOT NULL,
    veterinario VARCHAR(100) NOT NULL,
    observaciones TEXT,
    FOREIGN KEY (id_animal) REFERENCES animal(id_animal)
);

CREATE TABLE IF NOT EXISTS entrada (
    id_entrada INT PRIMARY KEY AUTO_INCREMENT,
    fecha_visita DATE NOT NULL,
    precio FLOAT NOT NULL,
    id_visitante INT,
    FOREIGN KEY (id_visitante) REFERENCES visitantes(id_visitante)
);

CREATE TABLE IF NOT EXISTS alimentacion (
    id_alimentacion INT PRIMARY KEY AUTO_INCREMENT,
    id_animal INT NOT NULL,
    tipo_comida VARCHAR(100) NOT NULL,
    cantidad VARCHAR(50),
    horario DATETIME,
    FOREIGN KEY (id_animal) REFERENCES animal(id_animal)
);
