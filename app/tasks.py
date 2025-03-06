# -*- coding: utf-8 -*-

from app.celery_config import celery_app
from app.process import (
    generate_custom_resume,
    save_to_markdown,
    convert_markdown_to_html,
    convert_html_to_pdf
)
from app.models import OptimizationRequest
import logging
import os


@celery_app.task
def process_resume(request_data: dict):
    """
    Processing resume optimization on background.
    """
    logging.info(">>>>>> Celery has received the task.")
    print(">>>>>> Celery has received the task.")

    request = OptimizationRequest(**request_data)

    new_resume_md = generate_custom_resume(request.resume_md, request.job_description)

    save_to_markdown(new_resume_md)

    resume_html = convert_markdown_to_html(new_resume_md)

    print(f">>>>>> Celery is running on: {os.getcwd()}")

    pdf_path = convert_html_to_pdf(resume_html)

    logging.info(f">>>>>> PDF file generated in: {pdf_path}")
    print(f">>>>>> PDF file generated in: {pdf_path}")

    return {
        "message": "CV processed correctly.",
        "pdf_path": pdf_path
    }
