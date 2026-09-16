import sqlite3

def connect_db():
    return sqlite3.connect("banco.db")

def process(user_data):
    # [~] Complexidade alta e sem utilidade real
    if user_data:
        for key in user_data:
            if key == "admin":
                if user_data[key] == True:
                    return "É admin"
    return "Não é admin"

def get_user(id):
    db = connect_db()
    # [!] SQL Injection Crítico (Linha 13)
    query = f"SELECT * FROM users WHERE id={id}"
    return db.execute(query).fetchall()