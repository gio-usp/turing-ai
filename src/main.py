#!/usr/bin/env python3
from config import getConfig
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from time import sleep

app = FastAPI()
health = None
graciously_shutdown = False
db = MongoClient(getConfig().DATABASE_URI, server_api=ServerApi('1'))

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Welcome to Turing AI API."}

@app.get("/health")
async def health_check():
    return {"status": "healthy" if db.admin.command('ping') else "unhealthy"}

        
def main(config):
    print(f"Running on environment `{config.ENV}` on port {config.PORT}")

    

if __name__ == "__main__":
    main(getConfig())