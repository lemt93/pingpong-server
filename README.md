# pingpong-server
"Simple" Ping Pong game server with WebSockets and Asyncio

## Prerequisite
[Docker](https://docs.docker.com/get-docker) installed with `docker-compose` CLI

## Up and Running
```
docker-compose up --build --detach --remove-orphans   // Build & start env at port 8111
docker-restart                                        // To sync code changes, just restart container
```

## Client example

```js
something.js
let ws = new WebSocket('ws://localhost:8111/')
ws.onmessage = message => console.log(message.data)
ws.send('world')                                      // hellworld
```
