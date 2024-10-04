import modules.utils.mensajes as msj
def confirmacion (mensaje):
    continuar = input({msj})
    if continuar.upper() != 'S':
        return False
    else:
        return True
