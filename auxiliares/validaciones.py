
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

# auxiliares/validaciones.py

def validar_texto_no_vacio(texto):
    """Verifica que un campo de texto no esté vacío y no contenga solo espacios."""
    return bool(texto) and str(texto).strip() != ""

def validar_entero_positivo(valor):
    """Verifica que el valor sea un entero positivo (para edad)."""
    try:
        edad = int(valor)
        return edad >= 0
    except ValueError:
        return False