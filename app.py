import logging
import sys

from flask import Flask
from flask import request

from language_models import process_query

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

@app.post("/")
def server():
   query = request.form.get("query")
   app.logger.info("Received request with message: %s", query)
   result = process_query(query)
   app.logger.info("Processed response: %s", result)
   return result
