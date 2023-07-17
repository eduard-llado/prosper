from langchain.evaluation.qa import QAEvalChain
from langchain.llms import OpenAI


def evaluate(queries, predictions):
    llm = OpenAI(temperature=0)
    eval_chain = QAEvalChain.from_llm(llm)
    response = eval_chain.evaluate(
        queries, predictions, question_key="question", prediction_key="text"
    )
    results = [r["results"] for r in response]
    return results
