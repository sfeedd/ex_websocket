from fastapi import FastAPI
from .router import router  # router.py에서 라우터를 임포트

app = FastAPI()

# 라우터를 FastAPI 애플리케이션에 포함
app.include_router(router)
