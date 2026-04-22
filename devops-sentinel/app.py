from fastapi import FastAPI
import logging

app = FastAPI()

logging.basicConfig(
    filename="server_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

@app.get("/")
def home():
    return {"message": "Servidor activo"}

@app.get("/divide")
def divide(a: int, b: int):
    try:
        return {"result": a / b}
    except Exception as e:
        logging.error(f"Error en /divide con a={a}, b={b}: {str(e)}")
        raise e

@app.get("/square")
def square(x: int):
    if x < 0:
        logging.error(f"Error en /square con x={x}: valor negativo no permitido")
        raise ValueError("No se permiten valores negativos")
    return {"result": x * x}