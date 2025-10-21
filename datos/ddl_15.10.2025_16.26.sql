


INSERT INTO animal (nombre, especie, habitat, edad) VALUES
('Leo', 'León', 8, 'Sabana Africana'),
('Mimi', 'Tigre de Bengala', 5, 'Selva Tropical'),
('Toto', 'Elefante Africano', 12, 'Sabana'),
('Luna', 'Pingüino Emperador', 4, 'Zona Polar'),
('Roco', 'Gorila Occidental', 10, 'Bosque Húmedo'),
('Coco', 'Cocodrilo del Nilo', 15, 'Pantano'),
('Nala', 'Leona', 7, 'Sabana Africana'),
('Paco', 'Guacamayo Azul', 3, 'Selva Tropical'),
('Dumbo', 'Elefante Asiático', 9, 'Zona Asiática'),
('Max', 'Oso Pardo', 6, 'Bosque Templado');

INSERT INTO cuidadores (nombre, turno, especialidad) VALUES
('Juan Torres', 'Mañana', 'Mamiferos Grandes'),
('Ana Gomez', 'Tarde', 'Aves Exoticas'),
('Luis Ruiz', 'Mañana', 'Reptiles'),
('Katherine Lee', 'Tarde', 'Animales', 'Acuaticos'),
('Calos Perez', 'Mañana', 'Mamiferos Pequeños'),
('Karla suazo', 'Tarde', 'Insectos'),
('Miguel Soto', 'Mañana', 'Animales Nocturnos')´,
('Cristina Cortez', 'Tarde', 'Animales Domesticos'),
('Fernando Rojos', 'Mañana', 'Animales Salvajes'),
('Laura Medina', 'Tarde', 'Animales Marinos');

INSERT INTO visitantes (nombre, rut) VALUES
('Pedro Alvarez', '12346789-0'),
('Maria Fernandez', '98765432-1'),
('Jorge Ramirez', '45678911-2'),
('Sofia Morales', '32165498-3'),
('Diego Castro', '65499876-4'),
('Elena Rivas', '78912354-5'),
('Andres Molina', '14785236-6'),
('Carla Vega', '96325874-7'),
('Rafael Soto', '85274196-8'),
('Isabel Cruz', '74185296-9'),
('Natalia Jimenez', '15975366-0'),
('Victor Salazar', '35715948-1'),
('Gabriela Ortiz', '25845679-2'),
('Santiago Fuentes', '65412387-3'),
('Valentina Rojas', '78912332-4');

INSERT INTO cuidados_medicos (id_animal, fecha, tipo_cuidado, descripcion, veterinario, observaciones) VALUES
(1, '15-10-2025', 'Revision Gneneral', 'Chequeo de rutina, peso y estado general', 'Dr. carlos Mendez', 'Animal en buen estado de salud'),
(2, '16-10-2025')






INSERT INTO alimentacion (id_animal, tipo_comida, cantidad, horario)
VALUES
(1, 'Carne fresca', '3 kg', '2025-10-18 09:00:00'),
(2, 'Heno y agua', '5 kg', '2025-10-18 08:30:00'),
(3, 'Frutas variadas', '2 kg', '2025-10-18 10:00:00'),
(4, 'Pescado', '1.5 kg', '2025-10-18 11:00:00'),
(5, 'Granos y vegetales', '3.5 kg', '2025-10-18 12:00:00');

INSERT INTO entrada (fecha_visita, precio, id_visitante)
VALUES
('18-10-2025', 5000, 1),
('19-10-2025', 4500, 2),
('20-10-2025', 6000, 3),
('21-10-2025', 5500, 4),
('22-10-2025', 7000, 5);

