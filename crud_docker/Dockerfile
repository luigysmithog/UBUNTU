FROM python:3.10-slim

# Crear carpeta de trabajo
WORKDIR /app

# Copiar solo el script (la DB ya está montada por volumen)
COPY crud_usuarios.py /app/crud_usuarios.py

# Instalar SQLite3 (si lo deseas usar fuera de Python también)
RUN apt-get update && apt-get install -y sqlite3

# Comando por defecto
CMD ["python", "crud_usuarios.py"]
