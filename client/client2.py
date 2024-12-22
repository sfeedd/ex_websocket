import websockets
import asyncio


async def send_message():
    uri = "ws://127.0.0.1:8000/ws/2"  # 사용자 2로 설정
    async with websockets.connect(uri) as websocket:
        print("WebSocket connected as User 2!")

        # 서버로 메시지 전송
        await websocket.send("Hello from User 2!")

        while True:
            # 서버에서 받은 메시지 출력
            response = await websocket.recv()
            print(f"Received from server: {response}")

            # 메시지 보내기
            message = input("You: ")
            await websocket.send(message)
            if message.lower() == "exit":
                break


# asyncio로 클라이언트 실행
asyncio.run(send_message())
