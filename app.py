from flask import Flask
app= Flask(__name__)
@app.route('/')
def index():
  return "<h1>First heroku flask web app</h1>"