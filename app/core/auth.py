"""
Created on 2022-12-08 15:22
@author: johannes
"""
from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader
from app.core.config import settings


def api_key_auth(api_key: str = Security(
        APIKeyHeader(name='x-api-key', auto_error=False))):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
