"""데이터베이스 세션 관리 및 ORM 설정"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from typing import Generator
import os

# SQLite 데이터베이스 URL (프로덕션에서는 환경변수로 관리)
SQLALCHEMY_DATABASE_URL =os.getenv("DATABASE_URL")

# 데이터베이스 엔진 생성
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    connect_args={"check_same_thread": False}  # SQLite 전용
)

# 세션 팩토리 생성
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# ORM 기본 클래스
Base = declarative_base()


def get_db() -> Generator:
    """데이터베이스 세션 생성 및 관리 (의존성 주입)"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    """데이터베이스 초기화 (테이블 생성)"""
    Base.metadata.create_all(bind=engine)
