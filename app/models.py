# -*- coding: utf-8 -*-

from pydantic import BaseModel


class OptimizationRequest(BaseModel):
    resume_md: str
    job_description: str
