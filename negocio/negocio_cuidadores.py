from prettytable import PrettyTable
def registrar_cuidador(self):
        print("\n--- Registro de Nuevo Cuidador ---")
        nombre = input("Nombre del Cuidador: ")
        turno = input("Turno (Mañana/Tarde): ") 
        especialidad = input("Especialidad: ")
        
        exito, mensaje = self.gestion.registrar_nuevo_cuidador(nombre, turno, especialidad)
        self._mostrar_resultado(exito, mensaje)
def mostrar_cuidadores(self):
    cuidadores = self.gestion.obtener_lista_cuidadores()
    if not cuidadores:
        print("No se encontraron cuidadores.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "Turno", "Especialidad"]
    for c in cuidadores:
        tabla.add_row([c.id_cuidador, c.nombre, c.turno, c.especialidad])
        print("\n--- Listado de Cuidadores ---")
        print(tabla)
        