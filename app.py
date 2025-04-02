from flask import Flask, request, render_template_string
import openai
import os

app = Flask(__name__)

# Pull your OpenAI API key from environment variables
openai.api_key = os.environ.get("OPENAI_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        query = request.form.get("query", "")
        if query:
            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful assistant for AI search strategy."},
                        {"role": "user", "content": query}
                    ],
                    max_tokens=200,
                    temperature=0.7
                )
                result = response.choices[0].message.content.strip()
            except Exception as e:
                result = f"Error from OpenAI: {e}"

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>AI Search Test</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f5f5f5;
                margin: 0;
                padding: 20px
