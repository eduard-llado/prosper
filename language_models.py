import logging

from langchain.llms import OpenAI

llm = OpenAI(temperature=0.9)

logger = logging.getLogger("app")

def process_query(query):
   return llm.predict(query)
