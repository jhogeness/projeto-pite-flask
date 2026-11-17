# Dicionário de dados

SGBD: SQLite (arquivo `tarefas.db`, criado automaticamente).

## Tabela `materia`
| Campo | Tipo | Tamanho | Nulo | Chave | Descrição |
|---|---|---|---|---|---|
| id | INTEGER | - | Não | PK | Identificador da matéria |
| nome | VARCHAR | 80 | Não | UNIQUE | Nome da matéria (não repete) |

## Tabela `tarefa`
| Campo | Tipo | Tamanho | Nulo | Chave | Descrição |
|---|---|---|---|---|---|
| id | INTEGER | - | Não | PK | Identificador da tarefa |
| titulo | VARCHAR | 120 | Não | - | Título da tarefa |
| descricao | TEXT | - | Sim | - | Detalhes da tarefa |
| prazo | DATE | - | Sim | - | Data limite (AAAA-MM-DD) |
| concluida | BOOLEAN | - | Sim | - | Verdadeiro se concluída (padrão: falso) |
| id_materia | INTEGER | - | Não | FK -> materia.id | Matéria da tarefa |

## Relacionamento
Uma matéria tem muitas tarefas (1:N). Uma tarefa pertence a uma única matéria.

## Regras de valor (validadas no controller)
- `titulo`: obrigatório, até 120 caracteres.
- `nome` da matéria: obrigatório, até 80 caracteres, sem repetição.
- `prazo`: data válida (AAAA-MM-DD) ou vazio.
- `id_materia`: deve ser de uma matéria existente.
