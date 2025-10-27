"""유틸리티 함수들"""
from datetime import datetime
from typing import Any, Dict


def get_current_timestamp() -> datetime:
    """현재 타임스탬프 반환"""
    return datetime.utcnow()


def format_datetime(dt: datetime) -> str:
    """datetime을 문자열로 포맷팅"""
    return dt.strftime("%Y-%m-%d %H:%M:%S")


def create_response(data: Any, message: str = "Success") -> Dict[str, Any]:
    """표준 응답 형식 생성"""
    return {
        "success": True,
        "message": message,
        "data": data,
        "timestamp": get_current_timestamp().isoformat()
    }


def create_error_response(message: str, error_code: str = "UNKNOWN_ERROR") -> Dict[str, Any]:
    """표준 에러 응답 형식 생성"""
    return {
        "success": False,
        "message": message,
        "error_code": error_code,
        "timestamp": get_current_timestamp().isoformat()
    }
