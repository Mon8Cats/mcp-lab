from flask import Flask, request, jsonify
from langchain_core.prompts import ChatPromptTemplate
#from langchain_community.chat_models import ChatOllama
from langchain_ollama import ChatOllama


app = Flask(__name__)

# LangChain + Ollama setup
llm = ChatOllama(model="mistral")

# Define a LangChain prompt template
prompt_template = ChatPromptTemplate.from_template("User: {user_input}\nAssistant:")

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.json
        user_input = data.get("message", "")

        if not user_input:
            return jsonify({"error": "Message is required"}), 400

        chain = prompt_template | llm
        response = chain.invoke({"user_input": user_input})

        return jsonify({"response": response.content})

    except Exception as e:
        print("🔥 Server Error:", e)
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
