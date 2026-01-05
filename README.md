# 🧠 Cortex Escolar

Sistema web desenvolvido em **Django** para gerenciamento escolar, com foco no cadastro
e visualização de alunos, controle de acesso por autenticação e interface simples
utilizando **Bootstrap**.

---

## 🚀 Funcionalidades

- 🔐 Autenticação de usuários (login e logout)
- 📊 Dashboard inicial
- 👨‍🎓 Cadastro de alunos
- 📋 Listagem de alunos
- 🧭 Rotas protegidas para usuários autenticados
- 🎨 Interface responsiva com Bootstrap

---

## 🛠️ Tecnologias Utilizadas

- Python 3
- Django
- HTML5
- Bootstrap 5
- SQLite (banco padrão do Django)

---

## 📁 Estrutura do Projeto

```
cortex_escolar/
├── alunos/
│   ├── migrations/
│   ├── templates/
│   │   └── alunos/
│   ├── views.py
│   ├── urls.py
│   └── models.py
├── core/
├── templates/
│   └── base.html
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## ⚙️ Como Executar o Projeto

### 1️⃣ Clonar o repositório

```
git clone https://github.com/seu-usuario/cortex-escolar.git
cd cortex-escolar
```

---

### 2️⃣ Criar e ativar o ambiente virtual

#### Windows

```
python -m venv venv
venv\Scripts\activate
```

#### Linux / macOS

```
python3 -m venv venv
source venv/bin/activate
```

---

### 3️⃣ Instalar as dependências

```
pip install -r requirements.txt
```

---

### 4️⃣ Aplicar as migrações

```
python manage.py migrate
```

---

### 5️⃣ Criar superusuário (opcional)

```
python manage.py createsuperuser
```

---

### 6️⃣ Executar o servidor

```
python manage.py runserver
```

---

### 7️⃣ Acessar no navegador

Aplicação:
```
http://127.0.0.1:8000/
```

Admin:
```
http://127.0.0.1:8000/admin/
```

---

## 🔐 Autenticação

- Acesso restrito a usuários autenticados
- Logout seguro via POST com proteção CSRF

---

## 👨‍💻 Autor

André Felipe Oliveira Dutra  
Estudante de Análise e Desenvolvimento de Sistemas  
IFPI – Campus Floriano

---

## 📄 Licença

Projeto livre para fins educacionais.
