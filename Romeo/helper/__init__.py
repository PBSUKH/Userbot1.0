from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import MongoClient 
from pyrogram import Client 
from config import MONGO_URL

r = AsyncIOMotorClient(MONGO_URL) 
j = MongoClient(MONGO_URL) 
mongodb = r.Romeo
pymongodb = r.Romeo
dbb = r["ROMEODB"]
