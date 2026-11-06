import os
import requests
from fastapi import FastAPI, Depends, HTTPException, Header
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from dotenv import load_dotenv
import ollama

load_dotenv()

API_KEY_CREDITS = {os.getenv("API_KEY"): 50}
print(API_KEY_CREDITS)
app = FastAPI()

def verify_api_key(x_api_key: str = Header(None)):
    credits = API_KEY_CREDITS.get(x_api_key, 0)
    
    if credits <= 0 or x_api_key != os.getenv('API_KEY'):
        raise HTTPException(status_code=401, detail="Invalid API Key, or no credits")

    return x_api_key

@app.post("/generate")
def generate(prompt: str, x_api_key: str = Depends(verify_api_key)):
    API_KEY_CREDITS[x_api_key] -= 1
    response = ollama.chat(model="mistral:7b", messages=[{"role": "user", "content": prompt}])
    print('Credits available: ', API_KEY_CREDITS)
    return {"response": response["message"]["content"]}