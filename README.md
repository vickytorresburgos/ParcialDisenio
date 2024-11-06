
# Mutant Detector API

Este proyecto es una API REST que permite detectar si una secuencia de ADN corresponde a un mutante. La API evalúa secuencias de ADN y guarda los resultados en una base de datos PostgreSQL. También proporciona estadísticas sobre el número de mutantes y humanos verificados.



Este proyecto utiliza:

- Python 3.10
- Flask
- SQLAlchemy
- PostgreSQL
- Docker y Docker Compose

## Requisitos

- Python 3.10 o superior
- PostgreSQL
- Docker 

## Instalación

1. **Clona el repositorio**:
 
   git clone <git@github.com:vickytorresburgos/MutantDetector.git>
   
   cd MutantDetector

2. **Configura un entorno virtual**:
  
   python3 -m venv venv
   source venv/bin/activate  

3. **Instala las dependencias**:
   
   pip install -r requirements.txt

4. **Configura PostgreSQL**: Crea una base de datos PostgreSQL llamada `mutantes` y un usuario con permisos para acceder a ella.

   CREATE DATABASE mutantes;
   CREATE USER user WITH PASSWORD 'password';
   GRANT ALL PRIVILEGES ON DATABASE mutantes TO user;

## Variables de Entorno

Crea un archivo `.env` en la raíz del proyecto y define las variables de conexión a la base de datos:

POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=mutantes
POSTGRES_USER=user
POSTGRES_PASSWORD=password

## Uso

1. **Ejecuta la aplicación**:
   
   python3 app.py

2. La API estará disponible en `http://127.0.0.1:8000`.

## Uso con Docker

Para ejecutar el proyecto usando Docker y Docker Compose:

1. **Configura el archivo `docker-compose.yml`** (el archivo ya está configurado con una red `mutant-network`, servicios para la base de datos y la API, y un volumen persistente).

2. **Inicia los servicios con Docker Compose**:
   ```bash
   docker-compose up --build -d
   ```

3. La API estará disponible en `http://localhost:8000`, y PostgreSQL estará en `localhost:5433`.

## Endpoints

### 1. Detectar Mutantes

**URL**: `/mutant/`  
**Método**: `POST`

**Body** (JSON):
```json
{
    "dna": ["ATGCGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
}
```

**Respuesta**:
- **200 OK** si el ADN pertenece a un mutante.
- **403 Forbidden** si el ADN no pertenece a un mutante.

### 2. Estadísticas

**URL**: `/stats`  
**Método**: `GET`

**Respuesta**:
```json
{
    "ADN Mutante": 1,
    "ADN Humano": 0,
    "ratio": 1.0
}
```

## Autores

Proyecto desarrollado por Victoria Torres.

