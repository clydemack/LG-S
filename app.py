from flask import Flask, request, render_template_string
import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

HTML_TEMPLATE = '''
<!DOCTYPE html>
<html>
<head>
  <title>GPT Brand Checker</title>
</head>
<body>
  <h2>Type a search query:</h2>
  <form method="post">
    <input name="query" style="width:100%;padding:10px;" />
    <button type="submit" style="padding:10px;margin-top:10px;">Submit</button>
  </form>
  {% if response %}
    <h3>Response:</h3>
    <pre style="background:#f4f4f4;padding:10px;">{{ response }}</pre>
  {% endif %}
</body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        user_input = request.form["query"]
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}],
            max_tokens=300
        )
        response = completion.choices[0].message.content
    return render_template_string(HTML_TEMPLATE, response=response)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
