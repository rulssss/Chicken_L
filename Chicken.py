import tkinter as tk
from tkinter import ttk
from functions import *

def load_data(txt_seleccionado):
    load_window = tk.Toplevel()  # Crear nueva ventana
    load_window.title("Modificación de datos")  # Título de la ventana
    load_window.geometry("500x350")  # Tamaño de la ventana
    load_window.config(bg="white")
    load_window.iconbitmap(r'C:\Users\mariano\Desktop\Programas\Programa (Chicken solo cajas)\icono\22266chicken_98785.ico')
    load_window.grab_set()  # Bloquear la ventana principal hasta que se cierre la ventana emergente

    # Centrando la ventana
    screen_width = load_window.winfo_screenwidth()
    screen_height = load_window.winfo_screenheight()
    window_width = 500
    window_height = 350
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    load_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # Etiquetas para el mensaje
    label1 = tk.Label(load_window, text="Está modificando la cantidad de:", font=("Segoe UI", 14), bg="white")
    label1.pack(pady=10)
    
    # Etiqueta para el producto seleccionado en negrita
    label2 = tk.Label(load_window, text=txt_seleccionado, font=("Segoe UI", 14, "bold"), bg="white")
    label2.pack(pady=5)

    # Entrada para valores numéricos con fondo gris
    entry_value = tk.Entry(load_window, font=("Segoe UI", 16), justify="center", bg="#d7d7d7", width=30)
    entry_value.pack(pady=50)

    
    
    # Función para sumar
    def sumar():
        try:
            valor_actual = int(entry_value.get())
            result_text.config(state="normal")
            result_text.delete("1.0", tk.END)

            if 0 < valor_actual < 1000:

                cursor = connection.cursor()
                query_sum_data = f"UPDATE cajas SET amount = amount + {valor_actual} WHERE name = '{txt_seleccionado}'"
                cursor.execute(query_sum_data)
                cursor.close()
                
                result_text.delete("1.0", tk.END)
                mostrar_todos_datos()
                load_window.destroy()
            else:
                result_text.tag_configure("red", foreground="red", font=("Segoe UI", 20))
                result_text.insert(tk.END, "Error:\tEl resultado de la suma está fuera del rango permitido el cual es entre 1 y 999.\n", "red")
                result_text.tag_configure("red", foreground="red", font=("Segoe UI", 18))
            result_text.config(state="disabled")
            
        except ValueError:
            result_text.config(state="normal")
            result_text.insert(tk.END, "Por favor ingresa un número válido.\n", "red")
            result_text.config(state="disabled")

    # Función para restar
    def restar():
        try:
            valor_actual = int(entry_value.get())
            result_text.config(state="normal")
            result_text.delete("1.0", tk.END)

            if 0 < valor_actual < 1000:

                cursor = connection.cursor()
                query_sum_data = f"UPDATE cajas SET amount = amount - {valor_actual} WHERE name = '{txt_seleccionado}'"
                cursor.execute(query_sum_data)
                cursor.close()
                
                result_text.delete("1.0", tk.END)
                mostrar_todos_datos()
                load_window.destroy()
            else:
                result_text.tag_configure("red", foreground="red", font=("Segoe UI", 20))
                result_text.insert(tk.END, "Error:\tEl resultado de la resta está fuera del rango permitido el cual es entre 1 y 999.\n", "red")
                result_text.tag_configure("red", foreground="red", font=("Segoe UI", 18))
            result_text.config(state="disabled")

        except ValueError:
            result_text.config(state="normal")
            result_text.insert(tk.END, "Por favor ingresa un número válido.\n", "red")
            result_text.config(state="disabled")

    # Frame para los botones
    button_frame = tk.Frame(load_window, bg="white")
    button_frame.pack(pady=10)

    # Botones para sumar y restar
    btn_sumar = tk.Button(button_frame, text="Sumar", command=sumar, width=15, relief="flat", bg="#d7d7d7", fg="black", font=("Segoe UI", 14, "bold"))
    btn_sumar.pack(side=tk.LEFT, padx=20)

    btn_restar = tk.Button(button_frame, text="Restar", command=restar, width=15, relief="flat", bg="#ef3232", fg="black", font=("Segoe UI", 14, "bold"))
    btn_restar.pack(side=tk.LEFT, padx=20)

    load_data.wait_window()


def ventana_seleccion():
    resultado = tk.BooleanVar()
    txt_seleccionado = None  # Inicializar la variable

    # Crear una nueva ventana (modal)
    confirm_window = tk.Toplevel()
    confirm_window.title("Cargar datos")
    confirm_window.geometry("500x350")
    confirm_window.config(bg="white")
    confirm_window.grab_set()
    confirm_window.iconbitmap(r'C:\Users\mariano\Desktop\Programas\Programa (Chicken solo cajas)\icono\22266chicken_98785.ico')

    # Centrando la ventana
    screen_width = confirm_window.winfo_screenwidth()
    screen_height = confirm_window.winfo_screenheight()
    window_width = 500
    window_height = 350
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    confirm_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # Etiqueta con el mensaje
    label = tk.Label(confirm_window, text="Seleccione la caja que desea editar:", font=("Segoe UI", 14), bg="white")
    label.pack(pady=20)

    # Lista de opciones
    opciones = [
        "Filet de merluza comun solimeno", "Filet de merluza a la finas hierbas solimeno",
        "Filet de merluza a la romana solimeno", "Medallon de merluza grangys",
        "Medallon de merluza espinaca y queso grangys", "Medallon de merluza capresse grangys",
        "Formita marina grangys", "Rabas pop", "Medallon de pollo grangys",
        "Medallon de pollo jamon y queso grangys", "Medallon de pollo espinaca y queso grangys",
        "Patita comun grangys", "Patita de pollo jamon y queso grangys", "Dino de pollo grangys",
        "Nuggets de pollo solimeno", "Dedito de pollo a la finas hierbas", 
        "Mini pechuga de pollo al verdeo", "Mila de soja y calabaza", 
        "Bocadito de calabaza y queso grangys", "Bocadito de espinaca grangys",     
        "Croqueta de papa jamon y queso", "Barritas de muzzarella", 
        "Papas caritas Mccain", "Papas noissett Mccain"
    ]
    
    # Crear Combobox con una fuente más grande
    seleccion = ttk.Combobox(confirm_window, values=opciones, state="readonly", font=("Segoe UI", 14), width=40)
    seleccion.pack(pady=20)

    # Configuración para agrandar la fuente de las opciones desplegables
    confirm_window.option_add('*TCombobox*Listbox.font', ("Segoe UI", 12))  # Cambia el tamaño de la letra de las opciones

    # Función para manejar el botón "Aceptar"
    def on_aceptar():
        nonlocal txt_seleccionado  # Hacer que txt_seleccionado sea accesible
        if seleccion.get():
            txt_seleccionado = seleccion.get()  # Guardar la opción seleccionada
            resultado.set(True)
            confirm_window.destroy()
    
    # Botón "Aceptar"
    btn_aceptar = tk.Button(confirm_window, text="Aceptar", command=on_aceptar, width=15, relief="flat", bg="#d7d7d7", fg="black", font=("Segoe UI", 14, "bold"))
    btn_aceptar.pack(pady=20)

    confirm_window.wait_window()

    return resultado.get(), txt_seleccionado  # Devolver también el txt_seleccionado

# Incorporar la función en el botón "Cargar Datos"
def cargar_datos(txt):
    result = ventana_seleccion()  # Obtener resultado y txt_seleccionado
    if result[0]:  # Si se aceptó
        txt_seleccionado = result[1]  # Asignar txt_seleccionado

        # Mostrar ventana de carga
        load_data(txt_seleccionado)

        result_text.config(state="normal")
        result_text.delete("1.0", tk.END)
        

        result_text.tag_configure("bold", font=("Segoe UI", 20, "bold"))
        result_text.insert(tk.END, "Datos Cargados.", "bold")
        result_text.config(state="disabled")

def mostrar_todos_datos():
    all_data = traer_todos_losdatos()

    result_text.tag_configure("bold", font=("Segoe UI", 20, "bold"))
    result_text.tag_configure("red", foreground="red")

    if all_data:
        result_text.config(state="normal", font=("Segoe UI", 19))  # Habilitar edición temporalmente
        result_text.delete("1.0", tk.END)  # Limpiar el contenido del cuadro de texto

        # Insertar el encabezado con formato en negrita
        result_text.insert(tk.END, "Nombre de la caja \t | \t Cantidad  \n", "bold")
        
        
        for i in all_data:
            new_text = f"{' =  '.join(map(str, i))}\n"
            result_text.insert(tk.END, "------------------------------------------------------|\n", "bold")
            
            if i[1] < 2:
                
                result_text.insert(tk.END, new_text, "red")
                
            else:
                result_text.insert(tk.END, new_text)
            
                

        result_text.config(state="disabled")  # Deshabilitar edición

# Borrar todos los datos
def borrar_datos():
    s = clear_data()
    if s:
        result_text.config(state="normal", font=("Segoe UI", 20))  # Habilitar edición temporalmente
        result_text.delete("1.0", tk.END)  # Limpiar el contenido del cuadro de texto
        result_text.tag_configure("bold", font=("Segoe UI", 20, "bold"))
        result_text.insert(tk.END, "Datos Borrados.", "bold")
        result_text.config(state="disabled")  # Deshabilitar edición

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Gestión de Datos")
ventana.state('zoomed')
ventana.iconbitmap(r'C:\Users\mariano\Desktop\Programas\Programa (Chicken solo cajas)\icono\22266chicken_98785.ico')

style = ttk.Style()
style.configure("TNotebook.Tab", font=("Segoe UI", 12))

frame_width = 200

notebook = ttk.Notebook(ventana, style="TNotebook")
notebook.pack(side=tk.LEFT, fill=tk.BOTH, padx=10, pady=10)

frame_datos = tk.Frame(notebook, width=frame_width, padx=10, pady=10, bd=2, relief="groove")
notebook.add(frame_datos, text="Datos")
frame_datos.pack_propagate(False)

label_datos = tk.Label(frame_datos, text="Datos", font=("Arial", 14), bg="#d7d7d7")
label_datos.pack(fill=tk.X, pady=(0, 30))

btn_cargar = tk.Button(frame_datos, text="Cargar Datos", command=lambda: cargar_datos(""), width=20, height=2, bg="#d7d7d7", bd=0, fg="black", font=("Segoe UI", 10, "bold"))
btn_cargar.pack(pady=10)

btn_mostrar_todos = tk.Button(frame_datos, text="Mostrar Todos los Datos", command=mostrar_todos_datos, width=20, height=2, bg="#d7d7d7", bd=0, fg="black", font=("Segoe UI", 10, "bold"))
btn_mostrar_todos.pack(pady=10)

btn_borrar = tk.Button(frame_datos, text="Borrar Datos", command=borrar_datos, width=12, height=1, bg="#ef3232", fg="black", bd=0, font=("Segoe UI", 12, "bold"), border=4)
btn_borrar.pack(side=tk.BOTTOM, anchor="s", pady=10)

# Frame derecho para mostrar los resultados
frame_derecho = tk.Frame(ventana, padx=10, pady=10)
frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Mensaje de bienvenida en el área de resultados
welcome_label = tk.Label(frame_derecho, text="¡Bienvenido a la Tienda del Pollo!", font=("Courier New", 24, "bold"),fg="black", relief="flat")
welcome_label.pack(pady=20)

scrollbar = tk.Scrollbar(frame_derecho)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Crear el Text widget con estado no editable
result_text = tk.Text(frame_derecho, bg="white", font=("Segoe UI", 12), yscrollcommand=scrollbar.set, state="disabled", height=10)
result_text.pack(fill=tk.BOTH, expand=True)
scrollbar.config(command=result_text.yview)

ventana.mainloop()