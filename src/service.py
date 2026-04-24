from validate import validar_id, validar_correo
from file import load_data, save_data

def new_register(id, nombre, correo):
    try:
        registros = load_data()

        ids = {str(r["id"]) for r in registros}
        correos = {r["correo"] for r in registros}

        if not validar_id(id, ids):
            return "Error: ID duplicado"

        if not validar_correo(correo, correos):
            return "Error: correo ya existe"

        nuevoRegistro = {
            "id": id,
            "nombre": nombre,
            "correo": correo
        }

        registros.append(nuevoRegistro)
        save_data(registros)

        return "\nRegistro creado exitosamente"

    except ValueError as e:
        print(f" {e}")

def list_records():
    registros = load_data()

    if not registros:
        print("No hay registros\n")
        return

    for r in registros:
        print(r)

def search_record(id):
    registros = load_data()

    resultado = [r for r in registros if str(r["id"]) == str(id)]

    if not resultado:
        return "Error: ID no encontrado"

    return resultado[0]

def update_record(id, nombre=None, correo=None):
    registros = load_data()

    for r in registros:
        if str(r["id"]) == str(id):

            if nombre:
                r["nombre"] = nombre

            if correo:
                correos = {reg["correo"] for reg in registros}

                if not validar_correo(correo, correos):
                    return "Error: correo ya existe"

                r["correo"] = correo

            save_data(registros)
            return "Registro actualizado correctamente"

    return "Error: ID no existe"

def delete_record(id):
    registros = load_data()

    nuevos = [r for r in registros if str(r["id"]) != str(id)]

    if len(nuevos) == len(registros):
        return "Error: ID no existe"

    save_data(nuevos)
    return "Registro eliminado correctamente"