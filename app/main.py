# -*- coding: utf-8 -*-

from fastapi import FastAPI
from app.tasks import process_resume
from app.models import OptimizationRequest
from app.celery_config import celery_app

app = FastAPI()


@app.get("/")
def read_root():
    return {"server": "working fine"}


@app.post("/optimization_request/")
def optimization_request(request: OptimizationRequest):
    """
    Test Optimization request shape.

    Parameters
    ----------
    request : OptimizationRequest
        Optimization request shape.

    Returns
    -------
    request : TYPE
        Optimization request shape..

    """
    return request


@app.post("/debug_task/")
def debug_task(request: OptimizationRequest):
    """
    Debugs process_resume task.

    Parameters
    ----------
    request : OptimizationRequest
        Optimization request interface.

    Returns
    -------
    dictionary
        Return message and pdf_path as return of the process task.

    """
    return process_resume(request.dict())


@app.post("/upload_resume/")
def upload_resume(resume_data: OptimizationRequest):
    """

    Parameters
    ----------
    resume_data : OptimizationRequest
        Receives resume and job description.

    Returns
    -------
    dict
        Return task_id and task status.

    """
    print(">>>>>>>> BEFORE CELERY TASK")
    task = process_resume.apply_async(
        kwargs={"request_data": resume_data.dict()},
        queue="resume_tasks"
    )
    print(">>>>>>>> AFTER CELERY TASK")
    return {
        "task_id": task.id,
        "status": "Processing"
    }


@app.get("/task_status/{task_id}")
def task_status(task_id: str):
    task_result = celery_app.AsyncResult(task_id)
    return {
        "task_id": task_id,
        "status": task_result.status,
        "result": task_result.result
    }
