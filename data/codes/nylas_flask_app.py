#!/usr/bin/env python
from flask import Flaskapp = Flask(__name__)
@app.route('/')def hello_world(): return 'Hello World!'
if __name__ == '__main__':    app.run()