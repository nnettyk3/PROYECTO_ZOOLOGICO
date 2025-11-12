from prettytable import PrettyTable
from modelos.cuidados_medicos import cuidados_medicos
from datos.insertar_datos import insertar_objeto
from datos.obtener_datos import obtener_datos_objetos

def registrar_cuidado_medico():
    print("\n--- Registro de Cuidado Médico ---")
    id_animal = input("ID del Animal: ")
    fecha_visita = input("Fecha de Visita (AAAA-MM-DD): ")
    tipo_cuidado = input("Tipo de Cuidado (Ej: Vacuna, Cirugía): ")
    descripcion = input("Descripción/Diagnóstico: ")
    veterinario = input("Veterinario: ")
    observaciones = input("Observaciones (opcional): ")
    nuevo_cuidados_medicos = cuidados_medicos(id_animal=id_animal.title(), fecha_visita=fecha_visita.title(), tipo_cuidado=tipo_cuidado.title(), descripcion=descripcion.title(), veterinario=veterinario.title(), observaciones=observaciones.title())
    insertar_objeto(nuevo_cuidados_medicos)      
    
def mostrar_cuidados_medicos():
    tabla_cuidados_medicos = PrettyTable()
    tabla_cuidados_medicos.field_names = ['id_animal', 'fecha_visita', 'tipo_cuidado', 'descripcion', 'veterinario', 'observaciones']
    listado_cuidados_medicos = obtener_datos_objetos(cuidados_medicos)
    if listado_cuidados_medicos:
            for cuidados_medicos in listado_cuidados_medicos:
                tabla_cuidados_medicos.add_row(
                    [cuidados_medicos.id_animal, cuidados_medicos.fecha_visita, cuidados_medicos.tipo_cuidado, cuidados_medicos.descripcion, cuidados_medicos.veterinario, cuidados_medicos.observaciones])
            print(tabla_cuidados_medicos)