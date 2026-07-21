from pydantic import BaseModel

class PromptRequest(BaseModel):
    title: str
    role: str
    context: str
    task: str
    rules: str
    output_format: str


class PromptResponse(BaseModel):
    id: int
    title: str
    prompt: str

class EvaluateRequest(BaseModel):
    prompt: str
    
class CompareRequest(BaseModel):
    prompt: str