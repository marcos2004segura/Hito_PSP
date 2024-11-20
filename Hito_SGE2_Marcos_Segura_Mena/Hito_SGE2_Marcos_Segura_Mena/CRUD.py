from conexion import conectar
import pandas as pd

# Crear registro
from conexion import conectar

def crear_encuesta(idEncuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas, vinos_semana, perdidas_control, diversion, digestivos, tension, dolor):
    conexion = conectar()
    cursor = conexion.cursor()

    # Verificar si el ID ya existe
    cursor.execute("SELECT * FROM ENCUESTA WHERE idEncuesta = %s", (idEncuesta,))
    resultado = cursor.fetchone()

    if resultado:
        print(f"Error: El ID {idEncuesta} ya existe en la base de datos.")
    else:
        sql = """
            INSERT INTO ENCUESTA (idEncuesta, edad, Sexo, BebidasSemana, CervezasSemana, BebidasFinSemana, BebidasDestiladasSemana, VinosSemana, PerdidasControl, DiversionDependenciaAlcohol, ProblemasDigestivos, TensionAlta, DolorCabeza)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        valores = (idEncuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana, bebidas_destiladas, vinos_semana, perdidas_control, diversion, digestivos, tension, dolor)
        cursor.execute(sql, valores)
        conexion.commit()
        print("Encuesta creada exitosamente en la base de datos.")

    cursor.close()
    conexion.close()


# Leer registros
def leer_encuestas():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ENCUESTA")
    registros = cursor.fetchall()

    if not registros:
        print("No se encontraron registros en la base de datos.")
    else:
        for registro in registros:
            print(registro)

    conexion.close()
    return registros

# Actualizar registro
def actualizar_encuesta(idEncuesta, edad):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "UPDATE ENCUESTA SET edad = %s WHERE idEncuesta = %s"
    valores = (edad, idEncuesta)
    cursor.execute(sql, valores)
    conexion.commit()
    print("Encuesta actualizada exitosamente.")
    conexion.close()

# Eliminar registro
def eliminar_encuesta(idEncuesta):
    conexion = conectar()
    cursor = conexion.cursor()
    sql = "DELETE FROM ENCUESTA WHERE idEncuesta = %s"
    cursor.execute(sql, (idEncuesta,))
    conexion.commit()
    print("Encuesta eliminada exitosamente.")
    conexion.close()

def consultar_por_edad():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ENCUESTA ORDER BY edad")
    registros = cursor.fetchall()
    conexion.close()
    return registros

def filtrar_consumo_alto():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ENCUESTA WHERE BebidasSemana > 10")
    registros = cursor.fetchall()
    conexion.close()
    return registros

def filtrar_perdidas_control():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ENCUESTA WHERE PerdidasControl > 3")
    registros = cursor.fetchall()
    conexion.close()
    return registros

def exportar_a_excel():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM ENCUESTA")
    registros = cursor.fetchall()

    # Definir nombres de columnas
    columnas = [
        "idEncuesta", "Edad", "Sexo", "BebidasSemana", "CervezasSemana",
        "BebidasFinSemana", "BebidasDestiladasSemana", "VinosSemana",
        "PerdidasControl", "DiversionDependenciaAlcohol", "ProblemasDigestivos",
        "TensionAlta", "DolorCabeza"
    ]

    # Crear un DataFrame con los registros
    df = pd.DataFrame(registros, columns=columnas)

    # Guardar el DataFrame en un archivo Excel
    archivo_excel = "registros_encuesta.xlsx"
    df.to_excel(archivo_excel, index=False)
    print(f"Datos exportados exitosamente a {archivo_excel}")

    cursor.close()
    conexion.close()


import matplotlib.pyplot as plt

def grafico_barras_consumo():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT Edad, AVG(BebidasSemana) FROM ENCUESTA GROUP BY Edad")
    datos = cursor.fetchall()
    conexion.close()

    edades = [fila[0] for fila in datos]
    consumo = [fila[1] for fila in datos]

    plt.bar(edades, consumo, color='skyblue')
    plt.xlabel("Edad")
    plt.ylabel("Consumo Promedio de Bebidas")
    plt.title("Consumo Promedio de Bebidas por Edad")
    plt.xticks(rotation=45)
    plt.show()

def grafico_pastel_genero():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT Sexo, COUNT(*) FROM ENCUESTA GROUP BY Sexo")
    datos = cursor.fetchall()
    conexion.close()

    etiquetas = [fila[0] for fila in datos]
    cantidad = [fila[1] for fila in datos]

    plt.pie(cantidad, labels=etiquetas, autopct='%1.1f%%', startangle=140)
    plt.title("Distribución de Género")
    plt.show()

def grafico_lineas_consumo():
    conexion = conectar()
    cursor = conexion.cursor()
    cursor.execute("SELECT Edad, SUM(BebidasSemana) FROM ENCUESTA GROUP BY Edad ORDER BY Edad")
    datos = cursor.fetchall()
    conexion.close()

    edades = [fila[0] for fila in datos]
    consumo = [fila[1] for fila in datos]

    plt.plot(edades, consumo, marker='o', color='green')
    plt.xlabel("Edad")
    plt.ylabel("Total de Bebidas Consumidas")
    plt.title("Consumo de Bebidas por Edad")
    plt.grid()
    plt.show()
