import os
from flask import Flask

app = Flask(__name__)
 
@app.route('/')
def hello_world():
    return 'Hello World!'
 
@app.route('/another_thing')
def hello_world2():
    return 'Hello World!'*500
 
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=int(os.environ["PORT"])) 
