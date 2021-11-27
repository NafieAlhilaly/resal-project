from typing import Any
from fastapi import FastAPI, File, UploadFile, BackgroundTasks, HTTPException, WebSocket
from fastapi.responses import HTMLResponse
from app import services
from io import StringIO
import pandas as pd

app = FastAPI()

@app.post("/upload", status_code=202)
async def upload(background_tasks: BackgroundTasks, file: UploadFile = File(...)) -> Any:

    """
    Endpoint accepts a File request expected to be a csv file, it will check if it csv or not
    using service.is_csv()
    if it is not a csv an exception will raise
    if it is a csv file it will be proccessed as a background task and send a notification when it finish

    """
    if not services.is_csv(file.filename):
        raise HTTPException(status_code=415, detail="Not a csv file")
        
    background_tasks.add_task(services.handle_file, file.file.read(), True)
    return {"message": "file received, processing your file, you'll be notified when we finish proccessing"}


html = """
<!DOCTYPE html>
<html>
    <head>
        <title>Chat</title>
    </head>
    <body>
        <h1>WebSocket Chat</h1>
        <form action="" onsubmit="sendMessage(event)">
            <input type="file" id="messageText" autocomplete="off"/>
            <button>Send</button>
        </form>
        <ul id='messages'>
        </ul>
        <script>
            var ws = new WebSocket("ws://localhost:8000/ws");
            ws.onmessage = function(event) {
                var messages = document.getElementById('messages')
                var message = document.createElement('li')
                var content = document.createTextNode(event.data)
                message.appendChild(content)
                messages.appendChild(message)
            };
            function sendMessage(event) {
                var input = document.getElementById("messageText")
                ws.send(input)
                event.preventDefault()
            }
        </script>
    </body>
</html>
"""

@app.get("/", status_code=200)
async def main() -> Any:
    """ a smple html form to recieve files/messages from"""
    return HTMLResponse(html)

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket) -> Any:
    """ a websocket """

    await websocket.accept()
    while True:
        data = await websocket.receive_bytes()
        df = pd.read_csv(StringIO(data))
        print(df)

