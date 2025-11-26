from fastapi import FastAPI

app = FastAPI()


@app.get("/server3")
async def backend_server_3():
    return "Hello from Server 3"
