import os
import langchain
import langsmith
import getpass
import os
from langchain_google_genai import ChatGoogleGenerativeAI

if "GOOGLE_API_KEY" not in os.environ:
    os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter your Google AI API key: ")


llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

messages = [
    (
    "system",
    "You are a helpful assistant who responds with a friendly undertone",
    ),
    ("human", 
     "Lets build an AI agent using Langsmtih!"),
]
ai_msg = llm.invoke(messages)
print(ai_msg.content)