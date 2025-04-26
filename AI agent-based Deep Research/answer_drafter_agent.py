import os
import json
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
from config import DATA_STORAGE_PATH, LANGCHAIN_MODEL_NAME, OPENAI_API_KEY

try:
    from langchain.llms import OpenAI
    from langchain.chains.question_answering import load_qa_chain
    from langchain.docstore.document import Document
except ImportError:
    print("Please install langchain package: pip install langchain")

def run_answer_drafter_agent():
    """
    Entry point for the Answer Drafter Agent.
    Loads collected data and generates answers using LangChain.
    """
    data_file = os.path.join(DATA_STORAGE_PATH, 'collected_data.json')
    if not os.path.exists(data_file):
        print(f"Data file {data_file} not found. Please run the Research Agent first.")
        return

    with open(data_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    # Prepare documents for LangChain
    documents = [Document(page_content=item['content'], metadata={"source": item['url']}) for item in data]

    # Initialize OpenAI LLM
    if not OPENAI_API_KEY:
        print("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        return

    llm = OpenAI(model_name=LANGCHAIN_MODEL_NAME, openai_api_key=OPENAI_API_KEY)

    # Load QA chain
    chain = load_qa_chain(llm, chain_type="stuff")

    # Example query
    query = "What is the main content of the collected data?"

    print(f"Generating answer using model {LANGCHAIN_MODEL_NAME} for query: {query}")
    answer = chain.run(input_documents=documents, question=query)

    print("Generated Answer:")
    print(answer)

if __name__ == "__main__":
    run_answer_drafter_agent()
