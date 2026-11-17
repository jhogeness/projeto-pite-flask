# Laudo de Qualidade

**Sistema:** Gerenciador de Tarefas de Estudo  
**Responsável:** Jhogenes Leonel  
**Disciplina:** Projeto Integrador Transdisciplinar em Engenharia de Software II  
**Data:** 17/11/2026  
**Repositório:** https://github.com/jhogeness/projeto-pite-flask  

## 1. Metodologia
A avaliação combinou revisão do código-fonte, testes manuais pelo navegador, requisições diretas ao servidor com entradas inválidas e a execução da suíte de testes automatizados (`pytest`). Os erros descritos neste laudo foram identificados na primeira versão do sistema (commit `a7efd3d`) e corrigidos no commit `b14198b`.

## 2. Resumo
A primeira versão funcionava no fluxo normal, mas não tratava entradas inválidas: um dado fora do formato derrubava a requisição com erro 500, e dados incorretos chegavam ao banco. Foram corrigidos três erros do sistema, a cobertura de testes passou de 2 para 7 testes e a documentação foi alinhada ao código.

## 3. Erros encontrados e correções
| ID | Erro | Como reproduzir | Criticidade | Correção | Evidência |
|---|---|---|---|---|---|
| E1 | Prazo em formato inválido causava erro 500 (`ValueError`) | Enviar `prazo=31/12/2026` ao cadastrar uma tarefa | Alta | A conversão da data passou para um `try/except`, e o sistema exibe mensagem de tratamento adequado. | Evidências 1 e 2 |
| E2 | Título só com espaços era aceito, e a tarefa era gravada com título em branco | Digitar apenas espaços no título | Média | O título passou por `strip()` antes da validação, com limite de 120 caracteres | Evidências 3 e 4 |
| E3 | Tarefa gravada com matéria vazia ou inexistente | Enviar `id_materia` vazio | Alta | O sistema só grava se a matéria existir; caso contrário exibe "Escolha uma matéria válida." | Evidências 5 e 6 |
| E4 | Cobertura de testes insuficiente: 2 testes, nenhum de tratamento de erro | Executar `pytest -v` na versão antiga | Média | Criados 5 testes: título vazio, prazo inválido, matéria ausente, matéria duplicada e alternância de status | Evidência 7 |
| E5 | README e dicionário de dados descreviam campos inexistentes no banco (`data_conclusao`, `status`, `materia_id`) | Comparar o README com `app/models.py` | Baixa | README e dicionário reescritos com os campos reais: `prazo`, `concluida` e `id_materia` | Evidência 8 |

## 4. Resultado dos testes automatizados
- **Versão antiga:** 2 testes aprovados, sem cobertura de erros.
- **Versão atual:** 7 testes aprovados (`pytest -v`).

## 5. Pontos em aberto (melhorias futuras)
- Não é possível editar tarefas nem excluir matérias.
- Os formulários não têm proteção CSRF, o que é aceitável para o uso acadêmico e local.
- O `base.html` não possui a meta tag de viewport, o que prejudica a exibição em celulares.
- Os rótulos dos formulários não estão associados aos campos, o que afeta a acessibilidade.
- O prazo é exibido no formato AAAA-MM-DD.
- A exclusão de tarefas e os filtros foram verificados manualmente, sem teste automatizado.

## 6. Conclusão
O sistema atende aos requisitos da disciplina: front-end, back-end no padrão MVC, banco de dados, tratamento de erros e testes automatizados. Os erros críticos foram corrigidos e comprovados por testes automatizados e por requisições de verificação. As melhorias listadas na seção 5 ficam como evolução futura.
