Sistema web desenvolvido com Django para centralizar e gerenciar dados de alunos de uma escola particular, funcionando como um painel (dashboard) administrativo simples, seguro e escalável.

🚀 Funcionalidades

🔐 Autenticação de usuários (login e logout)

📊 Dashboard inicial

👨‍🎓 Cadastro de alunos

📋 Listagem de alunos

✏️ Edição de dados dos alunos

🗑️ Exclusão de alunos

🧭 Navegação com layout base reutilizável

🔒 Proteção de rotas (acesso apenas para usuários autenticados)

🛠️ Tecnologias Utilizadas

Python 3

Django 6

HTML5

Bootstrap 5

SQLite (banco padrão do Django)

Git & GitHub

📁 Estrutura do Projeto
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

⚙️ Como Executar o Projeto
1️⃣ Clone o repositório
git clone https://github.com/andfe05/cortex-escolar.git
cd cortex-escolar

2️⃣ Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate   # Windows

3️⃣ Instale as dependências
pip install django

4️⃣ Execute as migrações
python manage.py migrate

5️⃣ Crie um superusuário
python manage.py createsuperuser

6️⃣ Rode o servidor
python manage.py runserver


Acesse no navegador:

http://127.0.0.1:8000/login/

🔐 Autenticação

O sistema utiliza o sistema de autenticação nativo do Django

Apenas usuários logados podem acessar o dashboard e os cadastros

Logout feito de forma segura via método POST

📌 Status do Projeto

🟢 Em desenvolvimento

Próximos passos planejados:

Perfis de usuário (admin, secretaria, professor)

Relacionamento entre alunos e turmas

Métricas no dashboard

Deploy do sistema

👨‍💻 Autor

André Felipe Oliveira Dutra
Estudante de Análise e Desenvolvimento de Sistemas
Instituto Federal do Piauí – IFPI

📌 Projeto desenvolvido para fins de estudo e portfólio.
