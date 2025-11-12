import os
import tempfile
import json
import pytest
from Gerenciador_de_Tarefas_Agil.app import app, init_db, DATABASE

@pytest.fixture
def client(tmp_path, monkeypatch):
    # Use a temporary database file for tests
    db_file = tmp_path / "test_tarefas.db"
    monkeypatch.setenv('DATABASE', str(db_file))
    # Ensure the app uses the test database path
    app.config['TESTING'] = True
    # initialize DB
    init_db()
    with app.test_client() as client:
        yield client

def test_criar_ver_deletar_tarefa(client):
    # create
    rv = client.post('/tarefa', json={'titulo':'Teste 1','descricao':'desc','status':'A Fazer'})
    assert rv.status_code == 201
    jd = rv.get_json()
    tid = jd['id']
    # get
    rv = client.get(f'/tarefa/{tid}')
    assert rv.status_code == 200
    data = rv.get_json()
    assert data['titulo'] == 'Teste 1'
    # update
    rv = client.put(f'/tarefa/{tid}', json={'titulo':'Teste 1 edit','descricao':'desc edit','status':'Concluído'})
    assert rv.status_code == 200
    # delete
    rv = client.delete(f'/tarefa/{tid}')
    assert rv.status_code == 200
