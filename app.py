from flask import Flask, request, render_template
from langchain_community.vectorstores import Chroma
from langchain.prompts import ChatPromptTemplate
from langchain_community.llms.ollama import Ollama
from get_embedding_function import get_embedding_function

app = Flask(__name__)

CHROMA_PATH = "chroma"
PROMPT_TEMPLATE = """
{question}
Answer the question based only on the following context, don't answer if it outside of this context.:

{context}
---
Answer the question based on the above context, do not use the word context, say 'According to my resources' instead'
If the question doesn't fit the context, don't give an answer

"""


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/query', methods=['POST'])
def query():
    query_text = request.form['query']
    model_name = request.form['model']
    response_text, sources, prompt_text = query_rag(query_text, model_name)
    return render_template('result.html', response=response_text, query=query_text, sources=sources,
                           model_name=model_name, prompt_text=prompt_text)


def query_rag(query_text: str, model_name: str):
    embedding_function = get_embedding_function()
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    results = db.similarity_search_with_score(query_text, k=5)

    context_text = "\n\n--\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    prompt = prompt_template.format(context=context_text, question=query_text)

    model = Ollama(model=model_name)
    response_text = model.invoke(prompt)

    # Collect sources
    sources = [doc.metadata.get("id", "Unknown source") for doc, _score in results]

    return response_text, sources, prompt


if __name__ == "__main__":
    app.run(debug=True)
