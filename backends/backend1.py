from fastapi import FastAPI
import time
import asyncio

app = FastAPI()


@app.get("/")
async def backend_server_1():
    await asyncio.sleep(1.5)
    return "Hello From Server 1"
