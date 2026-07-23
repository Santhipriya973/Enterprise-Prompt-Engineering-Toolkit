from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
from database import engine, get_db
from prompt_engine import build_prompt
from schemas import PromptRequest
from evaluator import evaluate_prompt
from schemas import EvaluateRequest
from optimizer import optimize_prompt

from compare_models import compare_models
from schemas import CompareRequest

from analytics import get_dashboard

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def home():
    return {"message": "Enterprise Prompt Toolkit"}


@app.post("/build_prompt")
def create_prompt(
    data: PromptRequest,
    db: Session = Depends(get_db)
):

    final_prompt = build_prompt(
        data.role,
        data.context,
        data.task,
        data.rules,
        data.output_format
    )

    new_prompt = models.Prompt(
    title=data.title,
    role=data.role,
    context=data.context,
    task=data.task,
    rules=data.rules,
    output_format=data.output_format,
    content=final_prompt
)
    

    db.add(new_prompt)
    db.commit()
    db.refresh(new_prompt)
# Save Version 1

    version = models.PromptVersion(
        prompt_id=new_prompt.id,
        version=1,
        title=new_prompt.title,
         role=new_prompt.role,
          context=new_prompt.context,
          task=new_prompt.task,
           rules=new_prompt.rules,
          output_format=new_prompt.output_format,
         content=new_prompt.content
)
    db.add(version)
    db.commit()

    return {
        "message": "Prompt saved successfully!",
        "id": new_prompt.id,
        "prompt": final_prompt
    }

@app.get("/prompts")
def get_prompts(db: Session = Depends(get_db)):
    prompts = db.query(models.Prompt).all()
    return prompts

@app.get("/prompts/{prompt_id}")
def get_prompt(prompt_id: int, db: Session = Depends(get_db)):

    prompt = db.query(models.Prompt).filter(
        models.Prompt.id == prompt_id
    ).first()

    if not prompt:
        return {"message": "Prompt not found"}

    return prompt

@app.put("/prompts/{prompt_id}")
def update_prompt(
    prompt_id: int,
    data: PromptRequest,
    db: Session = Depends(get_db)
):

    prompt = db.query(models.Prompt).filter(
        models.Prompt.id == prompt_id
    ).first()

    if not prompt:
        return {"message": "Prompt not found"}

    # Find latest version number
    latest_version = db.query(models.PromptVersion).filter(
        models.PromptVersion.prompt_id == prompt_id
    ).count()

    # Save current prompt as a version
    version = models.PromptVersion(
        prompt_id=prompt.id,
        version=latest_version + 1,
        title=prompt.title,
        role=prompt.role,
        context=prompt.context,
        task=prompt.task,
        rules=prompt.rules,
        output_format=prompt.output_format,
        content=prompt.content
    )

    db.add(version)

    # Update prompt
    prompt.title = data.title
    prompt.role = data.role
    prompt.context = data.context
    prompt.task = data.task
    prompt.rules = data.rules
    prompt.output_format = data.output_format

    prompt.content = build_prompt(
        data.role,
        data.context,
        data.task,
        data.rules,
        data.output_format
    )

    db.commit()

    return {
        "message": "Prompt Updated Successfully",
        "version_saved": latest_version + 1,
        "prompt": prompt
    }

@app.delete("/prompts/{prompt_id}")
def delete_prompt(
    prompt_id: int,
    db: Session = Depends(get_db)
):

    prompt = db.query(models.Prompt).filter(
        models.Prompt.id == prompt_id
    ).first()

    if not prompt:
        return {"message": "Prompt not found"}

    db.delete(prompt)
    db.commit()

    return {
        "message": "Prompt Deleted Successfully"
    }

@app.post("/evaluate")
def evaluate(data: EvaluateRequest):

    result = evaluate_prompt(data.prompt)

    return {
        "evaluation": result
    }

@app.post("/optimize")
def optimize(data: EvaluateRequest):

    result = optimize_prompt(data.prompt)

    return result

@app.post("/compare_models")
def compare(data: CompareRequest):

    result = compare_models(data.prompt)

    return result

@app.get("/prompts/{prompt_id}/versions")
def get_versions(
    prompt_id: int,
    db: Session = Depends(get_db)
):

    versions = db.query(models.PromptVersion).filter(
        models.PromptVersion.prompt_id == prompt_id
    ).all()

    if not versions:
        return {
            "message": "No versions found"
        }

    return {
        "prompt_id": prompt_id,
        "total_versions": len(versions),
        "versions": versions
    }

@app.post("/prompts/{prompt_id}/restore/{version_number}")
def restore_version(
    prompt_id: int,
    version_number: int,
    db: Session = Depends(get_db)
):

    prompt = db.query(models.Prompt).filter(
        models.Prompt.id == prompt_id
    ).first()

    if not prompt:
        return {"message": "Prompt not found"}

    version = db.query(models.PromptVersion).filter(
        models.PromptVersion.prompt_id == prompt_id,
        models.PromptVersion.version == version_number
    ).first()

    if not version:
        return {"message": "Version not found"}

    prompt.title = version.title
    prompt.role = version.role
    prompt.context = version.context
    prompt.task = version.task
    prompt.rules = version.rules
    prompt.output_format = version.output_format
    prompt.content = version.content

    db.commit()

    return {
    "message": "Prompt restored successfully",
    "restored_version": version_number,
    "prompt": {
        "id": prompt.id,
        "title": prompt.title,
        "role": prompt.role,
        "context": prompt.context,
        "task": prompt.task,
        "rules": prompt.rules,
        "output_format": prompt.output_format,
        "content": prompt.content
    }
}

@app.get("/analytics")
def analytics(
    db: Session = Depends(get_db)
):
    return get_dashboard(db)
