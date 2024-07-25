# Ollama Rag Web App

Use any Ollama compatible LLM to interact with your documents.

## Before Getting Started
Before getting started, make sure you have Python installed on your computer.
https://www.python.org/downloads/

(This project was created using Python 3.12.4)

You will also need to download the Ollama file from the official website: https://ollama.com/download

Once downloaded you can pick which Large Language Model's you want to use for this project.
Our Team recommends Llama 3-8b. Smaller language models will return less accurate results.

## Installation

1. Clone the repository

```
https://github.com/brukmula/OllamaRag
```

2. Navigate to the project directory

```
cd OllamaRag
```

3. Install the Dependencies

```commandline
pip install -r requirements.txt
```

## Creating a database
The first step to creating your database is to upload any of your documents to the 'data' folder of the project.

Once the documents are loaded into the folder run the following line on your command line.

```commandline
python create_database.py
```
This will create a Chroma database for your project to read from using the documents' information.

## Usage

Before running the app, make sure you have the Ollama server running on one of your terminals.

```commandline
ollama serve
```
Once you confirm that the server is running, run the Python Flask App.

```bash
python app.py
```

Once this is complete, the app will open the project at this address: http://127.0.0.1:5000

## Features

- All run locally
  - Ollama runs your LLMs on your own device, so no need to create any accounts.
- Multiple LLM Support
  - Since this program is run using Ollama, all Ollama supported LLMs are compatible with this program.
- Document Handling
  - PDF, txt, and MD files are all supported.

## Credit 

RAG Features: https://python.langchain.com/v0.2/docs/tutorials/rag/

This project uses code from [pixegami/rag-tutorial-v2] (https://github.com/pixegami/rag-tutorial-v2)
