from flask import Flask
import os  # Import os to get environment variables

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Boston Transit!"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Get PORT from Heroku, default to 5000 locally
    app.run(host="0.0.0.0", port=port)  # Bind to all network interfaces
