# Define la imagen base
FROM python:3.8-slim-buster

# Copia los archivos de la aplicación
COPY . /codeIA

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias
RUN pip install -r requirements.txt

# Expone el puerto 8080
EXPOSE 8080

# Especifica el comando para iniciar la aplicación
CMD ["python", "codeIA.py"]
