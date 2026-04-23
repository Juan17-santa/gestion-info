from validate import validar_id, validar_correo
from file import load_data, save_data

def crear_registro(id, nombre, correo):
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

        return "Registro creado exitosamente\n"

    except ValueError as e:
        print(f" {e}")

def listar_registros():
    registros = load_data()

    if not registros:
        print("No hay registros\n")
        return

    for r in registros:
        print(r)