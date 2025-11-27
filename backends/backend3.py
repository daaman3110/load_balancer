from fastapi import FastAPI
import time
import asyncio

app = FastAPI()


@app.get("/")
async def backend_server_3():
    await asyncio.sleep(2)
    return "Hello from Server 3"
