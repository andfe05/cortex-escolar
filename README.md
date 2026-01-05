# 🧠 Cortex Escolar

> Sistema web desenvolvido em **Django** para centralizar e gerenciar informações de alunos de uma escola particular.

Um projeto pensado como um **painel administrativo (dashboard)** simples, seguro e escalável, voltado para organização acadêmica e controle de dados.

---

## ✨ Funcionalidades

✅ Autenticação de usuários (login e logout)  
✅ Dashboard inicial  
✅ Cadastro de alunos  
✅ Listagem de alunos  
✅ Edição de dados  
✅ Exclusão de alunos  
✅ Layout base reutilizável  
✅ Rotas protegidas por autenticação  

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Descrição |
|----------|----------|
| 🐍 Python | Linguagem principal |
| 🌐 Django | Framework web |
| 🎨 HTML5 | Estrutura das páginas |
| 💠 Bootstrap 5 | Estilização e layout |
| 🗄️ SQLite | Banco de dados |
| 🔧 Git | Controle de versão |
| ☁️ GitHub | Hospedagem do código |

---

## 📂 Estrutura do Projeto

CortexEscolar/
│
├── cortex_escolar/        # Configurações do projeto
│
├── alunos/                # App principal
│   ├── templates/
│   │   └── alunos/
│   │       ├── base.html
│   │       ├── dashboard.html
│   │       ├── lista.html
│   │       └── form.html
│   ├── views.py
│   ├── urls.py
│   └── models.py
│
├── venv/                  # Ambiente virtual
├── manage.py
└── README.md

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/andfe05/cortex-escolar.git
cd cortex-escolar

2️⃣ Criar e ativar o ambiente virtual
python -m venv venv
venv\Scripts\activate

3️⃣ Instalar dependências
pip install django

4️⃣ Executar as migrações
python manage.py migrate

5️⃣ Criar superusuário
python manage.py createsuperuser

6️⃣ Rodar o servidor
python manage.py runserver


Acesse no navegador:

http://127.0.0.1:8000/login/

---

🔐 Autenticação

Sistema de autenticação nativo do Django

Apenas usuários autenticados acessam o sistema

Logout realizado de forma segura via POST

📈 Status do Projeto

🟡 Em desenvolvimento

Próximas funcionalidades planejadas:

Perfis de usuários (admin, secretaria, professor)

Relacionamento entre alunos e turmas

Métricas no dashboard

Deploy do sistema

👨‍💻 Autor

André Felipe Oliveira Dutra
🎓 Estudante de Análise e Desenvolvimento de Sistemas
🏫 Instituto Federal do Piauí – IFPI

📌 Projeto desenvolvido para fins educacionais e portfólio.
