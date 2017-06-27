from pymongo import MongoClient as mc

client = mc("10.222.29.153",27017)
db = client.ooclT
db.collection_names(include_system_collections=False)
coll = db.IPConfig

def addRecord(record):
    coll.insert(record)
    mc.close(self=db)

def removeRecord(record):
    if(record):
        coll.remove(record)
    else:
        coll.remove()
        mc.close(self=db)


'''
criteria: 需要被更新的条件表达式
objNew: 更新表达式
upsert: 如目标记录不存在，是否插入新文档。
multi: 是否更新多个文档。
'''
def updateRecord(criteria,objNew,upsert,mult):
    coll.update(criteria,objNew,upsert,mult)

def findOneRecord(condition):
    result = coll.find_one(condition)
    mc.close(self=db)
    return result


def findLimitedRecord(condition,limit):
    result = []
    if(limit=="*" or limit):
        if(condition):
            result = coll.find(condition)
        else:
            result = coll.find()
    else:
        if(condition):
            result = coll.find(condition).limit(limit)
        else:
            result = coll.find().limit(limit)
    mc.close(self=db)

    return result






