from fastapi import APIRouter, Request;
from fastapi.responses import JSONResponse
from database import db
from models.diary import DiaryEntry
from dotenv import load_dotenv
from datetime import datetime
from bson import json_util
import json
import jwt
import os
load_dotenv()
diary_router = APIRouter()

def addDiaryEntry(entry: DiaryEntry, username: str) -> dict:
    try:
        entry_dict = entry.dict();
        entry_dict['username'] = username
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        db.documents.diaryEntries.insert_one(entry_dict)
        return {'message':'entry done', 'status_code':200} 
    except:
        print('entry not done')
    return {'message':'entry not done', 'status_code':500}
def getEntries(username: str) -> dict:
    items = db.documents.diaryEntries.find({'username':username});
    items = [json.loads(json_util.dumps(item)) for item in items];
    try:
        for i in range(len(items)):
            items[i].pop('_id', None)
        return {'message': 'entries fetched', 'status_code': 200, 'todos':items}
    except:
        print('To do not fetched')
    return {'message':'entries not fetched', 'status_code':500}
def deleteEntry(index: int, username: str):
    try:
        resp = db.documents.diaryEntries.find_one({'username':username}, skip=index-1)
        db.documents.diaryEntries.delete_one({'_id':resp['_id']})
        return {'message':'deleted successful', 'status_code':200}
    except:
        print('entry not deleted')
    return {'message':'entry not deleted', 'status_code':500}
def updateEntry(entry: DiaryEntry, index: int, username: str):
    try:
        entry_dict = entry.dict()
        resp = db.documents.diaryEntries.find_one({'username':username}, skip=index-1)
        entry_dict['username']=username
        db.documents.diaryEntries.update_one({'_id':resp['_id']}, {'$set':entry_dict})
        return {'message':'updated successful', 'status_code':200}
    except:
        print('entry not updated')
    return {'message':'entry not updated', 'status_code':500}

@diary_router.get('/')
def root(index: int=1, title: str='todo title', description: str = 'to-do-description', done: bool=False):
    return {
        'index': index,
        'title':title,
        'description': description,
        'done': False
    }
@diary_router.get('/get-todos')
def get_entry(req: Request):
    if not 'auth-token' in req.headers:
        return JSONResponse(content = {'message':'auth-token not found in headers'}, status_code=403)
    token = req.headers['auth-token'];
    data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    response = getTodoItems(data['username']);
    if(response['status_code'] == 200):
        return JSONResponse(
            content={
                'message':response['message'],
                'todos':response['todos']
            }, 
            status_code=response['status_code']
        )
    return JSONResponse(content = {'message':response['message']}, status_code=response['status_code'])

@diary_router.post('/do-entry')
def do_entry(entry:DiaryEntry, req: Request):
    if not 'auth-token' in req.headers:
        return JSONResponse(content = {'message':'auth-token not found in headers'}, status_code=403)
    token = req.headers['auth-token'];
    data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    response = addDiaryEntry(entry, data['username']);
    return JSONResponse(content = {'message':response['message']}, status_code=response['status_code'])
@diary_router.delete('/delete')
def delete(index: int, req: Request):
    if not 'auth-token' in req.headers:
        return JSONResponse(content = {'message':'auth-token not found in headers'}, status_code=403)
    token = req.headers['auth-token'];
    data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    response = deleteEntry(index, data['username'])
    return JSONResponse(
        content = {
            'message':response['message']
            }, 
        status_code=response['status_code']
    )

@diary_router.get('/get-entries')
def get_todos(req: Request):
    if not 'auth-token' in req.headers:
        return JSONResponse(content = {'message':'auth-token not found in headers'}, status_code=403)
    token = req.headers['auth-token'];
    data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    response = getEntries(data['username']);
    if(response['status_code'] == 200):
        return JSONResponse(
            content={
                'message':response['message'],
                'todos':response['todos']
            }, 
            status_code=response['status_code']
        )
    return JSONResponse(content = {'message':response['message']}, status_code=response['status_code'])
@diary_router.put('/update')
def update(entry: DiaryEntry, req: Request, index: int):
    if not 'auth-token' in req.headers:
        return JSONResponse(content = {'message':'auth-token not found in headers'}, status_code=403)
    token = req.headers['auth-token'];
    data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    response = updateEntry(entry, index, data['username'])
    return JSONResponse(
        content = {
            'message':response['message']
            }, 
            status_code=response['status_code']
        )

