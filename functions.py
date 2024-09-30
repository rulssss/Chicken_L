import psycopg2
from tkinter import messagebox
import tkinter as tk

#################################################
#################################################
#################################################
#################################################

connection = psycopg2.connect(
host="localhost",
user="postgres",
password="",
database="chicken",
port="5432"
)
# autocommit
connection.autocommit = True

#################################################
#################################################
#################################################
#################################################

    

def traer_todos_losdatos():
    cursor= connection.cursor()
    query_data = f"SELECT name, amount FROM cajas ORDER BY box_id"
    cursor.execute(query_data)
    data = cursor.fetchall()
    cursor.close()

    return data

def ventana_confirmacion():
    resultado = tk.BooleanVar()
    
    # Crear una nueva ventana (modal)
    confirm_window = tk.Toplevel()
    confirm_window.title("Confirmación")
    confirm_window.geometry("400x200")  # Ajustar el tamaño a uno más grande
    confirm_window.config(bg="white")  # Fondo blanco, típico de ventanas de Windows
    confirm_window.grab_set()  # Bloquear la ventana principal hasta que se cierre la ventana emergente
    confirm_window.iconbitmap(r'C:\Users\mariano\Desktop\Programas\Programa (Chicken solo cajas)\icono\22266chicken_98785.ico')

    # Centrando la ventana
    screen_width = confirm_window.winfo_screenwidth()
    screen_height = confirm_window.winfo_screenheight()
    window_width = 400
    window_height = 200
    position_x = (screen_width // 2) - (window_width // 2)
    position_y = (screen_height // 2) - (window_height // 2)
    confirm_window.geometry(f"{window_width}x{window_height}+{position_x}+{position_y}")

    # Etiqueta con el mensaje
    label = tk.Label(confirm_window, text="¿Está seguro de borrar TODOS los datos?", font=("Segoe UI", 12), bg="white")
    label.pack(pady=40)  # Ajustar el espaciado para mayor separación

    # Función para manejar el botón "Sí"
    def on_yes():
        resultado.set(True)
        confirm_window.destroy()

    # Función para manejar el botón "No"
    def on_no():
        resultado.set(False)
        confirm_window.destroy()

    # Crear el marco para los botones
    button_frame = tk.Frame(confirm_window, bg="white")
    button_frame.pack(pady=20)

    # Botón "Sí" con estilo y tamaño más grande
    btn_yes = tk.Button(button_frame, text="Sí", command=on_yes, width=12, relief="flat", bg="#d7d7d7", fg="black", font=("Segoe UI", 12, "bold"))
    btn_yes.pack(side=tk.LEFT, padx=15)

    # Botón "No" con estilo y tamaño más grande
    btn_no = tk.Button(button_frame, text="No", command=on_no, width=12, relief="flat", bg="#ef3232", fg="black", font=("Segoe UI", 12, "bold"))
    btn_no.pack(side=tk.LEFT, padx=15)

    confirm_window.wait_window()

    return resultado.get()

def clear_data():
    
    v = ventana_confirmacion()
    if v:
        
        cursor = connection.cursor()
        query_clear_data = "UPDATE cajas SET amount = 0"
        cursor.execute(query_clear_data)
        cursor.close()
        messagebox.showinfo("Datos", "Datos borrados con éxito.")
        s = True
    else:
        s = False
    return s
    


