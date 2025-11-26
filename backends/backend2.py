from fastapi import FastAPI
import time
app = FastAPI()


@app.get("/")
async def backend_server_2():
    time.sleep(1)
    return "Hello from Server 2"
