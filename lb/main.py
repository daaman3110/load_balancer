from fastapi import FastAPI
from lb.router import choose_best_server, mark_server_dead
from lb.state import update_latency_values
from lb.health import run_health_checks
import asyncio
import time
import httpx

app = FastAPI()


# Periodic Background Check for servers
@app.on_event("startup")
async def start_health_loop():
    asyncio.create_task(health_loop())


async def health_loop():
    while True:
        await run_health_checks()
        await asyncio.sleep(3)


@app.get("/")
async def load_balancer():
    """
    Load Balancer Logic
    """

    server = choose_best_server()

    if server is None:
        return {"error": "all servers down"}

    start_time = time.perf_counter()

    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            response = await client.get(server["url"])
    except Exception:
        mark_server_dead(server["url"])
        return {"error": f"Server {server["url"]} unreachable"}

    stop_time = time.perf_counter()

    latency = stop_time - start_time

    # Only update latency if server returned proper response
    if response.status_code == 200:
        update_latency_values(server["url"], latency)
        return response.json()

    else:
        # Server responded but with error -> Mark Dead
        mark_server_dead(server["url"])
        return {"error": f"Server {server["url"]} returned {response.status_code}"}
