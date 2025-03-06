# -*- coding: utf-8 -*-

from celery import Celery

REDIS_URL = "redis://localhost:6379/0"

celery_app = Celery(
    "resume_optimizer",  # app name
    broker=REDIS_URL,
    backend=REDIS_URL,
    include=["app.tasks"]
)


celery_app.conf.update(
    task_routes={"app.tasks.*": {"queue": "resume_tasks"}},
    tasks_serializer="json",
    result_serializer="json",
    accept_content=["json"],
    result_backend=REDIS_URL,
    task_track_started=True,
    task_always_eager=False,
)
