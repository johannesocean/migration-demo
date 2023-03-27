"""
Created on 2022-12-08 15:19
@author: johannes
"""
import uvicorn
from fastapi import FastAPI
from app.routes import api_router

app = FastAPI(title="API-Demo")
app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run(
        app,
        host='0.0.0.0',
        port=8000,
        log_level='info',
        reload=False
    )
