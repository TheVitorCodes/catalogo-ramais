import pandas as pd
import sqlite3
import os

# Caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, 'ramais.db')
excel_path = os.path.join(BASE_DIR, 'ramais.xlsx')  # nome real da planilha

# Carregar a planilha
df = pd.read_excel(excel_path)

# Função para dividir nome completo
# Processar dados
registros = []
for _, row in df.iterrows():
    nome = str(row['Nome']).strip() if not pd.isna(row['Nome']) else ''
    sobrenome = str(row['Sobrenome']).strip() if not pd.isna(row['Sobrenome']) else ''

    setor = str(row['Setor']).strip() if not pd.isna(row['Setor']) else ''
    ramal = str(row['Ramal']).strip() if not pd.isna(row['Ramal']) else ''
    telefone = str(row['Telefone']).strip() if not pd.isna(row['Telefone']) else ''
    email = str(row['Email']).strip() if not pd.isna(row['Email']) else ''

    registros.append((nome, sobrenome, setor, ramal, telefone, email))

# Inserir no banco
conexao = sqlite3.connect(db_path)
cursor = conexao.cursor()

# Cria a tabela se não existir
cursor.execute('''
    CREATE TABLE IF NOT EXISTS ramais (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        sobrenome TEXT,
        departamento TEXT NOT NULL,
        ramal TEXT NOT NULL,
        telefone TEXT,
        email TEXT
    )
''')

cursor.executemany('''
    INSERT INTO ramais (nome, sobrenome, departamento, ramal, telefone, email)
    VALUES (?, ?, ?, ?, ?, ?)
''', registros)

conexao.commit()
conexao.close()

print(f"✅ {len(registros)} registros importados com sucesso!")