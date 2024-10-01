'''
import requests

def iterar_archivo(path,funcion):
    try:
        with open(path, "r") as archivo:
            for linea in archivo:
                limpio = linea.strip()
                check_status(limpio)
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as error:
        print("[Error]" + error)

def check_status(url):
    url=agregar_protocolo(url)
    try:
        respuesta = requests.get(url, timeout=5)
        print(respuesta.status_code)
    except requests.exceptions.RequestException as error:
        print(f"[Error] {error}")

def agregar_protocolo(url):
    """
    Agrega el protocolo "http" a una URL si no lo tiene.

    Args:
        url (str): La URL a procesar.

    Returns:
        str: La URL con el protocolo "http" agregado si no lo tenía.
    """
    if not url.startswith(("http://") and not url.startswith("https://")):
        url = "https://" + url
        return url
    else:
        return url

iterar_archivo("domains", check_status)
'''
import requests

def iterar_archivo(path, funcion):
    try:
        with open(path, "r") as archivo:
            for linea in archivo:
                limpio = linea.strip()
                check_status(limpio)  # Llamamos a la función con el string limpio
    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as error:
        print(f"[Error] {error}")

def check_status(url):
    url = agregar_protocolo(url)
    try:
        respuesta = requests.get(url, timeout=5)
        print(f"{url} {respuesta.status_code}")
        write_file(respuesta.status_code, url)
    except requests.exceptions.RequestException as error:
        print(f"[Error] {error}")

def agregar_protocolo(url):
    """
    Agrega el protocolo "http" a una URL si no lo tiene.

    Args:
        url (str): La URL a procesar.

    Returns:
        str: La URL con el protocolo "http" agregado si no lo tenía.
    """
    if not (url.startswith("http://") and not url.startswith("https://")):
        url = "https://" + url
        return url
    else:
        return url
    
def write_file(code,url,file="resultados.txt"):
    with  open(file, "a") as archivo:
        archivo.write(f"{code} {url}\n")

def capitaliz(string):
    print(string.upper)

iterar_archivo("domains", check_status)