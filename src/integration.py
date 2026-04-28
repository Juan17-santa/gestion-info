import json
import pandas as pd

def cargar_registros(ruta="data/records.json"):
    with open(ruta, "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def exportar_csv(ruta_json="data/records.json", salida="reporte.csv"):
    registros = cargar_registros(ruta_json)

    df = pd.DataFrame(registros)
    df.to_csv(salida, index=False)

    print("CSV generado correctamente")

def filtrar_registros(**kwargs):
    registros = cargar_registros()
    df = pd.DataFrame(registros)

    for clave, valor in kwargs.items():
        df = df[df[clave] == valor]

    return df.to_dict(orient="records")