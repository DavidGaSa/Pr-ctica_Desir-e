import requests
import time
import subprocess

URLS = [
    "http://127.0.0.1:8000/",
    "http://127.0.0.1:8000/divide?a=10&b=0",
    "http://127.0.0.1:8000/square?x=-3"
]

def call_claude():
    prompt = """
Lee server_errors.log, identifica el error en app.py, corrígelo.
Después ejecuta pytest.
No hagas git commit si pytest falla.
Finalmente genera un breve informe de lo corregido.
"""
    subprocess.run(["claude", prompt], shell=True)

while True:
    for url in URLS:
        try:
            response = requests.get(url, timeout=5)
            if response.status_code >= 500:
                print(f"Fallo detectado en {url}")
                call_claude()
                break
        except Exception as e:
            print(f"Error al monitorizar {url}: {e}")
    time.sleep(10)