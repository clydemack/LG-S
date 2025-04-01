GPT Brand Checker - Self-Hosted GPT Tool

1. Requirements:
   - Python 3.7+
   - pip (Python package installer)
   - An OpenAI API key

2. Setup Steps:

A. Run Locally:
---------------
1. Open a terminal
2. Navigate to this folder
3. Install dependencies:
   pip install -r requirements.txt
4. Set your OpenAI API key:
   On Mac/Linux:
     export OPENAI_API_KEY=your-key-here
   On Windows (CMD):
     set OPENAI_API_KEY=your-key-here
5. Start the app:
   python app.py
6. Open your browser to:
   http://localhost:5000

B. Deploy to Free Host (like Render or Railway):
------------------------------------------------
1. Create a new Python app
2. Upload these 3 files: app.py, requirements.txt
3. Set the environment variable:
   OPENAI_API_KEY = your-key-here
4. Deploy and copy your live URL

C. Embed in WordPress:
----------------------
Use an <iframe> in a WordPress post or page:

<iframe src="https://your-app-url.com" width="100%" height="400px" style="border:none;"></iframe>

That's it!
