#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 21:19:01 2025

@author: apantoja03130
"""

# DeepSeek

from openai import OpenAI
key = "XXX"
client = OpenAI(api_key=key, base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": "Say hello to this message."},
    ],
    stream=False
)

print(response.choices[0].message.content)