# Parte Teórica (entrega) - 2,0 pontos

## 1. Descrição do projeto e escopo inicial
Construção de um sistema simples de gerenciamento de tarefas (Kanban-like) para uma startup de logística.
Escopo inicial: permitir criar, listar, atualizar e deletar tarefas; registrar status e comentários básicos.

## 2. Metodologia ágil adotada
Híbrido: Scrum para cadência de entregas (sprints curtos de 1-2 semanas) e Kanban para fluxo diário.
- Planejamento: backlog no Projects do GitHub (cards)
- Execução: mover cartões entre colunas A Fazer / Em Progresso / Concluído
- Revisão: testes automatizados rodando no GitHub Actions

## 3. Importância da modelagem
Modelagem (UML) ajuda a planejar classes, interfaces e casos de uso. Incluí dois diagramas obrigatórios:
- Diagrama de Casos de Uso (arquivo: usecase.puml)
- Diagrama de Classes (arquivo: classes.puml)

### PlantUML: Diagrama de Casos de Uso (usecase.puml)
```
@startuml
title Casos de Uso - Gerenciador de Tarefas
actor "Usuário" as User
rectangle "Sistema de Tarefas" {
  User -- (Criar Tarefa)
  User -- (Listar Tarefas)
  User -- (Atualizar Tarefa)
  User -- (Deletar Tarefa)
}
@enduml
```

### PlantUML: Diagrama de Classes (classes.puml)
```
@startuml
title Diagrama de Classes - Gerenciador de Tarefas
class Tarefa {
  +int id
  +string titulo
  +string descricao
  +string status
  +criar()
  +atualizar()
  +deletar()
}
class RepositorioTarefas {
  +salvar(t: Tarefa)
  +buscar(id)
  +listar()
  +remover(id)
}
Tarefa --> RepositorioTarefas
@enduml
```

## 4. Testes automatizados utilizados
- Um teste unitário/funcional que cria, recupera, atualiza e deleta uma tarefa usando a API.
- Ferramenta: pytest
- Integração: GitHub Actions roda pytest automaticamente no push para `main`.

## 5. Justificativa de mudança de escopo (exemplo)
Durante o desenvolvimento decidimos priorizar a API REST e os testes automatizados em vez de uma interface web complexa, para garantir que a funcionalidade central estivesse testada e com CI.

## 6. Prints e commits relevantes (instruções)
Inclua no PDF final:
- Print do board Kanban com tarefas distribuídas nas 3 colunas.
- Print do histórico de commits no GitHub mostrando mensagens descritivas.
- Explicação breve (2-3 linhas) do que foi alterado em cada commit relevante.

## 7. Como gerar o PDF/DOCX final (instruções)
Opções:
1) Converter `THEORY.md` + prints para PDF usando seu editor (MS Word / Google Docs / pandoc).
2) No Linux com pandoc:
   ```
   pandoc THEORY.md -o Entrega_Projeto_Agil.pdf
   ```
3) Ou abra o markdown no VS Code e use "Markdown: Export (PDF)".
   
---

## 📸 Evidências no GitHub

### 🧱 Figura 1 — Kanban do Projeto
![Kanban](prints/kanban_projeto.png)
> O quadro Kanban no GitHub mostra as colunas “To Do”, “In Progress” e “Done” com as tarefas organizadas durante o desenvolvimento.

---

### 🧩 Figura 2 — Histórico de Commits
![Commits](prints/commits_projeto.png)
> Histórico de commits evidenciando a evolução do projeto e o uso de versionamento contínuo no GitHub.

---

### ⚙️ Figura 3 — Workflow GitHub Actions
![Actions](prints/github_actions_sucesso.png)
> Execução bem-sucedida do pipeline de integração contínua (CI) configurado no GitHub Actions, validando os testes automatizados.

