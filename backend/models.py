from sqlalchemy import Column, Integer, String, Text, DateTime
from database import Base
from datetime import datetime


class Prompt(Base):
    __tablename__ = "prompts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200))
    role = Column(Text)
    context = Column(Text)
    task = Column(Text)
    rules = Column(Text)
    output_format = Column(Text)
    content = Column(Text)


class PromptVersion(Base):
    __tablename__ = "prompt_versions"

    id = Column(Integer, primary_key=True, index=True)

    prompt_id = Column(Integer)

    version = Column(Integer)

    title = Column(String(200))

    role = Column(Text)

    context = Column(Text)

    task = Column(Text)

    rules = Column(Text)

    output_format = Column(Text)

    content = Column(Text)

    created_at = Column(DateTime, default=datetime.utcnow)