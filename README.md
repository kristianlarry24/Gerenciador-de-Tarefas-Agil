# Projeto Ágil no GitHub - Entrega Prática

![Build Status](https://github.com/kristianlarry24/Gerenciador-de-Tarefas-Agil/actions/workflows/python-app.yml/badge.svg)

Este repositório contém um projeto minimal de exemplo para a disciplina: um sistema básico de gerenciamento de tarefas (CRUD) com:
- Flask (API)
- SQLite (banco local)
- Testes com pytest
- GitHub Actions para rodar os testes automaticamente

## O que eu entreguei aqui
1. Código funcional (app.py, models.py)
2. Testes (tests/test_app.py)
3. Workflow GitHub Actions (.github/workflows/python-app.yml)
4. Arquivo THEORY.md com a parte teórica, UML (PlantUML) e instruções para gerar PDF/DOCX.
5. PlantUML para diagramas de Casos de Uso e Classes.

## Passo a passo (do zero) — como usar localmente e publicar no GitHub

### Pré-requisitos
- Git instalado
- Python 3.8+
- pip
- (opcional) VS Code ou outro editor

### 1) Clonar / criar repositório local
Se você tem o ZIP deste projeto: descompacte e entre na pasta:
```bash
unzip ProjetoAgil_GitHub.zip
cd ProjetoAgil_GitHub
```

Se quiser criar um novo repositório e enviar para o GitHub:
```bash
git init
git add .
git commit -m "Entrega inicial - Projeto Ágil"
# crie um repositório no GitHub (no site) e copie a URL, por exemplo:
git remote add origin https://github.com/SEU_USUARIO/NOME_REPO.git
git branch -M main
git push -u origin main
```

### 2) Rodar localmente
1. Crie e ative um ambiente virtual (recomendado)
```bash
python -m venv venv
# Windows
venv\Scripts\activate
# Linux / macOS
source venv/bin/activate
```
2. Instale dependências
```bash
pip install flask pytest
```
3. Inicialize o banco (é automático no primeiro start) e rode a app
```bash
python app.py
```
A API ficará disponível em http://127.0.0.1:5000

### 3) Testes
Rode:
```bash
pytest -q
```

### 4) Abrir Kanban no GitHub
No site do GitHub, vá em **Projects** (ou Projects > New project) e crie um board com colunas: **A Fazer**, **Em Progresso**, **Concluído**. Adicione ao menos 10 commits e mova cards durante o desenvolvimento.

### 5) GitHub Actions
Ao empurrar para `main`, o workflow `.github/workflows/python-app.yml` será acionado automaticamente. Ele executa `pytest`.

### 6) Documentação e mudança de escopo
Edite `README.md` e `THEORY.md` para registrar justificativa de mudanças. Tire prints do Kanban e dos commits relevantes e inclua no documento final (PDF/DOCX).

## Arquivos principais
- app.py — API Flask
- models.py — helpers (placeholder)
- tests/test_app.py — testes pytest
- .github/workflows/python-app.yml — CI para rodar testes
- THEORY.md — parte teórica e UML (veja também os .puml)

