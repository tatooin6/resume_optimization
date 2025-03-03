# -*- coding: utf-8 -*-

from fastapi import FastAPI
from app.tasks import process_resume

app = FastAPI()


@app.get("/")
def read_root():
    return {"server": "working fine"}


@app.post("/upload_resume/")
def upload_resume(resume_data: dict):
    task = process_resume.apply_async(args=[resume_data])
    return {"task_id": task.id, "status": "Processing"}
