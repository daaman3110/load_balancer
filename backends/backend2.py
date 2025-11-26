from fastapi import FastAPI

app = FastAPI()


@app.get("/server2")
async def backend_server_2():
    return "Hello from Server 2"
