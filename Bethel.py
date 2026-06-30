from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import  AIMessage, HumanMessage, SystemMessage


load_dotenv()
model = ChatGoogleGenerativeAI(model="gemini-2.5-flash",)


chats = [
SystemMessage(content="You are a helpful assistant."),
]

while True:
    user = input("You: ")
    humanMessage = HumanMessage(content=user)
    chats.append(humanMessage)


    if user == "exit":
        break
    
    res = model.invoke(chats)
    chats.append(AIMessage(content=res.content))
    print("result: ", res.content)



print("GoodBye! ")
# print(model)