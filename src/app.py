from flask import Flask
import json
import os

app = Flask(__name__)
with open('/Users/srangise/git/python-flask/config/config-e1.json') as config_file:
    config_data = json.load(config_file)
print(config_data["env"])


@app.route('/status')
def hello():
    print(config_data["env"])
    return "<h1>Application running successfully</h1>"

@app.route('/<name>')
def hello_name(name):
    print(config_data["env"])
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()