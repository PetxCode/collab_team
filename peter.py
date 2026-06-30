from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

from flask import Flask, render_template, request, jsonify


app = Flask(__name__)

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")


@app.route("/")
def indexHome():
    return render_template("index.html")

@app.route("/", methods=["POST"])
def index():
    
    chats=[
        SystemMessage(content="You are a care center agent assistant")
    ]
    history = []
    
    while True:
        user = input("You😍: ")
        humanMessage = HumanMessage(content=user)
        chats.append(humanMessage)
        history.append({"user":user})
        if user == "exit":
            break
        res = model.invoke(chats)
        chats.append(AIMessage(content=res.content))
        history.append({"result": res.content})
        return jsonify({"data": history})



 
chats=[
    SystemMessage(content="You are a care center agent assistant")
]
history = []

while True:
    user = input("You😍: ")
    humanMessage = HumanMessage(content=user)
    chats.append(humanMessage)

    history.append({"user":user})
    if user == "exit":
        break
    res = model.invoke(chats)
    chats.append(AIMessage(content=res.content))
    history.append({"result": res.content})
    print("result: ", res.content)

# for i in chats:
#     i[]
   
print(history)


if __name__ == "__main__":
    app.run(debug=True)