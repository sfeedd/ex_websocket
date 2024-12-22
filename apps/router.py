from fastapi import APIRouter, WebSocket
from typing import Dict

router = APIRouter()

# 연결된 클라이언트와의 웹소켓 객체를 관리하는 딕셔너리
active_connections: Dict[int, WebSocket] = {}

# 웹소켓 대화 엔드포인트
@router.websocket("/ws/{user_id}")
async def websocket_endpoint(websocket: WebSocket, user_id: int):
    await websocket.accept()  # 클라이언트의 웹소켓 연결을 승인
    active_connections[user_id] = websocket  # 연결된 클라이언트를 딕셔너리에 추가

    # 사용자에게 처음 인사
    await websocket.send_text(f"Hello, User {user_id}!")

    try:
        while True:
            # 클라이언트로부터 메시지를 수신
            message = await websocket.receive_text()
            if message.lower() == "exit":
                # 'exit' 메시지가 오면 연결 종료
                await websocket.send_text("Goodbye!")
                break

            # 메시지를 상대방에게 전송 (예시: 사용자 2에게 메시지 전송)
            recipient_id = 2 if user_id == 1 else 1  # 메시지를 받을 상대방의 ID 설정
            if recipient_id in active_connections:
                await active_connections[recipient_id].send_text(f"User {user_id}: {message}")
            else:
                await websocket.send_text(f"User {recipient_id} is not connected.")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        del active_connections[user_id]  # 연결 종료 후 클라이언트 제거
        await websocket.close()  # 연결 종료
