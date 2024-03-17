from fastapi import APIRouter, Request, Response, Cookie
from models.auth_models import LoginCredentials, SignUpCredentials, Token
from fastapi.responses import JSONResponse
from datetime import datetime, timedelta, timezone
from database import db
from dotenv import load_dotenv
import bcrypt
import jwt
import os

load_dotenv()
auth_router = APIRouter()

def get_hash(password: str) -> str:
    salt = bcrypt.gensalt()
    bytecode = password.encode('utf-8');
    hash = bcrypt.hashpw(bytecode, salt);
    return hash.decode('utf-8')

def check_pw(password: str, hash: str) -> bool:
    bytecode = password.encode('utf-8');
    return bcrypt.checkpw(bytecode, hash.encode('utf-8'));

def isNotUniqueBy(username: str, unique_field:str) -> bool:
    resp = db.auth.users.find_one({f'{unique_field}':username})
    return resp != None;

def signJsonWebToken(username: str) -> str:
    payload = {
        'username':username,
        'expiry':(datetime.now()+timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    }
    token = jwt.encode(payload, os.getenv('SECRET_KEY'), algorithm="HS256")
    return token
def verify_jwt_token(token: str) -> bool:
    try:
        payload = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
        return True
    except:
        return False
    return False

def LoginAuthentication(credentials: LoginCredentials) -> dict:
    creds = credentials.dict()
    account = db.auth.users.find_one({'username': creds['username']})
    if account == None:
        return {'message':'username does not exist', 'status_code':404}
    elif check_pw(creds['password'], account['password']):
        token = signJsonWebToken(creds['username']);
        return {'message':'username found', 'token':token, 'status_code':200}
    else:
        return {'message':'invalid credentials', 'status_code':403}
    return {'message':'internal server error', 'status_code':500}

def SignUp(credentials: SignUpCredentials) -> dict:
    creds = credentials.dict();
    creds['password'] = get_hash(creds['password']);
    token = signJsonWebToken(creds['username']);
    if isNotUniqueBy(creds['username'], 'username'):
        return {'message':'username already exists', 'status_code':409}
    if isNotUniqueBy(creds['email'], 'email'):
        return {'message':'email already exists', 'status_code': 409}
    try:
        db.auth.users.insert_one(creds)
        return {'message':'user added successfully', 'status_code':200, 'token':token}
    except:
        print('some error occured')
    return {'message':'user not added', 'status_code':500}

@auth_router.post('/login')
def login(credentials: LoginCredentials, req: Request, res: Response):
    response = LoginAuthentication(credentials)
    if(response['status_code'] == 200):
        return JSONResponse(content={'message':response['message'], 'token':response['token']}, status_code=200)
    return JSONResponse(content={'message':response['message']}, status_code=response['status_code'])

@auth_router.post('/signup')
def signup(credentials: SignUpCredentials, req: Request, res: Response):
    response = SignUp(credentials)
    if(response['status_code'] == 200):
        return JSONResponse(content={'message':response['message'], 'token':response['token']}, status_code=200)
    return JSONResponse(content={'message':response['message']}, status_code=response['status_code'])

@auth_router.post("/verify-cookie")
def verify_cookie(jwt_token:Token):
    if not jwt_token or not verify_jwt_token(jwt_token.dict()['token']):
        return JSONResponse(content = {'message':'token is invalid'}, status_code=403)
    data = jwt.decode(token, os.getenv('SECRET_KEY'), algorithms=["HS256"])
    print(data)
    return JSONResponse(content = {'message':'token is valid'}, status_code=200)