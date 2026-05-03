from src.retriever import retrieve_faq
from src.generator import generate_answer
from src.embedder import collection

history = []
while True:
    user_question = input("You: ")
    result = retrieve_faq(user_question)
    history.append(f"User: {user_question}")
    answer = generate_answer(history, result["documents"][0], result["distances"][0])
    print(f"Chat: {answer}")
    history.append(f"Chat: {answer}")