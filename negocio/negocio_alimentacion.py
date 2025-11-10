
def registrar_alimentacion(self):
        print("\n--- Registro de Alimentación ---")
        id_animal = input("ID del Animal a alimentar: ")
        tipo_comida = input("Tipo de comida: ")
        cantidad = input("Cantidad (Ej: 3.5 kg): ")
        horario = input("Horario (AAAA-MM-DD HH:MM:SS): ")
        
        exito, mensaje = self.gestion.registrar_alimentacion(id_animal, tipo_comida, cantidad, horario)
        self._mostrar_resultado(exito, mensaje)