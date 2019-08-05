import deploys
from flask import Blueprint, request
import time



simple_page = Blueprint('simple_page', __name__, template_folder='templates')
@simple_page.route('/getallengineers')
def getAllEngineers():
    print("getting engineers")
    return deploys.getEngineers()

@simple_page.route('/eventsbyengineer/<string:name>')
def getEvents(name):
    return deploys.getEventsByEngineer(name)

@simple_page.route('/events')
def getEventsByDuration():
    fromDateTime = request.args.get('from')
    toDateTime = request.args.get('to')
    return deploys.getEventsByDateTime(fromDateTime,toDateTime)


@simple_page.route('/summary')
def getSummary():
    if(request.args.get('date') is None):
        dateTime = int(time.time())
    else:
        dateTime = request.args.get('date')
    return deploys.getSummary(dateTime)

