from flask import Flask, render_template, request, redirect, send_file
import sqlite3
import os
import pandas as pd
import io

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'ramais.db')

@app.route('/')
def index():
    busca = request.args.get('busca', '').strip()

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    if busca:
        cursor.execute("""
            SELECT * FROM ramais
            WHERE nome LIKE ? OR
                  sobrenome LIKE ? OR
                  email LIKE ? OR
                  ramal LIKE ? OR
                  departamento LIKE ? OR
                  telefone LIKE ?
        """, tuple(['%' + busca + '%'] * 6))
    else:
        cursor.execute("SELECT * FROM ramais")

    ramais = cursor.fetchall()
    conn.close()
    return render_template('index.html', ramais=ramais)

@app.route('/adicionar', methods=['GET', 'POST'])
def adicionar():
    if request.method == 'POST':
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        setor = request.form['setor']
        ramal = request.form['ramal']
        telefone = request.form['telefone']
        email = request.form['email']

        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        cursor.execute("""
            INSERT INTO ramais (nome, sobrenome, departamento, ramal, telefone, email)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, sobrenome, setor, ramal, telefone, email))
        conn.commit()
        conn.close()
        return redirect('/')
    
    return render_template('formulario.html')

@app.route('/editar/<int:id>')
def editar(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM ramais WHERE id = ?", (id,))
    ramal = cursor.fetchone()
    conn.close()
    return render_template('editar.html', ramal=ramal)

@app.route('/atualizar/<int:id>', methods=['POST'])
def atualizar(id):
    nome = request.form['nome']
    sobrenome = request.form['sobrenome']
    setor = request.form['setor']
    ramal = request.form['ramal']
    telefone = request.form['telefone']
    email = request.form['email']

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE ramais
        SET nome = ?, sobrenome = ?, departamento = ?, ramal = ?, telefone = ?, email = ?
        WHERE id = ?
    """, (nome, sobrenome, setor, ramal, telefone, email, id))
    conn.commit()
    conn.close()
    return redirect('/')

@app.route('/deletar/<int:id>')
def deletar(id):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM ramais WHERE id = ?", (id,))
    conn.commit()
    conn.close()
    return redirect('/')

# baixar a lista como Excel
@app.route('/baixar')
def baixar():
    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("""
        SELECT nome, sobrenome, departamento AS setor, ramal, telefone, email FROM ramais
    """, conn)
    conn.close()

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, sheet_name='Ramais', index=False)

    output.seek(0)
    return send_file(
        output,
        download_name="ramais.xlsx",
        as_attachment=True,
        mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
    )

if __name__ == '__main__':
    app.run(debug=True)