#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 22:48:32 2025

@author: apantoja03130
"""

import google.generativeai as genai

genai.configure(api_key="XXX")

model = genai.GenerativeModel("gemini-2.0-flash")

prompt = "Say hi to this test file please."
response = model.generate_content(prompt)

print("Response:")
print(response.text)