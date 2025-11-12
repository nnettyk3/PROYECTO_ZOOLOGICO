from prettytable import PrettyTable
from modelos.visitantes import Visitantes
from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_datos_objetos

def registrar_visitante():
    print("\n--- Registro de Nuevo Visitante ---")
    nombre = input("Nombre: ")
    rut = input("RUT (Ej: 12345678-9): ")
    nuevo_visitantes = visitantes(nombre=nombre.title(), rut=rut.title())
    insertar_objeto(nuevo_visitantes)        
        
    
        

def mostrar_visitantes():
    tabla = PrettyTable()
    tabla.field_names = ["ID", "Nombre", "RUT"]
    for v in visitantes:
        tabla.add_row([v.id_visitante, v.nombre, v.rut])
        print("\n--- Listado de Visitantes ---")
        print(tabla)
   