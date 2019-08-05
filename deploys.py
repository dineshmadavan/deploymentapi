from database import Database
import json
from datetime import datetime,timedelta

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
    rows = dbObj.query(sql)
    items = []
    for row in rows:
        items.append("id:{0}, sha:{1}, date:{2},action:{3}".format(row[0],row[1],row[2],row[3]))
    return (json.dumps({'events': items}))

def getEventsByDateTime(fromDateTime,toDateTime):
    dbObj = Singleton.getInstance()
    sql = "select id, sha, action, engineer from deploys where date BETWEEN '" + fromDateTime + "' and '" + toDateTime + "'"
    rows = dbObj.query(sql)
    items = []
    for row in rows:
        items.append("id:{0}, sha:{1}, action:{2}, engineer:{3}".format(row[0],row[1],row[2],row[3]))
    return (json.dumps({'events': items}))


def getSummary(todateTime):
    """
    Function  to get the summary of events performed for the last 24 hours.
    If no date is given, the last 24 hours from the current time is used.
    :param todateTime: Date to query the database. This date - 24 hours is the duration used.
    :return: Returns the summary of the events i.e. count, count of each engineer's events and each action count.
    """
    dbObj = Singleton.getInstance()
    orig = datetime.fromtimestamp(int(todateTime))
    fromts = orig - timedelta(days=1)
    fromDate= int(fromts.timestamp())
    sql = "select id, sha, action, engineer from deploys where date BETWEEN '" + str(fromDate) + "' and '" + str(todateTime) + "'"
    rows = dbObj.query(sql)
    total =0
    engineersActions={}
    actions={}
    for row in rows:
        total+=1
        addItem(engineersActions,row[3])
        addItem(actions,row[2])
    items=[]
    engineers=[]
    actionsList=[]
    items.append("Total Events:{0}".format(total))
    for key in actions:
        actionsList.append("{0}:{1}".format(key,actions[key]))
    for key in engineersActions:
        engineers.append("{0}:{1}".format(key, engineersActions[key]))

    return (json.dumps({'Summary': items,"Total actions by Engineers":engineers, "Actions Performed":actionsList}))

def addItem(dic, item):
    if(item in dic):
        dic[item]+=1
    else:
        dic[item]=1