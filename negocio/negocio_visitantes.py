from prettytable import PrettyTable
def registrar_visitante(self):
        print("\n--- Registro de Nuevo Visitante ---")
        nombre = input("Nombre: ")
        rut = input("RUT (Ej: 12345678-9): ")
        
        exito, mensaje = self.gestion.registrar_visitante(nombre, rut)
        self._mostrar_resultado(exito, mensaje)

def mostrar_visitantes(self):
    visitantes = self.gestion.obtener_lista_visitantes()
    if not visitantes:
        print("No hay visitantes registrados.")
        return

    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "RUT"]
    for v in visitantes:
        tabla.add_row([v.id_visitante, v.nombre, v.rut])
        print("\n--- Listado de Visitantes ---")
        print(tabla)
