import deploys
from flask import Blueprint



simple_page = Blueprint('simple_page', __name__, template_folder='templates')
@simple_page.route('/getallengineers')
def getAllEngineers():
    print("getting engineers")
    return deploys.getEngineers()

@simple_page.route('/events/<string:name>')
def getEvents(name):
    print("getting events for ",name)
    return deploys.getEventsByEngineer(name)




