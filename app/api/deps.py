"""API 의존성 주입"""
from typing import Generator
from fastapi import Depends
from sqlalchemy.orm import Session
from database.session import get_db


def get_database() -> Generator:
    """데이터베이스 세션 의존성"""
    yield from get_db()
