
class CuidadorDAO:
    # ...
    def obtener_todos(self):
        # 1. Habla el idioma SQL (SELECT)
        query = "SELECT id_cuidador, nombre, turno, especialidad FROM cuidadores;"
        # cursor.execute(query) 

        # 2. Obtiene las filas de la BBDD (resultados)
        resultados = cursor.fetchall() 
        
        cuidadores = []
        # 3. REALIZA EL MAPEO (El punto CLAVE):
        for fila in resultados:
            # Convierte la fila de la BBDD (diccionario) en un objeto Cuidador
            cuidador = Cuidador(
                id_cuidador=fila['id_cuidador'],
                nombre=fila['nombre'],
                turno=fila['turno'],
                especialidad=fila['especialidad']
            )
            cuidadores.append(cuidador)
            
        return cuidadores # Retorna objetos POO al módulo de Negocio