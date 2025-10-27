# python-fastapi-boilerplate

FastAPI 기반 백엔드 프로젝트 보일러플레이트입니다.

프로젝트의 기본 구조는 아래와 같습니다.

```
python-fastapi-boilerplate/
│
├── app/
│   ├── api/
│   │   ├── v1/
│   │   │   ├── users.py      # 사용자 API 엔드포인트
│   │   │   └── items.py      # 아이템 API 엔드포인트
│   │   └── deps.py           # 의존성 관리
│   ├── core/
│   │   └── user_service.py   # 사용자 도메인 서비스
│   ├── database/
│   │   ├── models.py         # SQLAlchemy 모델 정의
│   │   ├── session.py        # DB 세션 관리
│   ├── infra/
│   │   └── utils.py          # 공통 유틸리티
│   ├── schemas/
│   │   └── user_schemas.py   # Pydantic 스키마 정의
│   ├── template/
│   │   └── template.html     # 기본 HTML 템플릿
│   └── main.py               # 애플리케이션 진입점
│
├── requirements.txt          # Python 패키지 명세
└── README.md                 # 프로젝트 설명 파일
```

## 실행 절차

1. 패키지 설치
   ```bash
   pip install -r requirements.txt
   ```

2. 서버 실행
   ```bash
   uvicorn app.main:app --reload
   ```

3. 엔드포인트 접속
   - Swagger UI: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## 사용 예시

### 사용자 목록 조회

```http
GET /api/v1/users/
```

### 사용자 생성

```http
POST /api/v1/users/
Content-Type: application/json

{
  "email": "user@example.com",
  "full_name": "홍길동",
  "password": "supersecret"
}
```