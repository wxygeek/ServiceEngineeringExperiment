#!/usr/bin/python
#coding = utf-8
import requests
import peewee
from peewee import SqliteDatabase, Model
import crap_config

db = None
api_key = 'be25bd115cd9e1e4a8ce9133527ed76b'
headers = {'apikey':api_key}

def getData(arg):
    pass

def get(url, params={}, headers=headers):
    return requests.get(url, params=params, headers=headers)

def post(url, data={}):
    return requests.post(url, data=data)

def loadConfig():
    pass

def crapTheData(config):
    

def main():
    configs = loadConfig()
    for config in configs:
        crapTheData(config)

if __name__ == 'main':
    main()
