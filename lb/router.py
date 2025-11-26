from lb.state import servers, set_alive, set_dead

# 1: Setting up Round Robin
index = 0


def get_next_round_robin():
    global index

    total = len(servers)

    for i in range(total):
        server = servers[index]

        # Move to next index for next call
        index = (index + 1) % total

        if server["alive"] is True:
            return server

    return None


# 2: Getting fastest server
def get_fastest_server():
    alive_servers = []

    for server in servers:
        if server["alive"] is True:
            alive_servers.append(server)

    if not alive_servers:
        return None

    fastest = alive_servers[0]

    for s in alive_servers:
        if s["latency"] < fastest["latency"]:
            fastest = s

    return fastest


# 3: Marking server dead
def mark_server_dead(url: str) -> None:
    set_dead(url)


# 4: Marking server alive
def mark_server_alive(url: str) -> None:
    set_alive(url)


# 5: Choosing best fastest available server (Inteliigent Routing)
def choose_best_server() -> dict | None:

    # First try fastest if available
    server = get_fastest_server()
    if server is not None:
        return server

    # Then fallback to Round Robin
    server = get_next_round_robin()
    if server is not None:
        return server

    # If nothing works then
    return None
