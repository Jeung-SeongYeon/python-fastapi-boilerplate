"""아이템 관련 API 엔드포인트"""
from typing import List
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.schemas.user_schemas import ItemCreate, ItemUpdate, ItemResponse
from app.core.user_service import ItemService
from app.api.deps import get_database

router = APIRouter(prefix="/items", tags=["items"])


@router.post("/", response_model=ItemResponse, status_code=201)
def create_item(item: ItemCreate, db: Session = Depends(get_database)):
    """아이템 생성"""
    return ItemService.create_item(db, item)


@router.get("/", response_model=List[ItemResponse])
def get_items(
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_database)
):
    """아이템 목록 조회"""
    return ItemService.get_items(db, skip=skip, limit=limit)


@router.get("/{item_id}", response_model=ItemResponse)
def get_item(item_id: int, db: Session = Depends(get_database)):
    """아이템 조회"""
    return ItemService.get_item(db, item_id)


@router.get("/owner/{owner_id}", response_model=List[ItemResponse])
def get_items_by_owner(
    owner_id: int,
    skip: int = Query(0, ge=0),
    limit: int = Query(100, ge=1, le=100),
    db: Session = Depends(get_database)
):
    """소유자별 아이템 조회"""
    return ItemService.get_items_by_owner(db, owner_id, skip=skip, limit=limit)


@router.put("/{item_id}", response_model=ItemResponse)
def update_item(item_id: int, item: ItemUpdate, db: Session = Depends(get_database)):
    """아이템 업데이트"""
    return ItemService.update_item(db, item_id, item)


@router.delete("/{item_id}", status_code=204)
def delete_item(item_id: int, db: Session = Depends(get_database)):
    """아이템 삭제"""
    ItemService.delete_item(db, item_id)
    return None
