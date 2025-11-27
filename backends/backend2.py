from fastapi import FastAPI
import time
import asyncio

app = FastAPI()


@app.get("/")
async def backend_server_2():
    await asyncio.sleep(0.8)
    return "Hello from Server 2"
