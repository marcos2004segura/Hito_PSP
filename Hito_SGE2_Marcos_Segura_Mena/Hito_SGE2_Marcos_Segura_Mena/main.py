from CRUD import crear_encuesta, leer_encuestas, actualizar_encuesta, eliminar_encuesta

try:
    # Crear una nueva encuesta
    print("Creando una nueva encuesta...")
    crear_encuesta(4, 25, 'Hombre', 10, 5, 7, 2, 1, 0, 'No', 'No', 'No', 'Alguna vez')
    print("Encuesta creada exitosamente.\n")

    # Leer todas las encuestas
    print("Leyendo todas las encuestas:")
    leer_encuestas()
    print("\n")

    # Actualizar la edad de una encuesta
    print("Actualizando la edad de la encuesta con ID 4...")
    actualizar_encuesta(4, 30)
    print("Encuesta actualizada exitosamente.\n")

    # Leer nuevamente para verificar la actualización
    print("Leyendo todas las encuestas después de la actualización:")
    leer_encuestas()
    print("\n")

    # Eliminar una encuesta
    print("Eliminando la encuesta con ID 4...")
    eliminar_encuesta(4)
    print("Encuesta eliminada exitosamente.\n")

    # Leer nuevamente para verificar la eliminación
    print("Leyendo todas las encuestas después de la eliminación:")
    leer_encuestas()

except Exception as e:
    print(f"Ocurrió un error: {e}")
