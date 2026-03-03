"""사용자 관련 API 엔드포인트"""
from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from schemas.user_schemas import UserCreate, UserUpdate, UserResponse
from core.user_service import UserService
from api.deps import get_database

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserResponse, status_code=201)
def create_user(user: UserCreate, db: Session = Depends(get_database)):
    """사용자 생성"""
    return UserService.create_user(db, user)


@router.get("/", response_model=List[UserResponse])
def get_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_database)
):
    """사용자 목록 조회"""
    return UserService.get_users(db, skip=skip, limit=limit)


@router.get("/{user_id}", response_model=UserResponse)
def get_user(user_id: int, db: Session = Depends(get_database)):
    """사용자 조회"""
    return UserService.get_user(db, user_id)


@router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_database)):
    """사용자 업데이트"""
    return UserService.update_user(db, user_id, user)


@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_database)):
    """사용자 삭제"""
    UserService.delete_user(db, user_id)
    return None
