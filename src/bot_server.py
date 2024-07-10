# main.py

from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class AskBot(BaseModel):
    question: str
    chat_history: list[list[str]]


def generate_answer(user_data):
    ans_res = {
        "answer": "you asked now: " + 
        user_data.question + 
        " but your last question was: " +
        user_data.chat_history[-1][0]
    }
    return ans_res

@app.post("/ask_simple_bot")
async def ask_simple_bot(user_data: AskBot):
    res = generate_answer(user_data)
    return res


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)