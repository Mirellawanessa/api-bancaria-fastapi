<h1>
  <a href="https://www.dio.me/">
    <img align="center" width="40px" src="https://hermes.digitalinnovation.one/assets/diome/logo-minimized.png">
  </a>  <span> API Bancária Assíncrona com FastAPI</span>
  </h1>

API RESTful assíncrona desenvolvida em Python utilizando FastAPI, para simular operações bancárias básicas como criação de contas, depósitos, saques e transferências. Projeto pensado para ser simples, eficiente e escalável.

---

## 🚀 Tecnologias Utilizadas

- **Python 3.9+**
- **FastAPI** – Framework web moderno, rápido e assíncrono
- **Uvicorn** – Servidor ASGI para rodar a aplicação
- **Pydantic** – Validação e modelagem de dados
- **UUID** – Identificadores únicos para contas
- Desenvolvimento orientado a APIs RESTful e arquitetura assíncrona

---

## 📋 Funcionalidades

- Criação de contas bancárias com identificação única (UUID)
- Consulta de saldo por conta
- Depósitos e saques com validação de saldo
- Transferência entre contas com verificação de saldo
- Tratamento de erros com mensagens claras via HTTP status codes

---

## 🛠️ Estrutura do Projeto
```bash
fastapi-banco/
│
├── app/
│   ├── main.py        # API principal e endpoints
│   ├── models.py      # Modelos de dados usando Pydantic
│   ├── schemas.py     # Schemas para requisições e respostas
│   └── database.py    # Simulação de banco de dados em memória
│
└── requirements.txt   # Dependências do projeto
```

## 💻 Como Executar Localmente

1. Clone o repositório:

```bash
https://github.com/Mirellawanessa/api-bancaria-fastapi.git
cd api-bancaria-fastapi
```
## 💻 Como Executar o Projeto

### Crie e ative um ambiente virtual:

```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```
## 📦 Instale as dependências

```bash
pip install -r requirements.txt
```
## ▶️ Execute a aplicação

```bash
uvicorn app.main:app --reload
```
## 🌐 Acesse a documentação interativa Swagger UI

```bash
[uvicorn app.main:app --reload](http://127.0.0.1:8000/docs)
```
## 🔧 Testando a API
Utilize o Swagger UI ou ferramentas como Postman/cURL para testar os endpoints:

```bash
POST /contas – Criar conta

GET /contas/{conta_id} – Obter dados da conta

POST /contas/{conta_id}/depositar – Depositar valor

POST /contas/{conta_id}/sacar – Sacar valor

POST /transferir – Transferir entre contas
```

## 👩‍💻 Desenvolvedora

<p>
  <img 
    align="left" 
    width="80" 
    src="https://github.com/Mirellawanessa/DIO-Trilha-Java-Basico/blob/main/GitHub/imagens/User.jpeg?raw=true"
  />
  <p>&nbsp;&nbsp;&nbsp;Mirella Wanessa<br>
  &nbsp;&nbsp;&nbsp;
  <a href="https://github.com/Mirellawanessa">GitHub</a>&nbsp;|&nbsp;
  <a href="https://www.linkedin.com/in/mirellawanessa/">LinkedIn</a>&nbsp;|&nbsp;
  <a href="https://www.instagram.com/myfilearchive">Instagram</a>
  &nbsp;|&nbsp;</p>
</p>

---

⌨️ with 💜 by [Mirella Wanessa](https://github.com/Mirellawanessa)

Sinta-se à vontade para deixar uma ⭐ se você curtir o conteúdo!
