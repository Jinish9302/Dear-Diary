from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, FileResponse, RedirectResponse
from routes.api import api_router
from dotenv import load_dotenv
import os
load_dotenv()

app = FastAPI()

# @app.get('/')
# def redirect():
#     return RedirectResponse('/app')

# app.mount("/app", StaticFiles(directory="build"))

app.include_router(api_router, prefix="/api")
