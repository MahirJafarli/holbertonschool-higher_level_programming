import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Convert ID and Price to proper types
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # 1. Validate Source
    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    # 2. Load Data
    try:
        if source == 'json':
            products = read_json()
        else:
            products = read_csv()
    except FileNotFoundError:
        return render_template('product_display.html', error="Data file not found")

    # 3. Filter by ID if provided
    if product_id:
        try:
            target_id = int(product_id)
            products = [p for p in products if p['id'] == target_id]
            if not products:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid Product ID")

    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
