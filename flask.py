# File: Site.py
from flask import Flask, render_template_string, request
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string('''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Run Main</title>
        </head>
        <body>
            <h1>Activate Main Script</h1>
            <form action="/activate" method="post">
                <button type="submit">Activate</button>
            </form>
        </body>
        </html>
    ''')

@app.route('/activate', methods=['POST'])
def activate():
    try:
        # Execute the main.py script
        result = subprocess.run(['python', 'main.py'], capture_output=True, text=True)
        output = result.stdout
    except Exception as e:
        output = f"An error occurred: {e}"
    return f"<pre>{output}</pre>"

if __name__ == '__main__':
    app.run(debug=True)

# File: main.py
def main():
    print("Hello, this is the main script running!")

if __name__ == "__main__":
    main()
