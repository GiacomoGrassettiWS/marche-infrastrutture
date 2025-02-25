from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
import requests
import os
 
app = FastAPI()
load_dotenv()

@app.get("/")
async def root():
    return {"status": "OK"}

@app.get("/interventi")
async def get_interventi():
    url = os.getenv("WMSCARTOGRAFIA_URL")
    if url:
        response =  requests.get(url)
        if response.status_code == 200:
            return response.json()["features"]
        else:
            return {"message": "Errore nella richiesta"}
    else:
        return {"message": "URL non configurato"}
    
    # Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, env_file=".env", reload=True)
