# 📚 Gerenciador de Tarefas de Estudo (PITE Software II)

Aplicação web desenvolvida em **Python com Flask**, orientada à arquitetura **MVC** (Model-View-Controller), utilizando **SQLite** para persistência de dados, **Bootstrap 5** para a interface visual e **Pytest** para a suíte de testes automatizados.

---

## 📋 Sumário
1. [Situação 1: Modelagem e Requisitos](#situação-1-modelagem-e-requisitos)
2. [Situação 2: Implementação e Testes](#situação-2-implementação-e-testes)
3. [Situação 3: Validação e Testes com Usuários](#situação-3-validação-e-testes-com-usuários)
4. [Como Executar o Projeto](#como-executar-o-projeto)

---

## 🛠️ Situação 1: Modelagem e Requisitos

### 1.1 Visão Geral do Sistema
O **Gerenciador de Tarefas de Estudo** é um sistema voltado para estudantes organizarem suas matérias acadêmicas, definirem prazos de entrega, acompanharem o status de conclusão e gerenciarem sua rotina de estudos de forma prática e centralizada.

### 1.2 Dicionário de Dados
O banco de dados relacional (`SQLite`) é composto por duas entidades principais:

* **Tabela `materia`**
  * `id` (INTEGER, Chave Primária): Identificador único da matéria.
  * `nome` (VARCHAR(100), Obrigatório): Nome da disciplina ou matéria de estudo.

* **Tabela `tarefa`**
  * `id` (INTEGER, Chave Primária): Identificador único da tarefa.
  * `titulo` (VARCHAR(150), Obrigatório): Título descritivo da tarefa ou atividade.
  * `descricao` (TEXT, Opcional): Detalhes ou orientações sobre a tarefa.
  * `data_conclusao` (DATE, Obrigatório): Prazo limite para entrega/conclusão.
  * `status` (VARCHAR(30), Padrão: 'Pendente'): Estado atual (`Pendente`, `Em Andamento`, `Concluída`).
  * `materia_id` (INTEGER, Chave Estrangeira referenciando `materia.id`): Matéria à qual a tarefa pertence.

---

## 💻 Situação 2: Implementação e Testes

### 2.1 Tecnologias Utilizadas
* **Linguagem:** Python 3.9+
* **Framework Web:** Flask & Flask-SQLAlchemy
* **Banco de Dados:** SQLite
* **Front-end:** Bootstrap 5 (via CDN) e Jinja2 Templates
* **Testes Automatizados:** Pytest

### 2.2 Estrutura de Pastas (MVC)
```text
Projeto/
├── app/
│   ├── __init__.py         # Fábrica da aplicação e inicialização do DB
│   ├── models.py           # Modelos de dados (Materia, Tarefa)
│   ├── controllers.py      # Rotas e lógica de controle
│   └── templates/          # Interfaces HTML com Bootstrap
│       ├── base.html
│       ├── index.html
│       ├── form_tarefa.html
│       └── materias.html
├── tests/                  # Testes automatizados com Pytest
├── run.py                  # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
└── README.md               # Documentação oficial