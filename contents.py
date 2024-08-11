import sqlite3

def print_medicines():
    conn = sqlite3.connect('medicine.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM medicines')
    medicines = cursor.fetchall()
    for medicine in medicines:
        print(medicine)
    conn.close()

print_medicines()
