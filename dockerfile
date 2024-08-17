# Usa una imagen base oficial de Python
FROM python:3.12-slim

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia los archivos de tu proyecto al directorio de trabajo
COPY . /app

# Instala las dependencias desde requirements.txt si existe
RUN pip install --no-cache-dir --upgrade pip
RUN if [ -f requirements.txt ]; then pip install -r requirements.txt; fi

# Define el comando por defecto para ejecutar el script
CMD ["python3", "main.py"]