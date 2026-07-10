from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from orchestrator import run_analysis

app = FastAPI(title="FounderOS AI")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class StartupIdea(BaseModel):
    idea: str

@app.get("/")
def home():
    return {"status": "running"}

@app.post("/analyze")
async def analyze(data: StartupIdea):
    result = await run_analysis(data.idea)
    return result