from prettytable import PrettyTable
from datos.insertar_datos import insertar_objeto
from modelos.alimentacion import Alimentacion
from datos.obtener_datos import obtener_datos_objetos


def registrar_alimentacion():
    print("\n--- Registro de Alimentación ---")
    id_animal = input("ID del Animal a alimentar: ")
    tipo_comida = input("Tipo de comida: ")
    cantidad = input("Cantidad (Ej: 3.5 kg): ")
    horario = input("Horario (AAAA-MM-DD HH:MM:SS): ")
        
    nuevo_alimentacion = Alimentacion(id_animal=id_animal.title(), tipo_comida=tipo_comida.title(), cantidad=cantidad.title(), horario=horario.title())
    insertar_objeto(nuevo_alimentacion)

def mostrar_alimentacion():
    tabla_alimentacion = PrettyTable()
    tabla_alimentacion.field_names = ['id_alimentacion', 'id_animal', 'tipo_comida', 'cantidad_comida', 'cantidad', 'horario']
    listado_alimentacion = obtener_datos_objetos(alimentacion)
    if listado_alimentacion:
        for alimentacion in listado_alimentacion:
            tabla_alimentacion.add_row(
                [alimentacion.id_alimentacion, alimentacion.id_animal, alimentacion.tipo_comida, alimentacion.cantidad_comida, alimentacion.cantidad, alimentacion.horario])
        print(tabla_alimentacion)
