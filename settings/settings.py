import os
from dotenv import load_dotenv

load_dotenv()


# Credeniales Cognos
USER_COGNOS = os.environ.get('USER_COGNOS')
PASSWORD_COGNOS = os.environ.get('PASSWORD_COGNOS')

# Configuración del servidor
HOST = '0.0.0.0'
PORT = 5000

