# Arquitectura del proyecto

## app.py
Servidor FastAPI con endpoints:
- `/` estado del servidor
- `/divide` división de dos números
- `/square` calcula el cuadrado

Registra errores en `server_errors.log`.

## test_app.py
Pruebas unitarias con Pytest.
Sirven como barrera antes de hacer commits.

## monitor.py
Monitoriza el servidor.
Si detecta un error HTTP 500, llama a Claude Code para revisar logs, corregir `app.py` y ejecutar `pytest`.

## server_errors.log
Archivo de logs con errores del servidor.