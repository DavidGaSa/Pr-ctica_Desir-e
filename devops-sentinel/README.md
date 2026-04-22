# DevOps Sentinel – Monitor de Salud y Despliegue Automatizado

## Descripción
Este proyecto implementa un flujo de monitorización y diagnóstico sobre una API local desarrollada con FastAPI.
El sistema detecta errores HTTP 500, registra evidencias en logs, genera un informe técnico de diagnóstico y ejecuta pruebas unitarias para validar el comportamiento de la aplicación.

## Estructura del proyecto
- `app.py`: servidor FastAPI con fallos controlados.
- `monitor.py`: monitor de salud que detecta errores y genera evidencias.
- `test_app.py`: suite de pruebas con Pytest.
- `server_errors.log`: registro de errores detectados.
- `proposed_fix.txt`: informe de diagnóstico y propuesta de corrección.
- `pytest_result.txt`: resultado de la ejecución de pruebas.
- `refactor_report.txt`: informe de refactorización y riesgos detectados.
- `ARCHITECTURE.md`: descripción de la arquitectura del sistema.

## Ejecución

### 1. Activar entorno virtual
En Windows:
```bash
venv\Scripts\activate

### 2. Arrancar el servidor
uvicorn app:app --reload

### 3. Eejcutar el monitor
python monitor.py

### 4. Ejecutar pruebas manualmente (opcional - se ejecutan automáticamente en monitor.py)
pytest


## 5. Verifica el flujo una última vez

Para una ejecución completa:

1. levantas `uvicorn`
2. ejecutas `python monitor.py`
3. el monitor acumula 10 logs
4. se genera `server_errors.log`
5. se genera `proposed_fix.txt`
6. se genera `pytest_result.txt`

Eso es la demostración práctica principal.

---
