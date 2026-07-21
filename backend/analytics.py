from sqlalchemy.orm import Session
import models


def get_dashboard(db: Session):

    total_prompts = db.query(models.Prompt).count()

    total_versions = db.query(models.PromptVersion).count()

    latest_prompt = (
        db.query(models.Prompt)
        .order_by(models.Prompt.id.desc())
        .first()
    )

    if total_prompts > 0:
        average_versions = round(total_versions / total_prompts, 2)
    else:
        average_versions = 0

    return {
        "total_prompts": total_prompts,
        "total_versions": total_versions,
        "latest_prompt": latest_prompt.title if latest_prompt else None,
        "average_versions": average_versions,
        "available_models": [
            "llama-3.3-70b-versatile",
            "openai/gpt-oss-20b"
        ]
    }