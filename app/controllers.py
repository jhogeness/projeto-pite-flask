from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for, flash, abort
from .models import db, Materia, Tarefa

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    status = request.args.get('status')
    query = Tarefa.query
    if status == 'pendente':
        query = query.filter_by(concluida=False)
    elif status == 'concluida':
        query = query.filter_by(concluida=True)
    
    tarefas = query.all()
    materias = Materia.query.all()
    return render_template('index.html', tarefas=tarefas, materias=materias, status_atual=status)

@bp.route('/tarefas/nova', methods=['GET', 'POST'])
def nova_tarefa():
    materias = Materia.query.all()
    if request.method == 'POST':
        titulo = request.form.get('titulo')
        descricao = request.form.get('descricao')
        prazo_str = request.form.get('prazo')
        id_materia = request.form.get('id_materia')

        if not titulo:
            flash("O título é obrigatório!", "danger")
            return redirect(url_for('main.nova_tarefa'))

        prazo = datetime.strptime(prazo_str, '%Y-%m-%d').date() if prazo_str else None

        nova = Tarefa(
            titulo=titulo,
            descricao=descricao,
            prazo=prazo,
            id_materia=id_materia
        )
        db.session.add(nova)
        db.session.commit()
        flash("Tarefa criada com sucesso!", "success")
        return redirect(url_for('main.index'))

    return render_template('form_tarefa.html', materias=materias, tarefa=None)

@bp.route('/tarefas/<int:id>/concluir', methods=['POST'])
def concluir_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    tarefa.concluida = not tarefa.concluida
    db.session.commit()
    flash("Status da tarefa alterado!", "success")
    return redirect(url_for('main.index'))

@bp.route('/tarefas/<int:id>/excluir', methods=['POST'])
def excluir_tarefa(id):
    tarefa = Tarefa.query.get_or_404(id)
    db.session.delete(tarefa)
    db.session.commit()
    flash("Tarefa excluída com sucesso!", "success")
    return redirect(url_for('main.index'))

@bp.route('/materias', methods=['GET', 'POST'])
def materias():
    if request.method == 'POST':
        nome = request.form.get('nome')
        if not nome:
            flash("O nome da matéria é obrigatório!", "danger")
        else:
            existente = Materia.query.filter_by(nome=nome).first()
            if existente:
                flash("Essa matéria já existe!", "warning")
            else:
                m = Materia(nome=nome)
                db.session.add(m)
                db.session.commit()
                flash("Matéria cadastrada com sucesso!", "success")
        return redirect(url_for('main.materias'))

    lista = Materia.query.all()
    return render_template('materias.html', materias=lista)