# Gerenciador de Tarefas de Estudo

Projeto Integrador Transdisciplinar em Engenharia de Software II, de SEU NOME (Cruzeiro do Sul Virtual).

Aplicação web em **Python com Flask**, na arquitetura **MVC** (Model-View-Controller), com **SQLite** para persistência, **Bootstrap 5** na interface e **Pytest** nos testes automatizados.

## Sumário
1. [Situação 1: modelagem](#situação-1-modelagem)
2. [Situação 2: implementação](#situação-2-implementação)
3. [Situação 3: validação](#situação-3-validação)
4. [Como executar](#como-executar)

---

## Situação 1: modelagem

### Visão geral
O sistema ajuda estudantes a organizar tarefas por matéria, definir prazos, marcar tarefas como concluídas e filtrar a lista por situação.

### Dicionário de dados
SGBD: SQLite (arquivo `tarefas.db`, criado automaticamente ao iniciar a aplicação).

**Tabela `materia`**
- `id` (INTEGER, chave primária): identificador da matéria.
- `nome` (VARCHAR(80), obrigatório, único): nome da matéria.

**Tabela `tarefa`**
- `id` (INTEGER, chave primária): identificador da tarefa.
- `titulo` (VARCHAR(120), obrigatório): título da tarefa.
- `descricao` (TEXT, opcional): detalhes da tarefa.
- `prazo` (DATE, opcional): data limite.
- `concluida` (BOOLEAN, padrão falso): indica se a tarefa foi concluída.
- `id_materia` (INTEGER, obrigatório, chave estrangeira para `materia.id`): matéria da tarefa.

**Relacionamento:** uma matéria possui várias tarefas (1:N). Uma matéria com tarefas é excluída junto com elas (cascata).

### Documentação de modelagem
- [Dicionário de dados completo](situacao1/dicionario-de-dados.md)
- [Diagramas UML](situacao1/diagramas.md)
- [Telas e mensagens de erro (IHC)](situacao1/telas-e-mensagens.md)

---

## Situação 2: implementação

### Funcionalidades
- Cadastrar matérias (sem repetição).
- Cadastrar tarefas com título, descrição, matéria e prazo.
- Alternar a tarefa entre pendente e concluída.
- Excluir tarefas, com confirmação.
- Filtrar tarefas: todas, pendentes e concluídas.
- Validação de dados com mensagens de erro (título vazio, prazo inválido, matéria inválida ou repetida).

### Tecnologias
- Python 3 e Flask
- Flask-SQLAlchemy e SQLite
- Bootstrap 5 (via CDN) e templates Jinja2
- Pytest

### Estrutura do projeto (MVC)
```text
app/
├── __init__.py       # fábrica da aplicação e criação do banco
├── models.py         # Model: Materia e Tarefa
├── controllers.py    # Controller: rotas e validações
└── templates/        # View: páginas HTML
    ├── base.html
    ├── index.html
    ├── form_tarefa.html
    └── materias.html
tests/                # testes automatizados
situacao1/            # modelagem
situacao2/            # manual de uso e vídeo
situacao3/            # testes e validação
run.py                # ponto de entrada
requirements.txt      # dependências
pytest.ini            # configuração do pytest
```

### Manual e vídeo
- [Manual de uso e vídeo de demonstração](situacao2/README.md)

---

## Situação 3: validação

- Testes automatizados (verificação): [resultado-testes.txt](situacao3/resultado-testes.txt)
- Testes com colegas (validação), correções e vídeo: [situacao3/README.md](situacao3/README.md)

---

## Como executar

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python run.py
```

Acesse http://127.0.0.1:5001

Para rodar os testes:

```bash
 python -m pytest -v
```