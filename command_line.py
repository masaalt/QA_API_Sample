from api import send_qa_simple_bot

if __name__ == "__main__":
    print("chat AI system started!")
    chat_history=[["init", "ed"]]
    while True:
        print("please ask your question:")
        question = input()
        result = send_qa_simple_bot({"question": question, "chat_history": chat_history})
        chat_history.append([question, result["answer"]])
        print("AI said: " + result["answer"])
        