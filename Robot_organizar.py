import os
import shutil
import time

# Carpeta que queremos organizar
carpeta_origen = r"C:\Users\jhanl\OneDrive\Desktop\Organizacion"

# Carpetas destino
categorias = {
    "Documentos": [".pdf", ".docx", ".txt", ".xlsx"],
    "Imágenes": [".jpg", ".png", ".jpeg", ".gif"],
    "Videos": [".mp4", ".avi", ".mov"],
    "Música": [".mp3", ".wav", ".flac"],
    "Ejecutables": [".exe", ".msi"],
    "Otros": []  # Si no coincide con ninguna categoría
}

# Crear las carpetas si no existen
for categoria in categorias.keys():
    ruta_destino = os.path.join(carpeta_origen, categoria)
    if not os.path.exists(ruta_destino):
        os.makedirs(ruta_destino)

def organizar_archivos():
    archivos = os.listdir(carpeta_origen)

    for archivo in archivos:
        ruta_archivo = os.path.join(carpeta_origen, archivo)

        # Verificar si es un archivo y no una carpeta
        if os.path.isfile(ruta_archivo):
            # Obtener la extensión del archivo
            _, extension = os.path.splitext(archivo)
            extension = extension.lower()

            # Determinar la categoría del archivo
            destino = "Otros"
            for categoria, extensiones in categorias.items():
                if extension in extensiones:
                    destino = categoria
                    break

            # Mover el archivo
            ruta_destino = os.path.join(carpeta_origen, destino, archivo)
            shutil.move(ruta_archivo, ruta_destino)
            print(f"Movido: {archivo} → {destino}")

while True:
    organizar_archivos()
    print("✅ Organización completa. Esperando 30 segundos para la próxima ejecución...")
    time.sleep(30)  # Espera 30 segundos antes de revisar de nuevo

"""Made by 

Jhanleer Polanco A00110107
Alexander Ravelo A00110323
Pedro Reyes A00108264
Leidy Gonzalez A00110754
"""
#