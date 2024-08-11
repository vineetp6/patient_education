from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def init_db():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS medicines (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            brand TEXT NOT NULL,
            indication TEXT NOT NULL,
            systemic TEXT NOT NULL,
            company_name TEXT NOT NULL,
            indication_generic_index TEXT NOT NULL,
            therapitic TEXT NOT NULL,
            generic TEXT NOT NULL,
            pregnancy_category TEXT NOT NULL,
            therapitic_generic TEXT NOT NULL
        )
    ''')
    
    sample_medicines = [
        ('Brand1', 'Indication1', 'Systemic1', 'Company1', 'Index1', 'Therapitic1', 'Generic1', 'Category1', 'TherapiticGeneric1'),
        ('Brand2', 'Indication2', 'Systemic2', 'Company2', 'Index2', 'Therapitic2', 'Generic2', 'Category2', 'TherapiticGeneric2'),
    ]
    
    cursor.executemany('INSERT INTO medicines (brand, indication, systemic, company_name, indication_generic_index, therapitic, generic, pregnancy_category, therapitic_generic) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', sample_medicines)
    
    conn.commit()
    conn.close()

@app.route('/')
def home():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM medicines')
    medicines = cursor.fetchall()
    conn.close()
    return render_template('index.html', medicines=medicines)

@app.route('/search')
def search():
    query = request.args.get('query', '').strip()
    if not query:
        return render_template('index.html', medicines=[])

    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    search_query = f"%{query}%"
    cursor.execute("""
        SELECT * FROM medicines 
        WHERE brand LIKE ? OR indication LIKE ? OR systemic LIKE ? OR company_name LIKE ? OR indication_generic_index LIKE ? OR therapitic LIKE ? OR generic LIKE ? OR pregnancy_category LIKE ? OR therapitic_generic LIKE ?
    """, (search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query, search_query))
    medicines = cursor.fetchall()
    conn.close()

    return render_template('index.html', medicines=medicines)

@app.route('/api/medicines', methods=['GET', 'POST'])
def manage_medicines():
    if request.method == 'GET':
        conn = sqlite3.connect('medicine.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM medicines')
        medicines = cursor.fetchall()
        conn.close()
        return jsonify(medicines)
    elif request.method == 'POST':
        new_medicine = request.json
        conn = sqlite3.connect('medicine.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO medicines (brand, indication, systemic, company_name, indication_generic_index, therapitic, generic, pregnancy_category, therapitic_generic) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', 
                       (new_medicine['brand'], new_medicine['indication'], new_medicine['systemic'], new_medicine['company_name'], new_medicine['indication_generic_index'], new_medicine['therapitic'], new_medicine['generic'], new_medicine['pregnancy_category'], new_medicine['therapitic_generic']))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Medicine added successfully'}), 201

if __name__ == '__main__':
    init_db()  # Initialize the database with sample data
    app.run(debug=True)
