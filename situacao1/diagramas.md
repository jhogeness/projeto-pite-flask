# Diagramas UML

Este documento reúne os diagramas UML do Gerenciador de Tarefas de Estudo. Eles descrevem a estrutura de dados, as funcionalidades e o fluxo das principais operações do sistema. Os diagramas foram escritos em Mermaid e são exibidos diretamente pelo GitHub.

## 1. Diagrama de classes
Representa as duas entidades do sistema, Matéria e Tarefa, com seus atributos e o relacionamento de um para muitos entre elas. Corresponde às classes de `app/models.py`.

```mermaid
classDiagram
    class Materia {
        +int id
        +string nome
    }
    class Tarefa {
        +int id
        +string titulo
        +string descricao
        +date prazo
        +bool concluida
        +int id_materia
    }
    Materia "1" --> "0..*" Tarefa : possui
```

## 2. Diagrama de casos de uso
Mostra as funcionalidades disponíveis para o estudante, que é o único ator do sistema. Cada caso de uso corresponde a uma rota de `app/controllers.py`.

```mermaid
flowchart LR
    E([Estudante])
    subgraph Sistema
        U1(Cadastrar matéria)
        U2(Cadastrar tarefa)
        U3(Concluir ou reabrir tarefa)
        U4(Excluir tarefa)
        U5(Listar e filtrar tarefas)
    end
    E --> U1
    E --> U2
    E --> U3
    E --> U4
    E --> U5
```

Funcionalidades não implementadas nesta versão: editar tarefa e excluir matéria.

## 3. Diagrama de sequência: cadastrar tarefa
Detalha o caminho de uma requisição de cadastro, da tela até o banco de dados. Corresponde à função `nova_tarefa` do controller, que valida título, prazo e matéria antes de gravar.

```mermaid
sequenceDiagram
    actor E as Estudante
    participant V as View (formulário)
    participant C as Controller
    participant B as Banco SQLite
    E->>V: Preenche título, matéria e prazo
    V->>C: POST /tarefas/nova
    C->>C: valida título, prazo e matéria
    alt dados inválidos
        C-->>V: mensagem de erro
    else dados válidos
        C->>B: INSERT em tarefa
        B-->>C: confirmação
        C-->>V: redireciona para a lista com mensagem de sucesso
    end
```

## 4. Diagrama de atividades: alternar status
Mostra o fluxo de alternar uma tarefa entre pendente e concluída. Corresponde à função `concluir_tarefa` do controller.

```mermaid
flowchart TD
    A([Início]) --> B[Abrir lista de tarefas]
    B --> C[Clicar em Alternar Status]
    C --> D{Tarefa estava concluída?}
    D -- Sim --> E[Sistema marca como pendente]
    D -- Não --> F[Sistema marca como concluída]
    E --> G[Exibir mensagem de sucesso]
    F --> G
    G --> H([Fim])
```