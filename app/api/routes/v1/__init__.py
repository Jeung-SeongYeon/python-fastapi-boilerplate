from fastapi import APIRouter
from api.routes.v1.users import router as users_router
from api.routes.v1.items import router as items_router

router = APIRouter(prefix="/v1")

#랜딩페이지
router.include_router(users_router)
router.include_router(items_router)