from src.embedder import model, collection

def add_faq(question, answer):
    string_toEncode = question + " " + answer
    embedding = model.encode(string_toEncode).tolist()
    indexes_num = collection.count()
    collection.add(
        ids=[str(indexes_num)],
        documents=[string_toEncode],
        embeddings=[embedding])

def reset_collection():
    all_ids = collection.get()["ids"]
    if len(all_ids) > 0:
        collection.delete(ids=all_ids)

def get_all():
    return collection.get()["documents"]