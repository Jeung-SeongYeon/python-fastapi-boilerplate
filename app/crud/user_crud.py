"""사용자 CRUD 로직"""
from sqlalchemy.orm import Session
from typing import List, Optional
from database.models import User, Item
from schemas.user_schemas import UserCreate, UserUpdate, ItemCreate, ItemUpdate


class UserRepository:
    """사용자 Repository"""
    
    @staticmethod
    def get_user(db: Session, user_id: int) -> Optional[User]:
        """ID로 사용자 조회"""
        return db.query(User).filter(User.id == user_id).first()
    
    @staticmethod
    def get_user_by_email(db: Session, email: str) -> Optional[User]:
        """이메일로 사용자 조회"""
        return db.query(User).filter(User.email == email).first()
    
    @staticmethod
    def get_user_by_username(db: Session, username: str) -> Optional[User]:
        """사용자명으로 사용자 조회"""
        return db.query(User).filter(User.username == username).first()
    
    @staticmethod
    def get_users(db: Session, skip: int = 0, limit: int = 100) -> List[User]:
        """사용자 목록 조회"""
        return db.query(User).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_user(db: Session, user: UserCreate) -> User:
        """사용자 생성"""
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    @staticmethod
    def update_user(db: Session, user_id: int, user_update: UserUpdate) -> Optional[User]:
        """사용자 업데이트"""
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            update_data = user_update.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_user, field, value)
            db.commit()
            db.refresh(db_user)
        return db_user
    
    @staticmethod
    def delete_user(db: Session, user_id: int) -> bool:
        """사용자 삭제"""
        db_user = db.query(User).filter(User.id == user_id).first()
        if db_user:
            db.delete(db_user)
            db.commit()
            return True
        return False


class ItemRepository:
    """아이템 Repository"""
    
    @staticmethod
    def get_item(db: Session, item_id: int) -> Optional[Item]:
        """ID로 아이템 조회"""
        return db.query(Item).filter(Item.id == item_id).first()
    
    @staticmethod
    def get_items(db: Session, skip: int = 0, limit: int = 100) -> List[Item]:
        """아이템 목록 조회"""
        return db.query(Item).offset(skip).limit(limit).all()
    
    @staticmethod
    def get_items_by_owner(db: Session, owner_id: int, skip: int = 0, limit: int = 100) -> List[Item]:
        """소유자별 아이템 조회"""
        return db.query(Item).filter(Item.owner_id == owner_id).offset(skip).limit(limit).all()
    
    @staticmethod
    def create_item(db: Session, item: ItemCreate) -> Item:
        """아이템 생성"""
        db_item = Item(**item.model_dump())
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item
    
    @staticmethod
    def update_item(db: Session, item_id: int, item_update: ItemUpdate) -> Optional[Item]:
        """아이템 업데이트"""
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item:
            update_data = item_update.model_dump(exclude_unset=True)
            for field, value in update_data.items():
                setattr(db_item, field, value)
            db.commit()
            db.refresh(db_item)
        return db_item
    
    @staticmethod
    def delete_item(db: Session, item_id: int) -> bool:
        """아이템 삭제"""
        db_item = db.query(Item).filter(Item.id == item_id).first()
        if db_item:
            db.delete(db_item)
            db.commit()
            return True
        return False
