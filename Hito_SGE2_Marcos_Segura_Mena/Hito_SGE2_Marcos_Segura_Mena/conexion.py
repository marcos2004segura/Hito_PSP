import mysql.connector # type: ignore

def conectar():
    try:
        conexion = mysql.connector.connect(
        host='localhost',
        port=3309,
        user='root',
        password='',
        database='ENCUESTAS',
        use_pure=True
)

        if conexion.is_connected():
            print("Conexión exitosa a la base de datos")
        return conexion
    except mysql.connector.Error as e:
        print(f"Error al conectar: {e}")
        return None

# Probar la conexión
conexion = conectar()
if conexion:
    conexion.close()
