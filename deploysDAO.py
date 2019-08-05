__author__ = "Dinesh Madavin"
__version__ = "1.0"
__email__ = "dmadavin@gmail.com"
__status__ = "Production"
__date__ = "August 5, 2019"


import deploys
from flask import Blueprint, request
import time

deploys_page = Blueprint('deploys_page', __name__, template_folder='templates')

@deploys_page.route('/')
def listApis():
    apis=[]

    apis.append("/getallengineers")
    apis.append("/eventsbyengineer/<name>")
    apis.append("/events?from=<epoch_date>&to=<epoch_date>")
    apis.append("/summary/<?date=<epoch_date>")
    return ({'name': 'Slack question - deployment api (wheres swagger??)','APIs':apis})


@deploys_page.route('/getallengineers')
def getAllEngineers():
    """
    Route for getting all engineers.
    Route: /getallengineers
    :return: Returns the list of unique engineers
    """
    return deploys.getEngineers()

@deploys_page.route('/eventsbyengineer/<string:name>')
def getEvents(name):
    return deploys.getEventsByEngineer(name)

@deploys_page.route('/events')
def getEventsByDuration():
    """
    Get the list of events by from and to date
    Query Params:
        from - the from date in epoch time
        to - to time in epoch
    :return: Return the list of events between the from and to date times.
    """
    if(request.args.get('from') is None or request.args.get('to') is None):
        return ('{"Error": "From and to date in epoch time is required"}'), 422
    else:
        fromDateTime = request.args.get('from')
        toDateTime = request.args.get('to')
        return deploys.getEventsByDateTime(fromDateTime,toDateTime)


@deploys_page.route('/summary')
def getSummary():
    """
    Summary of the events.
    Query Param:
        date - the date to get the summary from. In epoch time.
    :return: Return the summary of events for that day.
    """
    if(request.args.get('date') is None):
        dateTime = int(time.time())
    else:
        dateTime = request.args.get('date')
    return deploys.getSummary(dateTime)

