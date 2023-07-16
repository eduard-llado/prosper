import logging
from functools import cache

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from preprocess import build_index

logger = logging.getLogger("app")


@cache
def load_index():
    logger.info("Building index")
    index = build_index()
    return index


def process_query(query):
    index = load_index()
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
    qa_chain = RetrievalQA.from_chain_type(
        llm, retriever=index.as_retriever(), return_source_documents=True
    )
    response = qa_chain({"query": query})
    answer = response["result"]
    relevant_documents = response["source_documents"]
    logger.debug("Retrieved %s relevant documents", len(relevant_documents))
    logger.debug(relevant_documents)
    return answer
