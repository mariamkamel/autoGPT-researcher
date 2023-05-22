# from fastapi import FastAPI

# app = FastAPI()

import openai
import os

openai.api_key = os.environ.get("OPENAIAPI")  # Replace with your OpenAI API key

from flask import Flask

app = Flask(__name__)


@app.route("/<product_name>")
def hello(product_name):
    prompt = f"Research about {product_name}"
    print(prompt)
    response = openai.Completion.create(
        engine="text-davinci-003",  # Choose the appropriate engine for your needs
        prompt=prompt,
        max_tokens=500,  # Set the desired length of the research
        n=1,
        stop=None,
        temperature=0.8,  # Adjust the temperature for more or less randomness
    )
    print(response)
    research = response.choices[0].text.strip()

    return {"data": research}, 200
