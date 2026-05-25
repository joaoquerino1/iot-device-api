# 🔒 IoT Device API

API REST para gerenciamento de dispositivos de segurança eletrônica, desenvolvida com **FastAPI** e **SQLite**.

Inspirada no segmento de segurança eletrônica, a API simula o controle de dispositivos como câmeras, sensores e alarmes — permitindo cadastro, monitoramento de status e registro de eventos.

---

## 🚀 Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [Uvicorn](https://www.uvicorn.org/)

---

## ⚙️ Como rodar o projeto

### Pré-requisitos
- Python 3.10+
- Git

### Instalação

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/iot-device-api.git
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
| POST | `/devices/` | Cadastrar dispositivo |
| GET | `/devices/` | Listar todos os dispositivos |
| GET | `/devices/{id}` | Buscar dispositivo por ID |
| PATCH | `/devices/{id}/toggle` | Ativar ou desativar dispositivo |

### Eventos
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/devices/{id}/events` | Registrar evento em um dispositivo |
| GET | `/devices/{id}/events` | Listar eventos de um dispositivo |

---

## 📁 Estrutura do projeto

```plaintext
iot-device-api/
├── app/
│   ├── main.py
│   ├── database.py
│   ├── models.py
│   ├── schemas.py
│   └── routers/
│       ├── devices.py
│       └── events.py
├── requirements.txt
└── README.md
```

---

## 👨‍💻 Autor

Feito por **João Querino** — em desenvolvimento e aprendizagem contínua 🚀