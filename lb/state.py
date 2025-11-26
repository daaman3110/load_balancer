# List of servers
servers = [
    {"url": "http://localhost:9001", "alive": True, "latency": 99999},
    {"url": "http://localhost:9002", "alive": True, "latency": 99999},
    {"url": "http://localhost:9003", "alive": True, "latency": 99999},
]


# Update latency values
def update_latency_values(server_url: str, new_latency: int) -> None:
    """Updates the latency of server

    Args:
        server_url (str): URL of Server
        new_latency (int): New latency that is calculated
    """
    for server in servers:
        if server["url"] == server_url:
            server["latency"] = new_latency
            break


# Updating the state of server
def set_alive(server_url: str) -> None:
    """Sets the particular server as alive

    Args:
        server_url (str): URL of server
    """
    for server in servers:
        if server["url"] == server_url:
            server["alive"] = True
            break


def set_dead(server_url: str) -> None:
    """Sets the particular server as dead

    Args:
        server_url (str): URL of Server
    """
    for server in servers:
        if server["url"] == server_url:
            server["alive"] = False
            break
