import logging
import sys

from flask import Flask, request
from language_models import process_query

app = Flask(__name__)
app.logger.setLevel(logging.INFO)


@app.post("/")
def server():
    query = request.form.get("query")
    app.logger.info("Received request with message: %s", query)
    result = process_query(query)
    app.logger.info("Processed response: %s", result)
    return result
