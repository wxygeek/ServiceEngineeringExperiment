#coding = utf-8
import requests
import peewee
from peewee import SqliteDatabase, Model
import crap_config

db = None
api_key = 'be25bd115cd9e1e4a8ce9133527ed76b'
headers = {'apikey':api_key}

def get(url, params={}, headers=headers):
    return requests.get(url, params=params, headers=headers)

def post(url, data={}):
    return requests.post(url, data=data)

def loadConfig(conifg_file):
    import inspect
    configs = []
    config_class = [obj for name, obj in inspect.getmembers(crap_config, inspect.isclass) if name.startswith('Config_')]
    for config in config_class:
        my_config = {}
        my_config['database_name'] = config.__name__[7:]
        my_config['urls'] = {}
        my_config['params'] = {}
        for name, value in inspect.getmembers(config):
            if name.startswith('url_'):
                my_config['urls'][name[4:]] = value
            elif name.endswith('_params'):
                my_config['params'][name[:-7]] = value
        configs.append(my_config)
    return configs

modelDict = {
    'int':peewee.IntegerField,
    'float':peewee.FloatField,
    'strS':peewee.CharField,
    'strL':peewee.TextField,
    'unicode':peewee.TextField,
}
def getModelType(value):
    filed = None
    if type(value).__name__ == 'str':
        if len(value) > 255:
            filed = modelDict.get('strL')
        else :
            filed = modelDict.get('strS')
    else:
        filed = modelDict.get(type(value).__name__)
    if filed:
        return filed()
    else :
        return None

def generateTable(url, params, name, db):
    res = get(url,params)
    # class Table(Model):
    #     __name__ = name
    #     class Meta:
    #         database = db
    #
    data = res.json()
    print data.keys()
    # for k,v in data[name][0].iteritems():
    #     setattr(Table, k, getModelType(v))
    return data['total']

import cPickle as pickle
def storeData(filename, data):
    with open(filename,'ab+') as f:
        f.write(pickle.dumps(data))
    # if not data :
    #     return 0
    # row = Table()
    # for k,v in data.iteritems():
    #     if type(v).__name__ == 'unicode':
    #         setattr(row,k,v.encode('utf-8'))
    #     else :
    #         setattr(row,k,v)
    #     # print k,type(v)
    # row.save()

def crapTheData(config):
    db = SqliteDatabase(config['database_name']+'.db')
    db.connect()
    for name,url in config['urls'].iteritems():
        print name, 'craping '+url
        maxnum = generateTable(url, config['params'][name], name, db)
        print 'we need to crap',maxnum,' rows data'
        # db.create_tables([Table],safe=True)
        datalist = []
        for i in range(maxnum):
            params = config['params'][name]
            params['page'] = i
            res = requests.get(url, params ,headers=headers)
            print i, len(datalist)
            data = res.json().get('tngou')
            if data:
                datalist.append(data[0])
        storeData(config['database_name']+name+'.pic', datalist)

def main():
    configs = loadConfig(crap_config)
    print 'config loads over,there are',len(configs),' config'
    for config in configs:
        crapTheData(config)

if __name__ == '__main__':
    main()
