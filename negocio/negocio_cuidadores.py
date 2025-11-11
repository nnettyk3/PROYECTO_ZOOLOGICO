from prettytable import PrettyTable
from modelos.cuidadores import Cuidador
from datos.insertar_datos import insertar_objeto

def registrar_cuidador():
    print("\n--- Registro de Nuevo Cuidador ---")
    nombre = input("Nombre del Cuidador: ")
    turno = input("Turno (Mañana/Tarde): ") 
    especialidad = input("Especialidad: ")
    nuevo_cuidador = Cuidador(nombre=nombre.title(), turno=turno.title(), especialidad=especialidad.title())
    insertar_objeto(nuevo_cuidador)        
        
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
        