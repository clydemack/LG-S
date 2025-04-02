from flask import Flask, request, render_template_string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    result = ""
    if request.method == "POST":
        query = request.form.get("query", "")
        # Simulated response (replace with AI or custom logic if needed)
        result = f"You searched for: <strong>{query}</strong><br>This would show your brand if AI tools ranked it."

    return render_template_string("""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <style>
            body {
                font-family: Arial, sans-serif;
                padding: 20px;
                margin: 0;
            }
            form {
                max-width: 100%;
            }
            input[type="text"] {
                width: 100%;
                padding: 10px;
                margin-bottom: 10px;
                box-sizing: border-box;
            }
            button {
                padding: 10px 15px;
                background-color: #f26522;
                color: white;
                border: none;
                cursor: pointer;
                font-weight: bold;
            }
            .result {
                margin-top: 20px;
                padding: 15px;
                background: #f5f5f5;
                word-wrap: break-word;
                white-space: pre-wrap;
                box-shadow: 0 0 8px rgba(0,0,0,0.1);
            }
        </style>
    </head>
    <body>
        <form method="POST">
            <label for="query"><strong>Type a search query:</strong></label><br>
            <input type="text" id="query" name="query" required>
            <br>
            <button type="submit">Submit</button>
        </form>
        {% if result %}
            <div class="result">{{ result|safe }}</div>
        {% endif %}
    </body>
    </html>
    """, result=result)
