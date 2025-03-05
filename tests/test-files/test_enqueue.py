#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  3 22:48:16 2025

@author: apantoja03130
"""

from app.tasks import process_resume
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


print(sys.path)

task = process_resume.apply_async(
    kwargs={"request_data": {"resume_md": "Test CV", "job_description": "Test job"}})

print(f"Queued task with ID: {task.id}")
