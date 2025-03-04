import pyautogui
import time
import webbrowser
import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

# Configuración de seguridad: mover el mouse a la esquina superior izquierda detendrá el script
pyautogui.FAILSAFE = True

def buscar_en_buscador(url, tema):
    webbrowser.open(url)
    time.sleep(5)  # Tiempo de espera para que cargue la página
    pyautogui.write(f'{tema} filetype:pdf')
    pyautogui.press('enter')
    time.sleep(5)  # Esperar para ver los resultados

def iniciar_busqueda():
    tema = tema_entry.get()
    
    if not tema:
        messagebox.showwarning("Error", "Debe ingresar un tema para buscar.")
        return
    
    # URLs de los nuevos buscadores
    buscadores = {
        "Google": "https://www.google.com",
        "Bing": "https://www.bing.com",
        "DuckDuckGo": "https://duckduckgo.com",
        "Yahoo!": "https://espanol.yahoo.com/"
    }
    
    # Confirmación de inicio de búsqueda
    respuesta = messagebox.askyesno("Confirmar", f"¿Desea buscar el tema '{tema}' en todos los buscadores?")
    if not respuesta:
        return

    # Configurar la barra de progreso
    progreso['maximum'] = len(buscadores)
    progreso['value'] = 0

    # Ejecutar las búsquedas en los diferentes buscadores
    for nombre, url in buscadores.items():
        status_label.config(text=f"Buscando en {nombre}...")
        root.update()
        buscar_en_buscador(url, tema)
        progreso['value'] += 1
        root.update()

    # Mensaje de finalización
    status_label.config(text="Búsqueda completada.")
    messagebox.showinfo("Completado", "Búsqueda completada en todos los buscadores.")
    progreso['value'] = 0

# Configuración de la ventana principal (UI)
root = tk.Tk()
root.title("Buscador de PDF Automático")

# Estilo de la interfaz
style = ttk.Style()
style.configure('TButton', font=('Arial', 10))
style.configure('TLabel', font=('Arial', 10))

# Etiqueta y entrada para el tema
tema_label = ttk.Label(root, text="Ingrese el tema a buscar:")
tema_label.pack(pady=10)

tema_entry = ttk.Entry(root, width=50, font=('Arial', 12))
tema_entry.pack(pady=10)

# Botón para iniciar la búsqueda
buscar_button = ttk.Button(root, text="Iniciar Búsqueda", command=iniciar_busqueda)
buscar_button.pack(pady=10)

# Barra de progreso
progreso = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progreso.pack(pady=10)

# Etiqueta de estado
status_label = ttk.Label(root, text="", foreground="blue", font=('Arial', 10, 'italic'))
status_label.pack(pady=10)

# Ejecutar la ventana
root.geometry("400x300")
root.mainloop()
