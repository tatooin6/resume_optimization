# -*- coding: utf-8 -*-

from app.celery_config import celery_app
import time


@celery_app.task
def process_resume(resume_data: dict):
    """
    Processing simulation on background.
    """

    time.sleep(5)
    return {"message": "CV processed correctly"}
