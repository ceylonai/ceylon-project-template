import socketio
from ceylon import Agent
from fastapi import FastAPI
from uvicorn import Config, Server

# Create a new AsyncServer
app = FastAPI()
sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins='*')

sio_asgi_app = socketio.ASGIApp(socketio_server=sio, other_asgi_app=app)


class InterfaceAgent(Agent):

    async def run(self, inputs: "bytes"):
        @app.get("/")
        async def read_root():
            return {"message": "Hello World"}

        # Example Socket.IO event handler
        @sio.event
        async def connect(sid, environ):
            print('Client connected:', sid)

        @sio.event
        async def disconnect(sid):
            print('Client disconnected:', sid)

            # Start the Socket.IO server

        config = Config(app=sio_asgi_app, host="0.0.0.0", port=7878)
        server = Server(config)
        await server.serve()

    async def on_message(self, agent_id: "str", data: "bytes", time: "int"):
        pass
