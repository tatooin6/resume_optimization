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
)
