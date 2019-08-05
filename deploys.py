from database import Database
import json
from pprint import pprint

class Singleton:
    # Here will be the instance stored.
    __instance = Database("deploys.sqlite")

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

def getEngineers():
    dbObj=Singleton.getInstance()
    rows=dbObj.get('deploys','engineer')
    items=[]
    for row in rows:
        items.append(row[0])
    return (json.dumps({'engineers':items}))

def getEventsByEngineer(name):
    dbObj = Singleton.getInstance()
    sql = "select id, sha, date, action from deploys where engineer='"+name+"'"
    print(sql)
    rows = dbObj.query(sql)
    po=pprint(rows)
    items = []
    for row in rows:
        items.append("id:{0}, sha:{1}, date:{2},action:{3}".format(row[0],row[1],row[2],row[3]))
    return (json.dumps({'events': items}))
