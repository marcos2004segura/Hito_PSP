import tkinter as tk
from tkinter import messagebox
from CRUD import (
    crear_encuesta, leer_encuestas, actualizar_encuesta, eliminar_encuesta, consultar_por_edad, filtrar_consumo_alto, filtrar_perdidas_control,exportar_a_excel,grafico_barras_consumo,grafico_pastel_genero, grafico_lineas_consumo
)

# Configurar ventana principal
ventana = tk.Tk()
ventana.title("Encuestas Dr.Fernando")
ventana.geometry("700x600")
ventana.configure(bg="#f0f0f0")


# Funciones para CRUD
def crear_registro():
    try:
        id_encuesta = int(entry_id.get())
        edad = int(entry_edad.get())
        sexo = entry_sexo.get()
        bebidas_semana = int(entry_bebidas.get())
        cervezas_semana = int(entry_cervezas.get())
        bebidas_fin_semana = int(entry_bebidas_fin.get())
        bebidas_destiladas = int(entry_destiladas.get())
        vinos_semana = int(entry_vinos.get())
        perdidas_control = int(entry_control.get())
        diversion = entry_diversion.get()
        digestivos = entry_digestivos.get()
        tension = entry_tension.get()
        dolor = entry_dolor.get()

        crear_encuesta(id_encuesta, edad, sexo, bebidas_semana, cervezas_semana, bebidas_fin_semana,
                       bebidas_destiladas, vinos_semana, perdidas_control, diversion, digestivos, tension, dolor)
        messagebox.showinfo("Éxito", "Encuesta creada exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def eliminar_registro():
    try:
        id_texto = entry_id.get().strip()  # Obtener el texto del campo y eliminar espacios en blanco
        if not id_texto:
            messagebox.showwarning("Advertencia", "Por favor, ingresa un ID válido.")
            return

        id_encuesta = int(id_texto)
        respuesta = messagebox.askyesno("Confirmar", f"¿Estás seguro de que deseas eliminar la encuesta con ID {id_encuesta}?")
        if respuesta:
            eliminar_encuesta(id_encuesta)
            messagebox.showinfo("Éxito", f"Encuesta con ID {id_encuesta} eliminada exitosamente.")
        else:
            messagebox.showinfo("Cancelado", "Operación cancelada.")
    except ValueError:
        messagebox.showerror("Error", "El ID ingresado no es un número válido.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def leer_registros():
    try:
        registros = leer_encuestas()
        if registros:
            ventana_registros = tk.Toplevel(ventana)
            ventana_registros.title("Todos los Registros")

            # Crear un widget Text con barra de desplazamiento
            scrollbar = tk.Scrollbar(ventana_registros)
            scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

            text_widget = tk.Text(ventana_registros, yscrollcommand=scrollbar.set, wrap=tk.NONE, width=100, height=30)
            text_widget.pack(expand=True, fill=tk.BOTH)

            # Mostrar todos los registros en el Text widget
            for registro in registros:
                text_widget.insert(tk.END, f"{registro}\n")

            # Configurar la barra de desplazamiento
            scrollbar.config(command=text_widget.yview)
        else:
            messagebox.showinfo("Información", "No hay registros en la base de datos.")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def mostrar_consulta_por_edad():
    try:
        registros = consultar_por_edad()
        if registros:
            resultado = "\n".join([str(registro) for registro in registros])
            messagebox.showinfo("Consulta por Edad", resultado)
        else:
            messagebox.showinfo("Información", "No hay registros para mostrar.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_grafico_barras():
    try:
        grafico_barras_consumo()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_grafico_pastel():
    try:
        grafico_pastel_genero()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def mostrar_grafico_lineas():
    try:
        grafico_lineas_consumo()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Botones para gráficos
tk.Button(ventana, text="Gráfico de Barras - Consumo por Edad", command=mostrar_grafico_barras).pack(pady=10)
tk.Button(ventana, text="Gráfico de Pastel - Género", command=mostrar_grafico_pastel).pack(pady=10)
tk.Button(ventana, text="Gráfico de Líneas - Consumo por Edad", command=mostrar_grafico_lineas).pack(pady=10)

def mostrar_filtro_consumo_alto():
    try:
        registros = filtrar_consumo_alto()
        if registros:
            resultado = "\n".join([str(registro) for registro in registros])
            messagebox.showinfo("Consumo Alto de Alcohol", resultado)
        else:
            messagebox.showinfo("Información", "No se encontraron personas con consumo alto.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def exportar_registros():
    try:
        exportar_a_excel()
        messagebox.showinfo("Éxito", "Datos exportados a 'registros_encuesta.xlsx'.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Botón para exportar a Excel
tk.Button(ventana, text="Exportar a Excel", command=exportar_registros).pack(pady=10)

def mostrar_filtro_perdidas_control():
    try:
        registros = filtrar_perdidas_control()
        if registros:
            resultado = "\n".join([str(registro) for registro in registros])
            messagebox.showinfo("Pérdidas de Control", resultado)
        else:
            messagebox.showinfo("Información", "No se encontraron personas con pérdidas de control.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Campos de entrada
tk.Label(ventana, text="ID Encuesta").pack()
entry_id = tk.Entry(ventana)
entry_id.pack()

tk.Label(ventana, text="Edad").pack()
entry_edad = tk.Entry(ventana)
entry_edad.pack()

tk.Label(ventana, text="Sexo").pack()
entry_sexo = tk.Entry(ventana)
entry_sexo.pack()

tk.Label(ventana, text="Bebidas Semana").pack()
entry_bebidas = tk.Entry(ventana)
entry_bebidas.pack()

tk.Label(ventana, text="Cervezas Semana").pack()
entry_cervezas = tk.Entry(ventana)
entry_cervezas.pack()

tk.Label(ventana, text="Bebidas Fin de Semana").pack()
entry_bebidas_fin = tk.Entry(ventana)
entry_bebidas_fin.pack()

tk.Label(ventana, text="Bebidas Destiladas Semana").pack()
entry_destiladas = tk.Entry(ventana)
entry_destiladas.pack()

tk.Label(ventana, text="Vinos Semana").pack()
entry_vinos = tk.Entry(ventana)
entry_vinos.pack()

tk.Label(ventana, text="Pérdidas de Control").pack()
entry_control = tk.Entry(ventana)
entry_control.pack()

tk.Label(ventana, text="Diversión Dependencia Alcohol").pack()
entry_diversion = tk.Entry(ventana)
entry_diversion.pack()

tk.Label(ventana, text="Problemas Digestivos").pack()
entry_digestivos = tk.Entry(ventana)
entry_digestivos.pack()

tk.Label(ventana, text="Tensión Alta").pack()
entry_tension = tk.Entry(ventana)
entry_tension.pack()

tk.Label(ventana, text="Dolor de Cabeza").pack()
entry_dolor = tk.Entry(ventana)
entry_dolor.pack()

tk.Button(ventana, text="Eliminar Encuesta", command=eliminar_registro).pack(pady=10)
tk.Button(ventana, text="Actualizar Encuesta", command=actualizar_encuesta).pack(pady=5)

# Botones para CRUD
tk.Button(ventana, text="Crear Encuesta", command=crear_registro).pack(pady=10)
tk.Button(ventana, text="Mostrar Encuestas", command=leer_registros).pack(pady=10)

# Botones para consultas
tk.Button(ventana, text="Consulta por Edad", command=mostrar_consulta_por_edad).pack(pady=10)
tk.Button(ventana, text="Filtrar Consumo Alto", command=mostrar_filtro_consumo_alto).pack(pady=10)
tk.Button(ventana, text="Filtrar Pérdidas de Control", command=mostrar_filtro_perdidas_control).pack(pady=10)

# Iniciar la ventana
ventana.mainloop()
