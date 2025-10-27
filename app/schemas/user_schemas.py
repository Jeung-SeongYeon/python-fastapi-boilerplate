"""사용자 관련 스키마"""
from pydantic import BaseModel, EmailStr
from typing import Optional
from datetime import datetime


class UserBase(BaseModel):
    """사용자 기본 스키마"""
    username: str
    email: EmailStr
    full_name: Optional[str] = None


class UserCreate(UserBase):
    """사용자 생성 스키마"""
    pass


class UserUpdate(BaseModel):
    """사용자 업데이트 스키마"""
    username: Optional[str] = None
    email: Optional[EmailStr] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None


class UserInDB(UserBase):
    """데이터베이스 사용자 스키마"""
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True


class UserResponse(UserBase):
    """사용자 응답 스키마"""
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None


class ItemBase(BaseModel):
    """아이템 기본 스키마"""
    title: str
    description: Optional[str] = None


class ItemCreate(ItemBase):
    """아이템 생성 스키마"""
    owner_id: int


class ItemUpdate(BaseModel):
    """아이템 업데이트 스키마"""
    title: Optional[str] = None
    description: Optional[str] = None
    is_active: Optional[bool] = None


class ItemResponse(ItemBase):
    """아이템 응답 스키마"""
    id: int
    is_active: bool
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    
    class Config:
        from_attributes = True
