import pytest
from app import create_app
from app.models import db, Materia, Tarefa

@pytest.fixture
def app():
    app = create_app({"SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:", "TESTING": True})
    yield app

def test_criar_tarefa(app):
    with app.app_context():
        m = Materia(nome="Programação")
        db.session.add(m)
        db.session.commit()
        t = Tarefa(titulo="Estudar Flask", id_materia=m.id)
        db.session.add(t)
        db.session.commit()
        assert Tarefa.query.count() == 1

def test_pagina_inicial(app):
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200