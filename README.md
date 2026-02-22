# Local LLM Agent

![Status](https://img.shields.io/badge/status-in%20development-yellow?style=flat)

## Overview

This project is designed to develop some basic structures to run local LLMs. Once the basics are functioning it will provide a test bed for experimenting with LLMs and how to optimize thier parameters.

## To do list

- Use transformers to get a llm running locally from huggingface
- Use Ollama to get a local llm running
- Deploy a basic smolagent for a web search
- Insert an excessive amount of comments to understand the code
- Expand the code to show common parameters for function and performance
- Develop a RAG pipeline (should this be a separate project?)

## Technologies Used (expect updates here)

Basic Project Info\
![Python](https://img.shields.io/badge/python-3.10-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)


Framework & Libraries\
![LangChain](https://img.shields.io/badge/LangChain-0.1.0+-green.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28.0+-red.svg)
![ChromaDB](https://img.shields.io/badge/ChromaDB-0.4.0+-yellow.svg)

AI/ML Specific\
![Ollama](https://img.shields.io/badge/Ollama-Local%20LLM-blue)
![RAG](https://img.shields.io/badge/RAG-Enabled-purple)
![HuggingFace](https://img.shields.io/badge/🤗-Hugging%20Face-orange)

Tech Stack\
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup4-4.12.0+-lightgrey.svg)
![Pandas](https://img.shields.io/badge/Pandas-2.0.0+-blue.svg)
![NumPy](https://img.shields.io/badge/NumPy-1.24.0+-blue.svg)

Models Used\
![llama3.2](https://img.shields.io/badge/model-llama3.2:3b-blue)
![Qwen3](https://img.shields.io/badge/model-Qwen3--4B--BiasExpert-green)
![Embeddings](https://img.shields.io/badge/embeddings-mxbai--embed--large-purple)

Development Tools\
![Draw.io](https://img.shields.io/badge/diagrams-Draw.io-orange)
![LangSmith](https://img.shields.io/badge/monitoring-LangSmith-blue)

> pip install -r requirements.txt

## Ollama models used here

- llama3.2:3b (primary llm)
- mxbai-embed-large (embeddings model)
- nomic-embed-text:v1.5 (alternate embedder)

- RAG Evaluation Framework / Metrics / Techniques
- - qllama/bge-reranker-v2-m3:latest (prompt reranker)
- [Qwen3-4b-BiasExpert](https://huggingface.co/EmergentMethods/Qwen3-4B-BiasExpert) (bias analysis(huggingface))

## References

- https://www.youtube.com/watch?v=c5jHhMXmXyo - local RAG Chatbot
- https://www.youtube.com/watch?v=gcqp3Fbv4_o - RAG Pipeline
- https://www.e2enetworks.com/blog/guide-to-building-a-rag-based-llm-application RAG Guide from 2023
- https://medium.com/@krtarunsingh/an-in-depth-exploration-of-rag-retrieval-augmented-generation-611a0ddaba81 June 2024
- https://www.youtube.com/watch?v=uFhDXUOrgO0
- https://www.youtube.com/watch?v=vf9emNxXWdA & https://www.youtube.com/watch?v=g8OViy0xOoI RAG Walkthrough for 2025
- https://www.youtube.com/watch?v=sVcwVQRHIc8 LangChain walkthrough
- https://www.youtube.com/watch?v=wVdiT78-wS8 Video on chunking data

## Author

Jeff Oliver