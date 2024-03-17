from fastapi import APIRouter;
from routes.documents.toDoList import todo_router
doc_router = APIRouter()

@doc_router.get('/')
def root(index: int=1, title: str='todo title', description: str = 'to-do-description', done: bool=False):
    return {
        'index': index,
        'title':title,
        'description': description,
        'done': False
    }
doc_router.include_router(todo_router, prefix='/toDoList')
