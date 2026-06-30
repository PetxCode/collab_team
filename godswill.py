from dotenv import load
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


chats=[
    SystemMessage(content="You are a global sports opportunities assistant, your role is to provide information on global sports opportunities that are available for athletes in different nations of the world. loads of talented youths especially in Africa struggle to have access to global sports trials; scholarships; intenships; fellowships; and conferences, etc, hence you will share information to every user by researching sports websites around the globe and feeding that information to the users following their specific requests. Please always focust your results specifically to the question or input request of the user")
]

while True:
    user =input("User: ")
    humanMessage = HumanMessage(content=user)
    chats.append(humanMessage)

    if user =="exit":
        break
    res = model.invoke(chats)
    chats.append(AIMessage(content=res.content))
    print("result: ", res.content)

print("Daalu!")   