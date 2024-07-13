import os
import qrcode

# Datos que quieres codificar en el QR
datos = "http://127.0.0.1:5500/menu.html#"

# Generar objeto QRCode
codigo = qrcode.make(datos)

# Ruta a la carpeta de Imágenes en OneDrive
ruta_imagenes = "C:\\Users\\leono\\OneDrive\\Images"

# Nombre del archivo a guardar
nombre_archivo = 'FR_qr_la_cuestecita.png'

# Ruta completa del archivo
ruta_archivo = os.path.join(ruta_imagenes, nombre_archivo)

# Guardar el código QR en un archivo PNG en la carpeta de Imágenes
codigo.save(ruta_archivo)

print(f"Código QR generado y guardado como '{ruta_archivo}'")

# Verificar si el archivo existe y reemplazar si es necesario
if os.path.exists(ruta_archivo):
    print(f"El archivo '{nombre_archivo}' ya existe en la carpeta de Imágenes.")
    print(f"Reemplazando el archivo existente...")
    codigo.save(ruta_archivo)
    print(f"Archivo '{nombre_archivo}' reemplazado correctamente.")
else:
    print(f"Archivo '{nombre_archivo}' guardado por primera vez en la carpeta de Imágenes.")
