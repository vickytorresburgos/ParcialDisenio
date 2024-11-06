# usa la imagen base de python 3.10 para crear el contenedor

FROM python:3.10 

# directorio de trabajo dentro del contenedor

WORKDIR /mutant_app

# copia los archivos del directorio al directorio que esta en el contenedor

COPY /mutant_app /mutant_app/

# instala las dependencias

RUN pip install --no-cache-dir -r requirements.txt

# expone el puerto para acceder a la aplicacion

EXPOSE 8000

# evita que python escriba en el buffer -> util para depuracion

ENV PYTHONUNBUFFERED=1

# comando para ejecutar la aplicacion

CMD ["python", "app.py"]