__author__ = "Dinesh Madavin"
__version__ = "1.0"
__email__ = "dmadavin@gmail.com"
__status__ = "Production"
__date__ = "August 5, 2019"

from deployments.database import Database
import json
from datetime import datetime,timedelta
from flask import jsonify

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
    """
    Get all the distinct engineers
    :return: List of unique engineer names
    """
    dbObj=Singleton.getInstance()
    rows=dbObj.get('deploys','engineer')
    return jsonify(events=rows)

def getEventsByEngineer(name):
    """
    DB function to retrieve the list of events by an engineer
    :param name: Name of the engineer to query
    :return: The list of events performed by the engineer along with the id, sha and date.
    """
    dbObj = Singleton.getInstance()
    sql = "select id, sha, date, action from deploys where engineer='"+name+"'"
    rows = dbObj.query(sql)
    return jsonify(events=rows)

def getEventsByDateTime(fromDateTime,toDateTime):
    """
    Function to get the list of events by date
    :param fromDateTime: The from date in epoch
    :param toDateTime: The to date in epoch
    :return: List of events from the from and to date
    """
    dbObj = Singleton.getInstance()
    sql = "select id, sha, action, engineer from deploys where date BETWEEN '" + fromDateTime + "' and '" + toDateTime + "'"
    rows = dbObj.query(sql)
    return jsonify(events=rows)


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
    """
    Adding the item to dict for summary. This will be used to format the output for summary
    :param dic: the dictionary to add/update
    :param item: the key in question.
    """
    if(item in dic):
        dic[item]+=1
    else:
        dic[item]=1