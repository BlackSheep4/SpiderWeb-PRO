FROM python:3.12-slim

WORKDIR /app

COPY . /app

# Instala las dependencias del sistema
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias de Python
RUN pip install --no-cache-dir --upgrade pip && \
    pip install -r requirements.txt

CMD ["python", "test.py"]
