"""사용자 서비스 - 비즈니스 로직"""
from sqlalchemy.orm import Session
from typing import List, Optional
from schemas.user_schemas import UserCreate, UserUpdate, ItemCreate, ItemUpdate, UserResponse, ItemResponse
from crud.user_crud import UserRepository, ItemRepository
from fastapi import HTTPException, status


class UserService:
    """사용자 서비스"""
    
    @staticmethod
    def get_user(db: Session, user_id: int) -> UserResponse:
        """사용자 조회"""
        user = UserRepository.get_user(db, user_id)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return UserResponse.model_validate(user)
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[UserResponse]:
        """이메일로 사용자 조회"""
        user = UserRepository.get_user_by_email(db, email)
        if not user:
            return None
        return UserResponse.model_validate(user)
    
    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[UserResponse]:
        """사용자 목록 조회"""
        users = UserRepository.get_users(db, skip=skip, limit=limit)
        return [UserResponse.model_validate(user) for user in users]
    
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> UserResponse:
        """사용자 생성"""
        # 중복 체크
        existing_user = UserRepository.get_user_by_email(db, user.email)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        
        existing_user = UserRepository.get_user_by_username(db, user.username)
        if existing_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already taken"
            )
        
        db_user = UserRepository.create_user(db, user)
        return UserResponse.model_validate(db_user)
    
    @staticmethod
    def update_user(db: Session, user_id: int, user_update: UserUpdate) -> UserResponse:
        """사용자 업데이트"""
        # 중복 체크
        if user_update.email:
            existing_user = UserRepository.get_user_by_email(db, user_update.email)
            if existing_user and existing_user.id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Email already registered"
                )
        
        if user_update.username:
            existing_user = UserRepository.get_user_by_username(db, user_update.username)
            if existing_user and existing_user.id != user_id:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Username already taken"
                )
        
        db_user = UserRepository.update_user(db, user_id, user_update)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return UserResponse.model_validate(db_user)
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """사용자 삭제"""
        success = UserRepository.delete_user(db, user_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        return success


class ItemService:
    """아이템 서비스"""
    
    @staticmethod
    def get_item(db: Session, item_id: int) -> ItemResponse:
        """아이템 조회"""
        item = ItemRepository.get_item(db, item_id)
        if not item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item not found"
            )
        return ItemResponse.model_validate(item)
    
    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[ItemResponse]:
        """아이템 목록 조회"""
        items = ItemRepository.get_items(db, skip=skip, limit=limit)
        return [ItemResponse.model_validate(item) for item in items]
    
    @staticmethod
    def get_items_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 100) -> List[ItemResponse]:
        """소유자별 아이템 조회"""
        items = ItemRepository.get_items_by_owner(db, owner_id, skip=skip, limit=limit)
        return [ItemResponse.model_validate(item) for item in items]
    
    @staticmethod
    def create_item(db: Session, item: ItemCreate) -> ItemResponse:
        """아이템 생성"""
        # 소유자 존재 여부 확인
        owner = UserRepository.get_user(db, item.owner_id)
        if not owner:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Owner not found"
            )
        
        db_item = ItemRepository.create_item(db, item)
        return ItemResponse.model_validate(db_item)
    
    @staticmethod
    def update_item(db: Session, item_id: int, item_update: ItemUpdate) -> ItemResponse:
        """아이템 업데이트"""
        db_item = ItemRepository.update_item(db, item_id, item_update)
        if not db_item:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item not found"
            )
        return ItemResponse.model_validate(db_item)
    
    @staticmethod
    def delete_item(db: Session, item_id: int) -> bool:
        """아이템 삭제"""
        success = ItemRepository.delete_item(db, item_id)
        if not success:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Item not found"
            )
        return success
