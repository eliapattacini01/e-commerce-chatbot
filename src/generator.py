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
        prompt = "You are a FAQ chatbot with the task to give relevant answers to the customer, you should use the relevant FAQ and the distance provided to give the answer, ask at the end if the user has any other question"
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