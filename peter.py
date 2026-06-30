from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")

prompt=[
    SystemMessage(content="You are a care center agent assistant")
]



res = model.invoke(prompt)

print(res.content)