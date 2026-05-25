# 🔒 IoT Device API

API REST para gerenciamento de dispositivos de segurança eletrônica, desenvolvida com **FastAPI** e **SQLite**.

Inspirada no segmento de segurança eletrônica, a API simula o controle de dispositivos como câmeras, sensores e alarmes — permitindo cadastro, monitoramento de status e registro de eventos.

---

## 🚀 Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=python&logoColor=white)
![Uvicorn](https://img.shields.io/badge/Uvicorn-4051B5?style=for-the-badge&logo=python&logoColor=white)

---

## 💡 Sobre o projeto

Este projeto simula uma API de gerenciamento de dispositivos IoT voltada para segurança eletrônica — um segmento amplamente utilizado em empresas do setor de tecnologia.

A API permite:

- 📷 Cadastrar dispositivos como **câmeras**, **sensores** e **alarmes**
- 🔁 Ativar e desativar dispositivos remotamente
- 📋 Registrar e consultar **eventos** como movimentos detectados e alarmes acionados
- ✅ Validar entradas para garantir a integridade dos dados

---

## ⚙️ Como rodar o projeto

### Pré-requisitos
- Python 3.10+
- Git

### Instalação

```bash
# Clone o repositório
git clone https://github.com/joaoquerino1/iot-device-api.git
cd iot-device-api

# Crie e ative o ambiente virtual
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Instale as dependências
pip install -r requirements.txt

# Rode o servidor
uvicorn app.main:app --reload
```

Acesse a documentação interativa em: **http://localhost:8000/docs**

---

## 📡 Endpoints

### Dispositivos

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/devices/` | Cadastrar dispositivo |
| `GET` | `/devices/` | Listar todos os dispositivos |
| `GET` | `/devices/{id}` | Buscar dispositivo por ID |
| `PATCH` | `/devices/{id}/toggle` | Ativar ou desativar dispositivo |

### Eventos

| Método | Rota | Descrição |
|--------|------|-----------|
| `POST` | `/devices/{id}/events` | Registrar evento em um dispositivo |
| `GET` | `/devices/{id}/events` | Listar eventos de um dispositivo |

### Tipos válidos

| Campo | Valores aceitos |
|-------|----------------|
| Tipo de dispositivo | `camera`, `sensor`, `alarm` |
| Tipo de evento | `motion`, `alarm_triggered`, `offline`, `online` |

---

## 📁 Estrutura do projeto

```plaintext
iot-device-api/
├── app/
│   ├── main.py          # Entrada da aplicação
│   ├── database.py      # Configuração do banco de dados
│   ├── models.py        # Modelos das tabelas
│   ├── schemas.py       # Validação de dados com Pydantic
│   └── routers/
│       ├── devices.py   # Rotas de dispositivos
│       └── events.py    # Rotas de eventos
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Autor

Feito por **João Querino** — em desenvolvimento e aprendizagem contínua 🚀

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/joaoquerino1)
