from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from ai_coder.crew import AiCoder
import uvicorn

app = FastAPI(title="AI Coder API", version="1.0.0")

class CodeRequest(BaseModel):
    topic: str
    requirements: str

class CodeResponse(BaseModel):
    success: bool
    result: str
    error: str | None = None

@app.get("/")
async def root():
    """Health check endpoint"""
    return {"status": "ok", "message": "AI Coder API is running"}

@app.post("/generate-code", response_model=CodeResponse)
async def generate_code(request: CodeRequest):
    """
    Generate code based on topic and requirements.
    
    The planner agent will create an implementation plan,
    and the coder agent will generate the code.
    """
    try:
        inputs = {
            'topic': request.topic,
            'requirements': request.requirements
        }
        
        # Run the crew
        result = AiCoder().crew().kickoff(inputs=inputs)
        
        return CodeResponse(
            success=True,
            result=str(result),
            error=None
        )
    except Exception as e:
        return CodeResponse(
            success=False,
            result="",
            error=str(e)
        )

def start_server(host: str = "0.0.0.0", port: int = 8000):
    """Start the FastAPI server"""
    uvicorn.run(app, host=host, port=port)

if __name__ == "__main__":
    start_server()
