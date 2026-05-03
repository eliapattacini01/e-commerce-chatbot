from src.embedder import model, collection

def retrieve_faq(user_question):
    user_embedding = model.encode(user_question).tolist()
    results = collection.query(
        query_embeddings=[user_embedding], 
        n_results=2 
    )
    return results

