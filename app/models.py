from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Materia(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(80), nullable=False, unique=True)
    tarefas = db.relationship("Tarefa", backref="materia", cascade="all, delete")

class Tarefa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(120), nullable=False)
    descricao = db.Column(db.Text)
    prazo = db.Column(db.Date)
    concluida = db.Column(db.Boolean, default=False)
    id_materia = db.Column(db.Integer, db.ForeignKey("materia.id"), nullable=False)