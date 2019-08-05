import deploys
from flask import Blueprint, request



simple_page = Blueprint('simple_page', __name__, template_folder='templates')
@simple_page.route('/getallengineers')
def getAllEngineers():
    print("getting engineers")
    return deploys.getEngineers()

@simple_page.route('/eventsbyengineer/<string:name>')
def getEvents(name):
    print("getting events for ",name)
    return deploys.getEventsByEngineer(name)

@simple_page.route('/events')
def getEventsByDuration():
    fromDateTime = request.args.get('from')
    toDateTime = request.args.get('to')
    print("getting events by duration "+fromDateTime+" to "+ toDateTime)
    return deploys.getEventsByDateTime(fromDateTime,toDateTime)




