# Standard Library
import requests
import json
import os
from flask import Flask, render_template, request, jsonify, Response
from bs4 import BeautifulSoup

# Internal
from constants import UrlService
from settings.settings import HOST, PORT, USER_COGNOS, PASSWORD_COGNOS


app = Flask(__name__)

@app.route('/inicio',methods=['POST','GET'])
def inicio():
    return render_template('admin/v_ini.html')


def session_put(url):
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "parameters": [
            {"name": "CAMNamespace", "value": "MHINT"},
            {"name": "CAMUsername", "value": USER_COGNOS},
            {"name": "CAMPassword", "value": PASSWORD_COGNOS}
        ]
    }
    response = requests.put(url, headers=headers, json=data)

    if response.status_code == 201:
        return response
    else:
        return None


def get_content_items_reports(*, token: str):
    headers = {
            "IBM-BA-Authorization": token
        }
    response = requests.get(UrlService.URL.value + "/api/v1/content/team_folders/items", headers=headers)
    
    return response.content


def get_xsrf_token(*, url:str, token: str):
    params = {
        "fmt": "HTML"
    }
    headers = {
            "IBM-BA-Authorization": token
        }
    response = requests.get(url, headers=headers, params=params)
    
    return response.cookies

@app.route('/generate_report', methods=['GET'])
def generate_report(): 
    id_report = request.args.get('id')
    response_put = session_put(UrlService.URL.value + "/api/v1/session")
    if response_put:
        body = response_put.content
        body = json.loads(body.decode('utf-8'))
        token = body.get("session_key")
        cookies = response_put.cookies
                
        xsrf_token = get_xsrf_token(url=UrlService.REPORT_1.value + id_report, token=token)
                
        cookies = {
            'cam_passport': cookies.get("cam_passport"),
            'up': cookies.get("up"), 
            'usersessionid': cookies.get("usersessionid"),
            'CRN': cookies.get("CRN"),
            'cea-ssa': cookies.get("cea-ssa"), 
            'userCapabilities': cookies.get("userCapabilities"),
            'userCapabilitiesEx': cookies.get("userCapabilitiesEx"),
            'XSRF-TOKEN': xsrf_token.get("XSRF-TOKEN")
        }

        params = {
            "fmt": "HTML"
        }
        response = requests.get(UrlService.REPORT_1.value + id_report, cookies=cookies, params=params)

        
        if response.status_code in (200, 403):
            contenido_html = response.text
            
            # Crear un objeto BeautifulSoup
            soup = BeautifulSoup(contenido_html, 'html.parser')

            # Encontrar todas las etiquetas <span>
            spans = soup.find_all('span')

            # Eliminar las etiquetas <span> que no están dentro de <table>
            for span in spans:
                if span.find_parent('table') is None:
                    span.extract()

            # Obtener el contenido modificado
            contenido_html = str(soup)
            
            
            contenido_html_modificado = f'<html><body><center><h2>DEMO Embeding IBM Cognos</h2></center><div style="margin:40px;">{contenido_html}</div></body></html>'
            
            #return render_template('report.html', image_urls=img_urls[0])
            return Response(contenido_html_modificado, content_type='text/html')
        else:
            # Maneja errores de solicitud según sea necesario
            return "Error al generar el informe", response.status_code
    else:
        return "Error de autenticación en Cognos"


@app.route('/download_img', methods=['GET'])
def download_img():
    try:
        url = request.args.get('url')  # Obtener la URL de la imagen desde la solicitud JSON
        if not url:
            return jsonify({"error": "URL de imagen no proporcionada"}), 400
       
        # Obtener el nombre del archivo de la URL
        nombre_archivo = os.path.basename(url)
        
        # Descargar la imagen desde la URL
        respuesta = requests.get(url)
        if respuesta.status_code == 200:
            # Almacenar la imagen en la raíz del proyecto
            with open(nombre_archivo, 'wb') as archivo:
                archivo.write(respuesta.content)
            return jsonify({"mensaje": f"Imagen {nombre_archivo} descargada y almacenada en la raíz del proyecto."}), 200
        else:
            return jsonify({"error": "No se pudo descargar la imagen"}), 500
    except Exception as e:
        return jsonify({"error": f"Error en la descarga de la imagen: {str(e)}"}), 500


if __name__ == '__main__':
    app.run(debug=True, host=HOST, port=PORT)
