# Guia de Instalação, Execução e Estrutura do Projeto Django Library API

## 1. Requisitos

* **Sistema**: Linux ou macOS (ou Windows com pyenv-win)
* **Ferramentas**: `git`, `curl`, `build-essential` (toolchain C)
* **Gerenciadores**: `pyenv` e `venv`

---

## 2. Instalar o pyenv

### Linux / macOS

```bash
sudo apt update
sudo apt install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev git

curl https://pyenv.run | bash
```

Adicione ao seu shell:

```bash
export PATH="$HOME/.pyenv/bin:$PATH"
eval "$(pyenv init --path)"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Depois reinicie o terminal ou rode `source ~/.bashrc`.

---

## 3. Instalar o Python 3.13.5

```bash
pyenv install 3.13.5
pyenv global 3.13.5
python --version  # Deve exibir Python 3.13.5
```

---

## 4. Criar e ativar o ambiente virtual

```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\Activate.ps1  # Windows PowerShell
```

---

## 5. Instalar dependências

### Arquivo `requirements.txt`

```text
Django>=4.2
djangorestframework>=3.14
djangorestframework-simplejwt>=5.2
drf-spectacular>=0.28
pytest>=7.0
pytest-django>=4.5
```

### Instalar dependências

```bash
pip install --upgrade pip setuptools wheel
pip install -r requirements.txt
```

---

## 6. Configurar o projeto

### Criar migrações e banco de dados

```bash
python manage.py makemigrations
python manage.py migrate
```

### Criar superusuário

```bash
python manage.py createsuperuser
```

### Executar servidor

```bash
python manage.py runserver
```

Acesse:

* Admin: [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
* API base: [http://127.0.0.1:8000/api/](http://127.0.0.1:8000/api/)

---

## 7. Rodar testes

```bash
python manage.py test
```

Ou, se estiver usando pytest:

```bash
pytest
```

---

## 8. Estrutura do Projeto

```
biblioteca_api/
├── manage.py
├── config/
│   ├── settings.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
└── core/
    ├── admin.py
    ├── apps.py
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    ├── tests.py
    └── migrations/
```

---

## 9. Descrição dos Módulos

### `models.py`

Define as entidades principais:

* **User**: herda de `AbstractUser` e inclui o campo `is_librarian`.
* **Book**: representa um livro, com campos como `title`, `author`, `published_year`.
* **Library**: representa a biblioteca de um usuário e relaciona-se com livros e dono.

### `serializers.py`

Transforma os modelos Python em JSON (e vice-versa):

* `UserSerializer`
* `BookSerializer`
* `LibrarySerializer`

### `views.py`

Usa `ModelViewSet` para CRUD automático:

* `UserViewSet`
* `BookViewSet`
* `LibraryViewSet`

Com permissões e ações customizadas.

### `urls.py`

Registra os roteadores DRF:

```python
router.register(r'users', UserViewSet)
router.register(r'books', BookViewSet)
router.register(r'libraries', LibraryViewSet)
```

### `admin.py`

Configura os modelos no painel administrativo, incluindo exibição do campo `is_librarian`.

### `tests.py`

Contém testes unitários e de integração para validar comportamento dos modelos e endpoints.

---

## 10. Boas Práticas

* Use HTTPS em produção.
* Utilize tokens JWT para autenticação segura.
* Versione migrações e mantenha testes automatizados.
* Documente endpoints com `drf-spectacular`.
* Mantenha `.env` e `.venv` fora do controle de versão.

---

## 11. Exemplo de .gitignore

```gitignore
# Ambiente virtual
.venv/

# Cache e arquivos temporários
__pycache__/
*.pyc
*.pyo
*.pyd

# Banco de dados local
db.sqlite3

# Configurações locais
.env

# Arquivos de logs
*.log

# Diretório de migrações compiladas
**/migrations/__pycache__/
```

---

Autor: Abraão Brandão
Curso: Engenharia de Software