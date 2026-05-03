import vertexai
from vertexai.generative_models import GenerativeModel
vertexai.init(
project = "chatbot-ecom-494513",
location = "us-central1"
)
model = GenerativeModel("gemini-2.5-flash")


def generate_answer(question,relFAQ,distances):
    
    if min(distances)>1.5:
        prompt = "You are a FAQ chatbot with the task to give relevant answers to the customer, you must tell the customer there are no relevant information about his answer in your FAQ"
    else:
        prompt = "You are a helpful and polite customer support agent. Your task is to provide accurate, concise answers based *only* on the provided context below. RULES Keep answers concise (3-7 sentences) and user-friendly. "
    relFAQ_text = "\n".join(relFAQ)
    context = f"""
    {prompt}

    Context:
    {relFAQ_text}

    Customer question: {question}

    Answer:
    """
    answer = model.generate_content(contents=context)
    return answer.text