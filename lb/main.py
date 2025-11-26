from fastapi import FastAPI
import httpx

app = FastAPI()

# List of backend servers
servers = [
    "http://localhost:9001/server1",
    "http://localhost:9002/server2",
    "http://localhost:9003/server3",
]

# Creating index for round robin
index = 0


@app.get("/")
async def load_balancer():
    global index

    # Pick backend using round robin
    backend = servers[index]
    index = (index + 1) % len(servers)

    # Forward request to backend
    async with httpx.AsyncClient() as client:
        response = await client.get(backend)

    return {"backend_used": backend, "response": response.text}
