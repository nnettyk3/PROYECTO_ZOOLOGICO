from prettytable import PrettyTable
from datos.insertar_datos import insertar_objeto
from modelos.entrada import entrada
from datos.obtener_datos import obtener_datos_objetos

def vender_entrada():
        print("\n--- Venta de Entradas ---")
        print(f"Tipos disponibles: {list(gestion.precios_entradas.keys())}")
        tipo = input("Ingrese el TIPO de entrada: ")
        fecha_visita = input("Fecha de Visita (AAAA-MM-DD): ")
        id_visitante = input("ID del Visitante (Opcional, dejar vacío si no registrado): ")
        nuevo_vender_entrada = vender_entrada(tipo=tipo.title(), fecha_visita=fecha_visita.title(), id_visitante=id_visitante.title())
        insertar_objeto(nuevo_vender_entrada)

def mostrar_vender_entrada():
    tabla_vender_entrada = PrettyTable()
    tabla_vender_entrada.field_names = ['tipo', 'fecha_visita', 'id_visitante']
    listado_vender_entrada = obtener_datos_objetos(vender_entrada)
    if listado_vender_entrada:
            for vender_entrada in listado_vender_entrada:
                tabla_vender_entrada.add_row(
                    [vender_entrada.id_animal, vender_entrada.tipo, vender_entrada.fecha_visita, vender_entrada.id_visitante])
            print(tabla_vender_entrada)
        
        # Maneja ID de visitante opcional
        id_visitante = int(id_visitante) if id_visitante.isdigit() else None
        
      