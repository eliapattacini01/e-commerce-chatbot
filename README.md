# E-Commerce FAQ Chatbot
A dynamic FAQ chatbot for e-commerce platforms built with RAG (Retrieval-Augmented Generation), Vertex AI, and Gemini. Users can build a custom knowledge base through a simple UI and instantly query it through an AI-powered chatbot.

**FAQ Builder** — add custom question/answer pairs through the UI
**Embedding** — each FAQ is converted into a semantic vector using SentenceTransformers and stored in ChromaDB
**Retrieval** — when a user asks a question, the system finds the most semantically similar FAQs using cosine similarity
**Generation** — the relevant FAQs are passed as context to Gemini (via Vertex AI), which generates a natural language answer
