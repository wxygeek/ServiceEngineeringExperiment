import cPickle as pickle
def getSchemaIdList():
    with open('schema_num', 'r') as f:
        now = int(f.read().strip())
    return range(now)

def generateID():
    with open('schema_num','r+') as f:
        now = int(f.read().strip())
    with open('schema_num','w') as f:
        f.write(now+1)
    return now

def store(schema):
    with open(str(generateID)+'.schema','w') as f:
        f.write(pickle.dumps(schema))

def get(id):
    with open(str(id)+'.schema','r') as f:
        return pickle.loads(f.read())
