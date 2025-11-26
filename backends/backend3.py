from fastapi import FastAPI
import time
app = FastAPI()


@app.get("/")
async def backend_server_3():
    time.sleep(7)
    return "Hello from Server 3"
