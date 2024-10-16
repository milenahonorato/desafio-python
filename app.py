from flask import Flask, request, render_template, redirect
import mysql.connector

app = Flask(__name__)

# Conectar ao banco de dados
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',      # substitua com seu nome de usuário do MySQL
        password='12345abc',    # substitua com sua senha do MySQL
        database='python_db'     # o nome do banco de dados que você criou
    )
    return conn

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM todolist')  # nome da tabela
    items = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add():
    new_item = request.form['task']  # assumindo que o formulário envia uma chave chamada 'task'
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO todolist (task) VALUES (%s)', (new_item,))  # nome da coluna
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)