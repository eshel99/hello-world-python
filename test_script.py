print("new test_script") 

import sqlite3

def get_db_connection():
    try:
        conn = sqlite3.connect('autoscraper.db')
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def initialize_db():
    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS run_counter (
            count INTEGER
        )
        ''')
        cursor.execute("INSERT INTO run_counter (count) VALUES (1)")  # Example SQL query
        conn.commit()
        conn.close()

cimport sqlite3

def get_db_connection():
    try:
        conn = sqlite3.connect('autoscraper.db')
        return conn
    except sqlite3.Error as e:
        print(e)
        return None

def initialize_db():
    conn = get_db_connection()
    if conn is not None:
        cursor = conn.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS run_counter (
            count INTEGER
        )
        ''')
        cursor.execute("INSERT INTO run_counter (count) VALUES (1)")  # Example SQL query
        conn.commit()
        conn.close()

AWS_SECRET_ACCESS_KEY='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY' 
