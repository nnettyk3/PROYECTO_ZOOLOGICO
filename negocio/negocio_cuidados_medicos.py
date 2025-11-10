
def registrar_cuidado_medico(self):
    print("\n--- Registro de Cuidado Médico ---")
    id_animal = input("ID del Animal: ")
    fecha_visita = input("Fecha de Visita (AAAA-MM-DD): ")
    tipo_cuidado = input("Tipo de Cuidado (Ej: Vacuna, Cirugía): ")
    descripcion = input("Descripción/Diagnóstico: ")
    veterinario = input("Veterinario: ")
    observaciones = input("Observaciones (opcional): ")

    exito, mensaje = self.gestion.registrar_cuidado_medico(
            id_animal, fecha_visita, tipo_cuidado, descripcion, veterinario, observaciones
        )
    self._mostrar_resultado(exito, mensaje)