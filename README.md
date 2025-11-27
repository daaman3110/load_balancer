# Python Async Load Balancer

This project is a **smart HTTP load balancer** built with Python, FastAPI, and `httpx`. It demonstrates core **backend + infra concepts** such as:

* Load balancing (round-robin + fastest-server selection)
* Latency measurement per server
* Health checks with automatic failover
* Asynchronous requests for high performance
* Periodic background tasks for server monitoring

---

## Folder Structure

```
load-balancer/
│
├── lb/
│   ├── main.py       # FastAPI entry point for the load balancer
│   ├── router.py     # Routing logic: round-robin + fastest-server
│   ├── state.py      # Stores server states, latencies, alive/dead flags
│   ├── health.py     # Health check logic, updates server states periodically
│
├── backends/
│   ├── backend1.py   # Example backend server 1
│   ├── backend2.py   # Example backend server 2
│   ├── backend3.py   # Example backend server 3
│
└── README.md
```

---

## Features

1. **Round-Robin Routing**
   Requests are distributed across alive backend servers in a round-robin manner as a fallback.

2. **Fastest Server Selection**
   The load balancer chooses the backend with the lowest latency automatically.

3. **Latency Measurement**
   Each request measures the response time and updates the server state in real-time.

4. **Health Checks**
   Periodic background checks automatically mark servers alive or dead.

5. **Retry & Failover**
   Dead servers are skipped; requests retry using next available backend.

6. **Async & High Performance**
   All networking is asynchronous with `httpx.AsyncClient`, making it suitable for high throughput.

---

## How It Works

1. On startup, the LB initializes server states.
2. Periodically, `health_loop` pings each server and updates alive/dead flags.
3. When a request arrives at `/`:

   * The LB chooses the **fastest alive server**.
   * Starts a timer.
   * Forwards the request asynchronously to the backend.
   * Stops the timer and updates latency.
   * If the backend fails or times out, the server is marked dead and the next alive server is selected.

---

## Prerequisites

* Python 3.11+
* FastAPI
* httpx
* Uvicorn

Install dependencies:

```bash
pip install fastapi httpx uvicorn
```

---

## ⚡ Running the Project

1. Start your backend servers:

```bash
uvicorn backends.backend1:app --port 9001
uvicorn backends.backend2:app --port 9002
uvicorn backends.backend3:app --port 9003
```

2. Start the load balancer:

```bash
uvicorn lb.main:app --port 8000
```

3. Test by sending requests to `http://localhost:8000/`.
   You should see responses from different backends depending on latency and round-robin selection.

---

## Project Highlights

* **Intelligent Routing:** Chooses the fastest alive server automatically.
* **Async Architecture:** Uses `asyncio` + `httpx` for non-blocking requests.
* **State Management:** Centralized server states in `state.py`.
* **Health Monitoring:** Automatic live/dead updates with periodic checks.
* **Extensible:** Easy to add weighted routing, retries, logging, or dashboard visualization.

---



