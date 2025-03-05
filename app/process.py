#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 11:55:47 2025

@author: apantoja03130
"""

import google.generativeai as genai
import markdown
import os
from weasyprint import HTML
from dotenv import load_dotenv

load_dotenv()
genai_api_key = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=genai_api_key)

model = genai.GenerativeModel("gemini-2.0-flash")


def load_file(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_custom_resume(resume_md, job_description):
    """ Resume optimization based on Job Description """

    prompt = f"""
    You are an expert on recruitment and curriculum optimization

    Take the next curriculum in Markdown format and make adjustments so it fits
    with the job description proportioned.

    - Highlight skills and experiences relevant to the position.
    - Adjust the tone and approach based on the industry and role.
    - Keep the original structure, but modify the content intelligently.

    ## Curriculum
    {resume_md}

    ## Job Description
    {job_description}

    Return only the optimized curriculum in Markdown format, without comments nor explanations
    """

    response = model.generate_content(
        prompt,
        generation_config=genai.types.GenerationConfig(
            max_output_tokens=380,
            temperature=0.5
        )
    )
    return response.text


def save_to_markdown(content, filename="data/outputs/optimized_resume.md"):
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def convert_markdown_to_html(md_content):
    return markdown.markdown(md_content)


def convert_html_to_pdf(html_content, output_file="data/outputs/optimized_resume.pdf"):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    pdf_path = os.path.abspath(output_file)
    print(f">>>>>>>>  Generating PDF in: {pdf_path}")
    HTML(string=html_content).write_pdf(pdf_path)
    return pdf_path


if __name__ == "__main__":
    resume_md = load_file("../data/inputs/resume.md")

    job_description = load_file("../data/inputs/job_description.txt")

    new_resume_md = generate_custom_resume(resume_md, job_description)

    save_to_markdown(new_resume_md)

    resume_html = convert_markdown_to_html(new_resume_md)

    pdf_path = convert_html_to_pdf(resume_html)

    print(f"PDF created in {pdf_path}")
