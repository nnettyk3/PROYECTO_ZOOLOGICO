
import re

def validar_edad(edad):
    """Verifica que la edad sea un entero positivo."""
    try:
        edad = int(edad)
        return edad > 0
    except ValueError:
        return False

def formatear_rut(rut):
    """Formatea un RUT simple (ejemplo para Chile: XX.XXX.XXX-X)."""
    # Expresión regular simple para validar formato RUT
    if not re.match(r'^\d{7,8}-[\dkK]$', rut):
        return None
    return rut.upper()