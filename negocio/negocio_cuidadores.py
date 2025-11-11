from prettytable import PrettyTable
from modelos.cuidadores import Cuidador
from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_datos_objetos

def registrar_cuidador():
    print("\n--- Registro de Nuevo Cuidador ---")
    nombre = input("Nombre del Cuidador: ")
    turno = input("Turno (Mañana/Tarde): ") 
    especialidad = input("Especialidad: ")
    nuevo_cuidador = Cuidador(nombre=nombre.title(), turno=turno.title(), especialidad=especialidad.title())
    insertar_objeto(nuevo_cuidador)        
        
def mostrar_cuidadores():
    tabla_cuidadores = PrettyTable()
    tabla_cuidadores.field_names = ['id_cuidador', 'nombre', 'turno', 'especialidad']
    listado_cuidadores = obtener_datos_objetos(Cuidador)
    if listado_cuidadores:
        for cuidadores in listado_cuidadores:
            tabla_cuidadores.add_row(
                [cuidadores.id_cuidador, cuidadores.nombre, cuidadores.turno, cuidadores.especialidad])
        print(tabla_cuidadores)