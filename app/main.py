"""FastAPI 메인 애플리케이션"""
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from api.v1 import users, items
from database.session import init_db
from database.models import Base

# FastAPI 앱 인스턴스 생성
app = FastAPI(
    title="FastAPI Boilerplate",
    description="FastAPI 보일러플레이트 프로젝트",
    version="1.0.0"
)

# 데이터베이스 초기화
@app.on_event("startup")
def startup_event():
    """애플리케이션 시작 시 실행"""
    init_db()


# 정적 파일 마운트
app.mount("/static", StaticFiles(directory="app/template"), name="static")

# API 라우터 등록
app.include_router(users.router, prefix="/api/v1")
app.include_router(items.router, prefix="/api/v1")


@app.get("/", response_class=HTMLResponse)
def read_root():
    """루트 엔드포인트"""
    return """
    <html>
        <head>
            <title>FastAPI Boilerplate</title>
        </head>
        <body>
            <h1>FastAPI Boilerplate</h1>
            <p>Welcome to FastAPI Boilerplate!</p>
            <ul>
                <li><a href="/docs">Swagger UI</a></li>
                <li><a href="/redoc">ReDoc</a></li>
                <li><a href="/api/v1/users/">Users API</a></li>
                <li><a href="/api/v1/items/">Items API</a></li>
            </ul>
        </body>
    </html>
    """


@app.get("/health")
def health_check():
    """Health check 엔드포인트"""
    return {"status": "healthy"}
