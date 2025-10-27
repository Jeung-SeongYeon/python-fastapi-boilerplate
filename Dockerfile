FROM python:3.11-slim

# 작업 디렉토리 생성 및 설정
WORKDIR /app

# 요구사항 파일 복사 및 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 앱 소스 복사
COPY . .

# uvicorn 실행 (포트 8000, 메인 모듈: app/main.py)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
