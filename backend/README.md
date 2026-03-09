# Índice

- [Stack do Backend](#stack-do-backend)
- [Pré-requisitos](#pré-requisitos)
- [Como subir o Backend](#como-subir-o-backend)
- [Configuração de Ambiente](#configuração-de-ambiente)
- [Estrutura esperada do backend](#estrutura-esperada-do-backend)
- [Comandos úteis](#comandos-úteis)
- [Metodologia de Desenvolvimento (TDD)](#metodologia-de-desenvolvimento-tdd)
- [APIs e Consumo no Frontend](#apis-e-consumo-no-frontend)
- [Testes](#testes)
- [Qualidade de código](#qualidade-de-código)
- [SonarQube](#sonarqube)
- [Build do projeto](#build-do-projeto)
- [Banco de dados](#banco-de-dados)
- [Comandos Docker úteis](#comandos-docker-úteis)
- [Fluxo recomendado de desenvolvimento](#fluxo-recomendado-de-desenvolvimento)
- [Resumo](#resumo)

---

# Stack 

### Framework
- **Django** — framework principal do backend
- **Django REST Framework (DRF)** — para APIs REST
- **PostgreSQL** — banco de dados

### Testes
- **Pytest** — testes unitários e de integração
- **Coverage** — medição de cobertura de testes

### Qualidade de código
- **Ruff** — linting e formatação
- **Black** — formatação de código
- **SonarQube** — análise avançada de qualidade, segurança e cobertura

---

# Pré-requisitos

Para trabalhar no backend você precisa apenas de:

- **Docker**
- **Docker Compose**

Antes de começar, confirme se estão instalados executando estes comandos no terminal:

```bash
docker --version
docker compose version
```

Se não estiverem instalados, baixe e instale do site oficial: https://docker.com

---

# Como subir o Backend

Na raiz do projeto execute:

```bash
docker compose up --build
```

Para rodar em segundo plano:

```bash
docker compose up -d --build
```

O container do backend vai:

1. Aguardar o PostgreSQL ficar pronto
2. Aplicar as migrações automaticamente
3. Iniciar o servidor Django

Depois disso o backend estará disponível em: http://localhost:8000

API principal: http://localhost:8000/api/

Admin Django: http://localhost:8000/admin/

---

# Configuração de Ambiente

O projeto usa variáveis de ambiente para configurações específicas.

Copie o arquivo de exemplo:

Linux/Mac

```bash
cp .env.example .env
```

Windows

```bash
copy .env.example .env
```

Após alterar o `.env`, reinicie:

```bash
docker compose down
docker compose up --build
```

---

# Estrutura esperada do backend

```text
backend/
│
├─ project/
│  ├─ settings.py
│  ├─ urls.py
│  ├─ asgi.py
│  └─ wsgi.py
│
├─ users/
│  ├─ migrations/
│  ├─ models.py
│  ├─ serializers.py
│  ├─ views.py
│  ├─ urls.py
│  └─ tests.py
│
├─ core/
│  ├─ views.py
│  └─ urls.py
│
├─ manage.py
├─ requirements.txt
├─ pyproject.toml
├─ sonar-project.properties
├─ Dockerfile
├─ docker-compose.yml
└─ .env.example
```

---

# Comandos úteis

Entrar no container:

```bash
docker compose exec backend sh
```

Rodar migrações:

```bash
docker compose exec backend python manage.py migrate
```

Criar migrações:

```bash
docker compose exec backend python manage.py makemigrations
```

Criar superuser:

```bash
docker compose exec backend python manage.py createsuperuser
```

Abrir shell Django:

```bash
docker compose exec backend python manage.py shell
```

---

# Metodologia de Desenvolvimento (TDD)

Este projeto segue **Test Driven Development (TDD)**.

Fluxo:

1. Criar o teste
2. Rodar teste (falha)
3. Implementar código mínimo
4. Teste passa
5. Refatorar

---

# APIs e Consumo no Frontend

Todas as respostas são em JSON.

### Core

GET `/api/health/`

Resposta:

```json
{
  "status": "ok"
}
```

### Users

GET `/api/users/`  
POST `/api/users/`  
GET `/api/users/{id}/`  
PUT `/api/users/{id}/`  
PATCH `/api/users/{id}/`  
DELETE `/api/users/{id}/`

---

# Testes

Rodar testes:

```bash
docker compose exec backend pytest
```

Cobertura:

```bash
docker compose exec backend coverage run -m pytest
docker compose exec backend coverage report
```

---

# Qualidade de código

Ruff:

```bash
docker compose exec backend ruff check .
```

Black:

```bash
docker compose exec backend black --check .
```

---

# SonarQube

Acesse: http://localhost:9000

Credenciais:

admin / admin

Executar análise:

```bash
docker compose exec backend coverage run -m pytest
docker compose exec backend coverage xml

docker run --rm --network backend_default -v $(pwd):/usr/src sonarsource/sonar-scanner-cli
```

---

# Build do projeto

O backend roda via Docker.

Para produção utilize o Dockerfile.

---

# Banco de dados

PostgreSQL em container.

Host interno: postgres  
Host local: localhost  
Porta: 5432  

---

# Comandos Docker úteis

Ver containers:

```bash
docker ps
```

Logs:

```bash
docker compose logs
```

Parar:

```bash
docker compose down
```

---

# Fluxo recomendado de desenvolvimento

1. Clonar repositório

2. Copiar .env

```bash
cp .env.example .env
```

3. Subir ambiente

```bash
docker compose up --build
```

4. Confirmar API http://localhost:8000/api/health/

5. Antes de PR:

```bash
docker compose exec backend pytest
docker compose exec backend ruff check .
docker compose exec backend black --check .
```

---

# Resumo

Depois de clonar:

```bash
cp .env.example .env
docker compose up --build
```

Backend disponível em: http://localhost:8000