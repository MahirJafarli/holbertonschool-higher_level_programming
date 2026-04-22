import json
import csv
import sqlite3
import os
from flask import Flask, render_template, request

app = Flask(__name__)

def create_database():
    """Creates the SQLite database and populates it with initial data."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    # Check if data already exists to avoid duplicate entries
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
        conn.commit()
    conn.close()

def read_json():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql(product_id=None):
    """Fetches data from the SQLite database."""
    try:
        conn = sqlite3.connect('products.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()

        if product_id:
            cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
        else:
            cursor.execute('SELECT * FROM Products')
        
        rows = cursor.fetchall()
        products = [dict(row) for row in rows]
        conn.close()
        return products
    except sqlite3.Error:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    products = []
    if source == 'json':
        try:
            products = read_json()
        except FileNotFoundError:
            return render_template('product_display.html', error="JSON file not found")
            
    elif source == 'csv':
        try:
            products = read_csv()
        except FileNotFoundError:
            return render_template('product_display.html', error="CSV file not found")
            
    elif source == 'sql':
        products = read_sql(product_id)
        if products is None:
            return render_template('product_display.html', error="Database error")
        if product_id and not products:
             return render_template('product_display.html', error="Product not found")
        return render_template('product_display.html', products=products)

    # Filtering for JSON/CSV
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
    # Initialize the database file before starting the server
    create_database()
    # Run the Flask app
    app.run(debug=True, port=5000)
