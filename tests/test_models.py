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


def test_tarefa_sem_titulo_nao_e_gravada(app):
    client = app.test_client()
    with app.app_context():
        db.session.add(Materia(nome="Física"))
        db.session.commit()
    client.post("/tarefas/nova", data={"titulo": "", "id_materia": "1"})
    with app.app_context():
        assert Tarefa.query.count() == 0


def test_prazo_invalido_nao_quebra(app):
    client = app.test_client()
    with app.app_context():
        db.session.add(Materia(nome="Física"))
        db.session.commit()
    r = client.post("/tarefas/nova", data={"titulo": "A", "prazo": "31/12/2026", "id_materia": "1"})
    assert r.status_code == 302
    with app.app_context():
        assert Tarefa.query.count() == 0


def test_tarefa_sem_materia_nao_e_gravada(app):
    client = app.test_client()
    client.post("/tarefas/nova", data={"titulo": "A", "id_materia": ""})
    with app.app_context():
        assert Tarefa.query.count() == 0


def test_materia_duplicada(app):
    client = app.test_client()
    client.post("/materias", data={"nome": "Cálculo"})
    client.post("/materias", data={"nome": "Cálculo"})
    with app.app_context():
        assert Materia.query.count() == 1


def test_alternar_status(app):
    client = app.test_client()
    with app.app_context():
        m = Materia(nome="Física")
        db.session.add(m)
        db.session.commit()
        t = Tarefa(titulo="A", id_materia=m.id)
        db.session.add(t)
        db.session.commit()
        id_t = t.id
    client.post(f"/tarefas/{id_t}/concluir")
    with app.app_context():
        assert db.session.get(Tarefa, id_t).concluida is True