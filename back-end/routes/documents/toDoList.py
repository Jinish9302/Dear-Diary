from fastapi import APIRouter, Request;
from fastapi.responses import JSONResponse
from models.todo import Todo
from database import db
import jwt
from dotenv import load_dotenv
import os
load_dotenv()
todo_router = APIRouter()

def updateTodo(todo: Todo, index: int, username: str):
    try:
        todo_dict = todo.dict()
        resp = db.documents.toDoEntities.find_one({'username':username}, skip=index-1)
        todo_dict['username']=username
        db.documents.toDoEntities.update_one({'_id':resp['_id']}, {'$set':todo_dict})
        return {'message':'updated successful', 'status_code':200}
    except:
        print('todo not updated')
    return {'message':'todo not updated', 'status_code':500}
def deleteTodo(index: int, username: str):
    try:
        resp = db.documents.toDoEntities.find_one({'username':username}, skip=index-1)
        db.documents.toDoEntities.delete_one({'_id':resp['_id']})
        return {'message':'deleted successful', 'status_code':200}
    except:
        print('todo not deleted')
    return {'message':'todo not deleted', 'status_code':500}


def addTodoItem(todo: Todo, username: str) -> dict:
    try:
        todo_dict = todo.dict();
        todo_dict['username'] = username
        db.documents.toDoEntities.insert_one(todo_dict)
        return {'message':'Todo added', 'status_code':200} 
    except:
        print('Todo not added')
    return {'message':'Todo not added', 'status_code':500}

@todo_router.get('/')
def root(index: int=1, title: str='todo title', description: str = 'to-do-description', done: bool=False):
    return {
        'index': index,
        'title':title,
        'description': description,
        'done': False
    }

@todo_router.post('/add-todo')
def addTodo(todo: Todo, req: Request):
    if not 'auth-token' in req.headers:
        return JSONResponse(content = {'message':'auth-token not found in headers'}, status_code=403)
    token = req.headers['auth-token'];
    data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    response = addTodoItem(todo, data['username']);
    return JSONResponse(content = {'message':response['message']}, status_code=response['status_code'])

@todo_router.put('/update')
def update(todo: Todo, req: Request, index: int):
    if not 'auth-token' in req.headers:
        return JSONResponse(content = {'message':'auth-token not found in headers'}, status_code=403)
    token = req.headers['auth-token'];
    data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    response = updateTodo(todo, index, data['username'])
    return JSONResponse(content = {'message':response['message']}, status_code=response['status_code'])

@todo_router.delete('/delete')
def delete(index: int, req: Request):
    if not 'auth-token' in req.headers:
        return JSONResponse(content = {'message':'auth-token not found in headers'}, status_code=403)
    token = req.headers['auth-token'];
    data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    response = deleteTodo(index, data['username'])
    return JSONResponse(content = {'message':response['message']}, status_code=response['status_code'])

