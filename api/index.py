from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'welcome to spotistats backend'

@app.route('/test')
def test():
    return 'health check'