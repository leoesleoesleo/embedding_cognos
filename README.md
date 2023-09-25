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

- Estrucutra de las cookies
	```
	{
            'cam_passport': 'MTsxMDE6ZDg4NDAzMDgtMTU0ZS04OTBhLTM5YzgtYmU1NDMzOTE2Y2MyOjEwNjI5OTUwMjY7MDszOzA7',
            'up': 'H4sIAAAAAAAAAGWR3UoDMRBGX0Vyrbi9ULF3xVqrVK10RRBBJsl0mzbJLMlsbRHf3Yk/VRRykTlJTr5MXhW7gI8U8XKo+moQMDkDT4fn/nkGfg2WktpXc0oBWNbH9fVE6rxyUaozSi0lYBTkck3kNaQhmRVa1efU4b7SYFZNoi7aGebsKE6oaVxs5HTv9KQ6qHoy9qqq/zGKekEvYxc5y44yH3gvtMuYbiCgQN8Cu0gCedsWAMaInwUsKOAUmgKlEl6u1M473o4QuEso1jn4jCXvIFLcBup+WJvIdoYnZMAXCcZdIGsx3uolGv6lkFeqTX2/uKr93bGt26Ve9rK5GFXwcLSWoyaEKSUG/xlIu6FLYpAugP8OdB5B+9KvL6nFOXSe/z3WUGSMf7JpyFjjhnfe8oUdk3p7B9EIEt/YAQAA', 
            'usersessionid': 'AggAAAASPhdlAAAAAAoAAABNnVTuTJ5fR9rHFAAAAOu/Qt44unGzFEQ0HwNWVv+5GcE1BwAAAFNIQS0yNTYgAAAAcveQmKlNTJ4cI6Wlgv8uynilTmiBBXDt16K8BxefeCA=',
            'CRN': 'http%3A%2F%2Fdeveloper.cognos.com%2Fceba%2Fconstants%2FbiDirectionalOptionEnum%23biDirectionalFeaturesEnabled%3Dfalse%26showWelcomePage%3Dtrue%26isToolbarDocked%3Dtrue%26timeZoneID%3DAmerica%252FEl_Salvador%26showOptionSummary%3Dtrue%26showHiddenObjects%3Dfalse%26format%3DHTML%26skin%3Dcorporate%26contentLocale%3Den%26linesPerPage%3D15%26automaticPageRefresh%3D30%26backgroundSessionLogging%3D1970-01-01%2B00%253A00%253A00%26columnsPerPage%3D3%26http%3A%2F%2Fdeveloper.cognos.com%2Fceba%2Fconstants%2FsystemOptionEnum%23accessibilityFeatures%3Dfalse%26listViewSeparator%3Dnone%26productLocale%3Den%26showHints%3DshowAll%26displayMode%3Dlist%26',
            'cea-ssa': 'false', 
            'userCapabilities': 'f%3Bfdbffc6d%3Bf07c1faf%3Bff27defa%26AwcAAABTSEEtMjU2FAAAAOu%2FQt44unGzFEQ0HwNWVv%2B5GcE1Kp3zwkHAwRd2UC%2FRq%2FKEjxOutt7T%2FcEIS1LwCzl22cY%3D',
            'userCapabilitiesEx': 'ffef9fff%3Bf%3Bfdbffc6d%3Bf07c1faf%3Bff27defa%26AhQAAADrv0LeOLpxsxRENB8DVlb%2FuRnBNQcAAABTSEEtMjU2IAAAAJijCXFRp05vjWLS%2FsaiYdWu994qvWLU3ep%2FaBqXHmlI',
            'XSRF-TOKEN': 'lL_gI1Zjo3v_Ybrj84nVFtJwroXv8iHx',
            
            'abuse_interstitial': 'cd61-155-190-18-7.ngrok-free.app',
            'caf': 'CAFW00000128Q0FGQTYwMDAwMDAwNmVBaFFBQUFEcnYwTGVPTHB4c3hSRU5COERWbGItdVJuQk5RY0FBQUJUU0VFdE1qVTJJQUFBQUVYZGRFa0dnVHV4UHV1TGNIdlBUZmMzS0E1SERxMWFmQkwtay03eWhHbWQ0NzA5NDl8MTAxOjAwNTNiN2Y0LWE4OTctYjI0My0wNDhhLTJlY2JlYTg3OTVmMjowNzc4NjI3ODk2fDEwMTpkODg0MDMwOC0xNTRlLTg5MGEtMzljOC1iZTU0MzM5MTZjYzI6MTA2Mjk5NTAyNg__',
            'MRUStorage': '%7B%22xTUhJTlQ6dTpjbj1scGF0aW5v%22%3Atrue%7D',
            'CogCacheService': '20545151307800',
        }
	```


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

### Editar urls de los reportes de Cognos desde constants.py
	```
	class UrlService(Enum):
	    URL = "https://5a3d-155-190-18-42.ngrok-free.app"
	    REPORT_1 = URL + "/bi/v1/disp/rds/reportData/report/i7E39FA1D451B46D580850BF7BBEB77D8"
	    REPORT_2 = URL + "/bi/v1/disp/rds/reportData/report/iCBE21C8C7BB745728455B368E2609788"
	    DASHBOARD_1 = URL + "/bi/?perspective=dashboard&pathRef=.public_folders%2FSamples%2F1dashboard&action=view&mode=dashboard&CAMN&ui_appbar=false&ui_navbar=false"

	```

### Correr la aplicación
 - Importar la collection de postman para usar los servicios más rápido
 - Ejecutar aplicación desde NGROK con el fin de generar una url con certificados válidos (https) para que las imagenes puedan cargar con los certificados de seguridad, ejemplo: https://93ab-190-71-54-186.ngrok-free.app/generate_report
 - Nota: para que las imagenes carguen correctamente ademas de correr la aplicación en https, tambien será necesario hacer el logueo desde cognos.
   
