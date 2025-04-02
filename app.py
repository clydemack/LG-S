from flask import Flask, request, render_template_string
import openai
import os

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")

html = """
<!DOCTYPE html>
<html>
<head>
    <title>AI Query</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            padding: 20px;
            background-color: #f9f9f9;
        }
        h2 {
            text-align: center;
        }
        form {
            text-align: center;
            margin-bottom: 20px;
        }
        input[type="text"] {
            width: 80%%;
            padding: 10px;
            font-size: 16px;
        }
        input[type="submit"] {
            margin-top: 10px;
            padding: 10px 20px;
            font-size: 16px;
            display: inline-block;
        }
        .response-box {
            background-color: #f1f2f2;
            padding: 20px;
            margin: auto;
            max-width: 90%%;
            word-wrap: break-word;
            white-space: pre-wrap;
        }
        @media (max-width: 600px) {
            input[type="text"] {
                width: 95%%;
            }
        }
    </style>
</head>
<body>
    <h2>Type a search query:</h2>
    <form method="POST">
        <input type="text" name="query" placeholder="e.g. best SEO company in Austin">
        <br>
        <input type="submit" value="Submit">
    </form>
    {% if response %}
    <div class="response-box">
        <strong>Response:</strong><br><br>{{ response }}
    </div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    response_text = ""
    if request.method == "POST":
        query = request.form["query"]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant for search optimization."},
                {"role": "user", "content": query}
            ]
        )
        response_text = completion.choices[0].message["content"]
    return render_template_string(html, response=response_text)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
