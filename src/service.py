registros = []
ids = set()
correos = set()

def crear_registro(id, nombre, correo):
    from validate import validar_id, validar_correo

    if not validar_id(id, ids):
        return "Error al crear: ID duplicado"

    if not validar_correo(correo, correos):
        return "Error al crear: correo duplicado"

    registro = {
        "id": id,
        "nombre": nombre,
        "correo": correo
    }

    registros.append(registro)
    ids.add(id)
    correos.add(correo)

    return "Registro creado exitosamente\n"

def listar_registros():
    return registros