from flask import Flask, request, render_template_string
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    response = ""
    if request.method == "POST":
        query = request.form.get("query")
        response = f"You searched for: {query}"

    return render_template_string("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>AI Search Demo</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #ccc;
                margin: 40px;
            }
            .container {
                max-width: 800px;
                margin: auto;
                background-color: #d3cdca;
                padding: 20px;
                box-shadow: 0px 0px 8px #888;
                border-radius: 6px;
            }
            h2 {
                text-align: center;
            }
            form {
                text-align: center;
            }
            input[type="text"] {
                width: 90%;
                padding: 12px;
                font-size: 16px;
                margin-bottom: 12px;
            }
            input[type="submit"] {
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
            }
            .response {
                margin-top: 20px;
                font-size: 18px;
                text-align: center;
                font-weight: bold;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h2>Type a search query:</h2>
            <form method="POST">
                <input type="text" name="query" required>
                <br>
                <input type="submit" value="Submit">
            </form>
            {% if response %}
                <div class="response">{{ response }}</div>
            {% endif %}
        </div>
    </body>
    </html>
    """, response=response)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
