from fastapi import APIRouter;
from routes.auth import auth_router;
from routes.documents.documents import doc_router
api_router = APIRouter()

@api_router.get('/')
async def root(name:str = 'Jinish', age:int = 22):
    return {
        'name':name,
        'age': age
    }

api_router.include_router(auth_router, prefix='/auth');
api_router.include_router(doc_router, prefix='/documents');
