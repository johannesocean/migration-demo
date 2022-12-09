"""
Created on 2022-12-08 15:19
@author: johannes
"""
from fastapi import APIRouter
from app.sunfeature.endpoints import router as feature_router

api_router = APIRouter(prefix="/api")
api_router.include_router(feature_router)
