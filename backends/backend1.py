from fastapi import FastAPI

app = FastAPI()


@app.get("/server1")
async def backend_server_1():
    return "Hello From Server 1"
