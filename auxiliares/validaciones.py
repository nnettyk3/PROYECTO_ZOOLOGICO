
def validar_entero(valor, campo):
    try:
        return int(valor)
    except ValueError:
        raise ValueError(f"El campo '{campo}' debe ser un número entero.")
