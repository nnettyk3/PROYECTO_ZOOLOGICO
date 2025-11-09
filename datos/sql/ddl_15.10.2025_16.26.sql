


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
('Katherine Lee', 'Tarde', 'Animales Acuaticos'),
('Calos Perez', 'Mañana', 'Mamiferos Pequeños'),
('Karla suazo', 'Tarde', 'Insectos'),
('Miguel Soto', 'Mañana', 'Animales Nocturnos'),
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
(1, '2025-10-15', 'Revision General', 'Chequeo de rutina, peso y estado general', 'Dr. Carlos Mendez', 'Animal en buen estado de salud'),
(2, '2025-10-16', 'Vacunacion', 'Aplicacion de vacuna antirrabica', 'Dra. Lucia Fernandez', 'Sin reacciones adversas'),
(3, '2025-10-17', 'Tratamiento Dental', 'Limpieza dental', 'Dr. Miguel Torres', 'Mejora en la salud bucal'),
(4, '2025-10-18', 'Revision de Piel', 'Evaluacion de Lesiones cutaneas', 'Dra. Ana Ruiz', 'No se encontraron problemas'),
(5, '2025-10-19', 'Cirugia Menor', 'Extraccion de tumor benigno', 'Dra. Sofia Lopez', 'Recuperacion satisfactoria'),
(1, '2025-10-20', 'Revision General', 'Chequeo de rutina', 'Dr. Carlos Mendez', 'Animal en buen estado de salud'),
(2, '2025-10-21', 'Vacunacion', 'Aplicacion de vacuna contra la gripe felina', 'Dra. Lucia Fernandez', 'Sin reacciones adversas'),
(3, '2025-10-22', 'Tratamiento Dental', 'Revision y Limpieza dental', 'Dr. Miguel Torres', 'Mejora en la salud bucal'),
(4, '2025-10-23', 'Revision de Piel', 'Evaluacion de Lesiones cutaneas', 'Dra. Ana Ruiz', 'No se encontraron problemas'),
(5, '2025-10-24', 'Cirugia Menor', 'Extraccion de tumor benigno', 'Dra. Sofia Lopez', 'Recuperacion satisfactoria');


INSERT INTO alimentacion (id_animal, tipo_comida, cantidad, horario) VALUES 
(1, 'Carne fresca', 3, '2025-10-18 09:00:00'), 
(2, 'Heno y agua', 5, '2025-10-18 08:30:00'), 
(3, 'Frutas variadas', 2, '2025-10-18 10:00:00'), 
(4, 'Pescado', 1.5, '2025-10-18 11:00:00'), 
(5, 'Granos y vegetales', 3.5, '2025-10-18 12:00:00');

INSERT INTO entrada (fecha_visita, precio, id_visitante)
VALUES
('2025-10-18', 5000, 1),
('2025-10-19', 4500, 2),
('2025-10-20', 6000, 3),
('2025-10-21', 5500, 4),
('2025-10-22', 7000, 5);


