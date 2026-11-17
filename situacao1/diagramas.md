# Diagramas UML

Para ver no VS Code, instale a extensão "Markdown Preview Mermaid Support" e use Cmd+Shift+V.

## Diagrama de classes
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

## Diagrama de casos de uso
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

## Diagrama de sequência: cadastrar tarefa
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

## Diagrama de atividades: alternar status
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
