from fastapi import WebSocket, APIRouter

ws_route = APIRouter(prefix="/ws")


@ws_route.websocket("/")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message text was: {data}")