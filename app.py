from flask import Flask, render_template, request, redirect, url_for, g, jsonify
import sqlite3
import os

DATABASE = os.path.join(os.path.dirname(__file__), 'tarefas.db')

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

def init_db():
    conn = sqlite3.connect(DATABASE)
    conn.execute('CREATE TABLE IF NOT EXISTS tarefas (id INTEGER PRIMARY KEY AUTOINCREMENT, titulo TEXT NOT NULL, descricao TEXT, status TEXT NOT NULL)')
    conn.commit()
    conn.close()

app = Flask(__name__)

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route('/')
def index():
    db = get_db()
    cur = db.execute('SELECT * FROM tarefas ORDER BY id DESC')
    tarefas = cur.fetchall()
    return jsonify([dict(t) for t in tarefas])

@app.route('/tarefa', methods=['POST'])
def criar_tarefa():
    data = request.get_json() or {}
    titulo = data.get('titulo')
    descricao = data.get('descricao','')
    status = data.get('status','A Fazer')
    if not titulo:
        return jsonify({'error':'titulo é obrigatório'}), 400
    db = get_db()
    cur = db.execute('INSERT INTO tarefas (titulo, descricao, status) VALUES (?,?,?)', (titulo, descricao, status))
    db.commit()
    tarefa_id = cur.lastrowid
    return jsonify({'id': tarefa_id}), 201

@app.route('/tarefa/<int:id>', methods=['GET'])
def ver_tarefa(id):
    db = get_db()
    cur = db.execute('SELECT * FROM tarefas WHERE id=?', (id,))
    t = cur.fetchone()
    if not t:
        return jsonify({'error':'não encontrado'}), 404
    return jsonify(dict(t))

@app.route('/tarefa/<int:id>', methods=['PUT'])
def atualizar_tarefa(id):
    data = request.get_json() or {}
    db = get_db()
    db.execute('UPDATE tarefas SET titulo=?, descricao=?, status=? WHERE id=?',
               (data.get('titulo'), data.get('descricao'), data.get('status'), id))
    db.commit()
    return jsonify({'ok': True})

@app.route('/tarefa/<int:id>', methods=['DELETE'])
def deletar_tarefa(id):
    db = get_db()
    db.execute('DELETE FROM tarefas WHERE id=?', (id,))
    db.commit()
    return jsonify({'ok': True})

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0', port=5000)
