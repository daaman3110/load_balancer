from fastapi import FastAPI
import time

app = FastAPI()


@app.get("/")
async def backend_server_1():
    time.sleep(5)
    return "Hello From Server 1"
