__author__ = "Dinesh Madavin"
__version__ = "1.0"
__email__ = "dmadavin@gmail.com"
__status__ = "Production"
__date__ = "August 5, 2019"

"""
A Simple API to connect to an SQL DB and return values.
"""
from flask import Flask
from deploysDAO import deploys_page
app = Flask(__name__)
app.register_blueprint(deploys_page)
if __name__ == '__main__':
    app.run(debug=True)