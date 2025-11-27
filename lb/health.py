import httpx
from lb.state import servers, set_alive, set_dead


async def check_server(server: dict):
    """
    Function to mark whether server is alive or dead
    """
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            response = await client.head(server["url"])

            if response.status_code == 200:
                set_alive(server["url"])
            else:
                set_dead(server["url"])

    except Exception:
        set_dead(server["url"])


async def run_health_checks():
    """
    Runs health checks for all servers
    """
    for server in servers:
        await check_server(server)
