
from flask import Flask
from deploysDAO import simple_page
app = Flask(__name__)
app.register_blueprint(simple_page)
app.run(debug=True)