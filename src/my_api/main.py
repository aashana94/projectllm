from fastapi import FastAPI, BackgroundTasks
import asyncio
import os
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
# import anthropic
# from groq import Groq
from dotenv import load_dotenv
from openai import OpenAI


load_dotenv()

app = FastAPI()
# app.mount("/static", StaticFiles(directory="src/my_api/static"), name="static")
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)
print("CLIENT CREATED:", client)

class Message(BaseModel):
    content: str

@app.get("/")
async def root():
    return FileResponse("src/my_api/static/index.html")

@app.post("/chat")
async def chat(message: Message):
    try:
        response = client.chat.completions.create(
            model="google/gemma-4-31b-it:free",
            messages=[{"role": "user", "content": message.content}]
        )
        print("GOT RESPONSE:", response)
        return {"response": response.choices[0].message.content}
    except Exception as e:
        print("ERROR TYPE:", type(e))
        print("ERROR:", e)
        if "429" in str(e):
            return {"response": "Model is busy, please try again in a moment."}
    return {"response": f"Error: {str(e)}"}
# async def slow_job(item_id: int):
#     await asyncio.sleep(2)
#     print(f"Done processing {item_id}")

# @app.post("/process/{item_id}")
# async def process(item_id: int, tasks: BackgroundTasks):
#     tasks.add_task(slow_job, item_id)
#     return {"status": "queued", "id": item_id}
