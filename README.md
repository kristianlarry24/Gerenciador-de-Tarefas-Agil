# Projeto Ágil no GitHub - Entrega Prática

![Build Status](https://github.com/kristianlarry24/Gerenciador-de-Tarefas-Agil/actions/workflows/python-app.yml/badge.svg)

Este repositório contém um projeto minimal de exemplo para a disciplina: um sistema básico de gerenciamento de tarefas (CRUD) com:
- Flask (API)
- SQLite (banco local)
- Testes com pytest
- GitHub Actions para rodar os testes automaticamente

---

## 📋 Descrição
Este projeto é um **Gerenciador de Tarefas Ágil**, criado com Flask e SQLite, que permite cadastrar, visualizar e atualizar tarefas.

Inclui:
- Interface web simples (HTML e Flask)
- Banco de dados SQLite
- Metodologia Ágil (Scrum simplificado)
- Testes automatizados (pytest)
- GitHub Actions configurado (CI)

---

## 🧩 Tecnologias utilizadas
- Python 3
- Flask
- SQLite
- Git e GitHub
- GitHub Actions

---

## 🚀 Como rodar o projeto localmente
```bash
git clone https://github.com/kristianlarry24/Gerenciador-de-Tarefas-Agil.git
cd Gerenciador-de-Tarefas-Agil
python -m venv venv
venv\Scripts\activate   # (Windows)
pip install -r requirements.txt
python app.py
