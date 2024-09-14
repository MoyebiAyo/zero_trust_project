import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Zero Trust Framework on Render!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use the PORT environment variable provided by Render
    app.run(host="0.0.0.0", port=port)