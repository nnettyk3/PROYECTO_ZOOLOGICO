
def vender_entrada(self):
        print("\n--- Venta de Entradas ---")
        print(f"Tipos disponibles: {list(self.gestion.precios_entradas.keys())}")
        tipo = input("Ingrese el TIPO de entrada: ")
        fecha_visita = input("Fecha de Visita (AAAA-MM-DD): ")
        id_visitante = input("ID del Visitante (Opcional, dejar vacío si no registrado): ")
        
        # Maneja ID de visitante opcional
        id_visitante = int(id_visitante) if id_visitante.isdigit() else None
        
        exito, mensaje = self.gestion.vender_entrada(tipo, fecha_visita, id_visitante)
        self._mostrar_resultado(exito, mensaje)