import json
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items_list():
    """Reads items from a JSON file and renders them in items.html."""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            # Safely extract the list of items
            items = data.get("items", [])
    except (FileNotFoundError, json.JSONDecodeError):
        # Fallback if file is missing or corrupted
        items = []

    return render_template('items.html', items=items)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
