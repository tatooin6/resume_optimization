#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:45:13 2025

@author: apantoja03130
"""

import openai
import markdown
from weasyprint import HTML
import os

# openai.api_key = ""

client = openai.OpenAI(
    api_key="XXX")


def load_markdown_resume(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()


def generate_custom_resume(resume_md, job_description):
    prompt = f"""
    {resume_md}
    {job_description}
    """

    # (messages, model)
    chat_completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.7
    )

    return chat_completion["choices"][0]["message"]["content"]


def save_to_markdown(content, filename="optimized_resume.md"):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)


def convert_markdown_to_html(md_content):
    return markdown.markdown(md_content)


def convert_html_to_pdf(html_content, output_file="optimized_resume.pdf"):
    pdf_path = os.path.join(os.getcwd(), output_file)  # Ruta completa al PDF
    HTML(string=html_content).write_pdf(pdf_path)
    return pdf_path


if __name__ == "__main__":
    resume_md = load_markdown_resume("resume.md")

    job_description = input("Introduce la descripción del puesto: ")

    new_resume_md = generate_custom_resume(resume_md, job_description)

    save_to_markdown(new_resume_md)

    resume_html = convert_markdown_to_html(new_resume_md)

    convert_html_to_pdf(resume_html)

    print("Currículum optimizado generado como optimized_resume.pdf")
