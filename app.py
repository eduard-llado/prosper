from flask import Flask
from flask import request

app = Flask(__name__)

@app.post("/")
def hello_world():
   return request.get_data()
