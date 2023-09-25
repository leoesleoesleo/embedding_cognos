#
# Demo Embedding Cognos Python
## &nbsp; [![pyVersion38](https://img.shields.io/badge/python-3.8.0-blue.svg)](https://www.python.org/download/releases/3.7/)

## Flujo del proceso
<p align="justify">
Diagrama de contexto
</p>
<div align="center">
<img height="200" src="https://leoesleoesleo.github.io/imagenes/flujo_cognos.png" alt="Flujo Cognos">
</div>
<p align="justify">
El alcance es poder embeber reportes de IBM Cognos en una plicación externa	
</p>

## Manual de instalación

- Clonar repositorio
	```
	git clone https://github.com/leoesleoesleo/03_project_.git
	```

- Crear archivo de variables de entorno .env basado en .env.example
	```
  	cp .env_example .env
 	```

### Usando Docker (Opcional)

- Levantar contenedor Docker
	```
	docker-compose -p project up --build
	```

- Entrar al contenedor en modo bash
	```
	docker-compose -p project run web bash
	```
### Usando Entorno Virtual (Opcional)
- Crear entorno virtual

  Ejemplo anaconda
	```
	conda create -n env python=3.7
	```
	```
	conda activate venv
	```

  Ejemplo virtualenv
  ```
	pip install virtualenv
	```
	```
	python3 -m venv env
	```
	```
	source env/bin/activate
	```
	
- Navegar hasta la carpeta del proyecto en la carpeta requirements para instalar dependencias
    ```
    pip install -r requirements.txt
    ```

### Correr la aplicación
 - Importar la collection de postman para usar los servicios más rápido
 - Ejecutar aplicación desde NGROK con el fin de generar una url con certificados válidos (https) para que las imagenes puedan cargar con los certificados de seguridad, ejemplo: https://93ab-190-71-54-186.ngrok-free.app/generate_report
 - Nota: para que las imagenes carguen correctamente ademas de correr la aplicación en https, tambien será necesario hacer el logueo desde cognos.
   
