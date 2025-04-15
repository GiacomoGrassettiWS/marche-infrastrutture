from fastapi import FastAPI
import uvicorn
from dotenv import load_dotenv
from scraper import Scraper
app = FastAPI()

load_dotenv()

@app.get("/")
async def root():
    return {"status": "OK"}

@app.get("/upload_media_pubb")
async def upload_media_pubb():
    try:
        scraper = Scraper()
        completed = await scraper.entry_point()
        return {"completed": completed, "message": "Upload completato"}
    except Exception as e:
        return {"completed": False, "message": str(e)}

# Start the FastAPI server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
