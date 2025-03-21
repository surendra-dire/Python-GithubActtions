# app.py
from flask import Flask
import sys

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Flask Web Application!"

if __name__ == '__main__':
    try:
        app.run(debug=True, host='0.0.0.0')  # Ensure it's listening on all interfaces
    except Exception as e:
        print(f"Error occurred: {e}", file=sys.stderr)
        sys.exit(1)  # Exit with an error code if something goes wrong
