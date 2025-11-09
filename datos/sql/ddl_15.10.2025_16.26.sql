


INSERT INTO animal (nombre, especie, habitat, edad) VALUES
('Leo', 'León', 'Sabana Africana', 8),
('Mimi', 'Tigre de Bengala', 'Selva Tropical', 5),
('Toto', 'Elefante Africano', 'Sabana', 12),
('Luna', 'Pingüino Emperador', 'Zona Polar', 4),
('Roco', 'Gorila Occidental', 'Bosque Húmedo', 10),
('Coco', 'Cocodrilo del Nilo', 'Pantano', 15),
('Nala', 'Leona', 'Sabana Africana', 7),
('Paco', 'Guacamayo Azul', 'Selva Tropical', 3),
('Dumbo', 'Elefante Asiático', 'Zona Asiática', 9),
('Max', 'Oso Pardo', 'Bosque Templado', 6);

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
(2, '16-10-2025', 'vacunacion', 'Aplicacion de vacuna antirrabica', 'Dra. Lucia Fernandez', 'Sin reacciones adversas'),
(3, '17-10-2025', 'Tratamiento Dental', 'Limpieza denntal', 'Dr','Miguel Torres', 'Mejora en la salud bucal'),
(4, '18-10-2025', 'Revision de Piel', 'Evaluacion de Lesiones cutaneas', 'Dra. Ana Ruiz', 'No se encontraron problemas'),
(5, '19-10-2025', 'Cirugia Menor', 'Extraccion de tumot benigmo', 'Dr. Sofia Lopez', 'Recuperacion satisfactoria'),
(1, '20-10-2025', 'Revision General', 'Chequeo de rutina', 'Dr. Carlos Mendez', 'Animal en buen estado de salud'),
(2, '21-10-2025', 'Vacunacion', 'Aplicacion de vacuna contra la gripe felina', 'Dra. Lucia Fernandez', 'Sin reacciones adversas'),
(3, '22-10-2025', 'Tratamiento Dental', 'Revision y Limpieza dental', 'Dr. Miguel Torres', 'Mejora en la salud bucal'),
(4, '23-10-2025', 'Revision de piel', 'Evaliacion de Lesiones cutaneas', 'Dra. Ana Ruiz', 'No se encontraron problemas'),
(5, '24-10-2025', 'cirugia menor', 'Extraccion de tumot benigno', 'Dr. sofia Lopez', 'Recuperacion satisfactoria');


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

