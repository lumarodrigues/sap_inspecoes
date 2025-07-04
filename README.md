
# 🔧 API de Inspeções Técnicas Industriais com Integração SAP PM (Mock)

Este projeto é uma API RESTful desenvolvida com Django e Django REST Framework (DRF), destinada ao registro de inspeções técnicas em equipamentos estáticos como vasos de pressão, tanques, permutadores e filtros. Cada inspeção registrada também é integrada (simulada) com um endpoint externo que representa o sistema SAP PM.

---

## 🚀 Funcionalidades

- ✅ Registro de inspeções técnicas industriais.
- 📂 Upload de imagem do equipamento inspecionado.
- 🔎 Listagem e consulta detalhada das inspeções.
- 🔄 Envio automático de dados para uma API externa simulando o SAP PM.
- 🐳 Containerização com Docker & Docker Compose.
- 📘 Documentação automática da API com Swagger (drf-yasg).
- 🐘 Banco de dados PostgreSQL.

---

## 📦 Tecnologias Utilizadas

| Camada           | Tecnologias                          |
|------------------|--------------------------------------|
| Backend          | Django 4.x, Django REST Framework    |
| API Doc          | Swagger (via drf-yasg)               |
| Banco de Dados   | PostgreSQL                           |
| Containerização  | Docker & Docker Compose              |
| Integração Mock  | requests (simulando envio ao SAP PM) |
| Upload Imagem    | Pillow                               |

---

## 🧱 Modelagem de Dados

A inspeção técnica contém os seguintes campos:

| Campo                      | Tipo        | Descrição                                             |
|---------------------------|-------------|--------------------------------------------------------|
| data_inspecao             | Date        | Data em que foi realizada a inspeção                  |
| tecnico_responsavel       | String      | Nome do técnico que realizou a inspeção               |
| plataforma                | Enum        | Ex: P-1, P-2, P-3, P-4                                |
| modulo                    | Enum        | Ex: M01 até M10                                       |
| setor                     | Enum        | S01, S02, S03                                         |
| tipo_equipamento          | Enum        | Vaso, Tanque, Permutador, Filtro                      |
| tag                       | String      | Código do equipamento (ex: VP-001, TQ-003)            |
| defeito                   | Enum        | Ex: vazamento, trinca, desgaste                       |
| causa                     | Enum        | Ex: corrosão interna, impacto                         |
| categoria_rti             | Enum        | I, II, III, IV                                        |
| recomendacao_rti          | Enum        | Ex: Reparar, Estender prazo, Pintura                  |
| observacoes               | Text        | Observações livres                                    |
| foto                      | Imagem      | Foto opcional do equipamento                         |

---

## 🔗 Endpoints da API

| Método | Endpoint           | Descrição                                      |
|--------|--------------------|-----------------------------------------------|
| POST   | `api/v1/inspecao/`        | Cria uma nova inspeção                        |
| GET    | `api/v1/inspecao/{id}/`   | Retorna os dados de uma inspeção específica   |
| GET    | `api/v1/inspecoes/`        | Lista todas as inspeções registradas          |
| GET    | `api/v1/swagger/`         | Interface de documentação Swagger             |

---

## 🧪 Exemplo de Payload (JSON)

```json
{
  "data_inspecao": "2025-07-03",
  "tecnico_responsavel": "Fulano de Tal",
  "plataforma": "P-2",
  "modulo": "M05",
  "setor": "S03",
  "tipo_equipamento": "Permutador",
  "tag": "PM-010",
  "defeito": "Trinca",
  "causa": "Impacto",
  "categoria_rti": "III",
  "recomendacao_rti": "Reparar imediatamente",
  "observacoes": "Trinca observada no flange superior."
}
```

---

## 🌐 Integração com SAP PM (Mock)

Após cada `POST /inspecao`, os dados da inspeção são automaticamente enviados (via `requests.post`) para um sistema externo simulado no seguinte endpoint:

```
POST http://mock-sap.local/api/ordem-inspecao
```

Esta etapa é feita dentro do método `perform_create` do ViewSet.

---

## ⚙️ Como Rodar o Projeto

# 🚀 Como Rodar a Aplicação Localmente com Docker

Este guia irá te ajudar a rodar a aplicação e o banco de dados PostgreSQL localmente usando Docker e Docker Compose, de forma simples e rápida.

## Pré-requisitos

Antes de começar, você precisa ter instalado no seu computador:

- [Docker](https://docs.docker.com/get-docker/) (versão recente)  
- [Docker Compose](https://docs.docker.com/compose/install/) (geralmente já vem junto com Docker)

## Passo 1: Clonar o repositório

Abra seu terminal e clone o projeto:

```bash
git clone https://github.com/lumarodrigues/sap_inspecoes.git
cd sap_inspecoes
```

## Passo 2: Criar o arquivo `.env`

Copie o arquivo de exemplo `.env.example` (se houver) ou crie um arquivo `.env` na raiz do projeto com as variáveis de ambiente necessárias, por exemplo:

```env
DEBUG=True
DATABASE_NAME=sap_db
DATABASE_USER=sap_user
DATABASE_PASSWORD=password
DATABASE_HOST=db
DATABASE_PORT=5432
```

## Passo 3: Garantir permissões no entrypoint

Se o projeto usa um script de entrada (como `entrypoint.sh`), certifique-se que ele tenha permissão de execução:

```bash
chmod +x entrypoint.sh
```

## Passo 4: Subir os containers com Docker Compose

Agora, basta rodar o comando para construir a imagem da aplicação e subir os containers do banco e da aplicação:

```bash
docker-compose up --build
```

Esse comando vai:

- Baixar a imagem do PostgreSQL (se ainda não tiver)
- Construir a imagem da aplicação
- Subir o banco PostgreSQL com as configurações do `.env`
- Iniciar a aplicação Django no container web

## Passo 5: Acessar a aplicação

- A API estará disponível em: [http://localhost:8000/api/v1/inspecao/](http://localhost:8000/api/v1/inspecao/)
- A documentação Swagger em: [http://localhost:8000/api/v1/swagger/](http://localhost:8000/api/v1/swagger/)

## Passo 6 (Opcional): Parar a aplicação

Para parar os containers, pressione `CTRL+C` no terminal onde rodou o `docker-compose up` ou execute em outro terminal:

```bash
docker-compose down
```

---

## Passo 7: Testando a aplicação com um mock de integração

O projeto inclui um serviço (mock_sap) que simula um endpoint externo (como o SAP PM), permitindo testar o envio de dados da API sem depender de um sistema real.

Para testar, basta executar o seguinte comando curl no terminal. Ele simula uma requisição POST com os dados de uma ordem de inspeção:

```
curl -X POST http://localhost:8000/api/v1/ordem-inspecao/ \
  -H "Content-Type: application/json" \
  -d '{
    "data_inspecao": "2025-07-03",
    "tecnico_responsavel": "João Silva",
    "plataforma": "P-1",
    "modulo": "M01",
    "setor": "S01",
    "tipo_equipamento": "Vaso de Pressão",
    "tag": "VP-001",
    "defeito": "Redução de espessura",
    "causa": "Corrosão externa",
    "categoria_rti": "I",
    "recomendacao_rti": "Reparar imediatamente",
    "observacoes": "Inspeção realizada conforme padrão"
}'
```

Uma outra forma de testar a aplicação é através dos Unittests:

### Rodando os testes

Com a aplicação já rodando via Docker, execute:

```bash
docker-compose exec web python manage.py test
```

## Notas importantes

- Se a porta `5432` já estiver em uso no seu computador (por exemplo, se você já tem outro PostgreSQL rodando localmente), o container do banco pode não subir. Nesse caso, você pode alterar a porta no arquivo `docker-compose.yml`, por exemplo:

```yaml
ports:
  - "5433:5432"
```

- Caso tenha problemas de permissão com o `entrypoint.sh`, verifique a permissão do arquivo conforme o passo 3.

- O banco de dados PostgreSQL será criado automaticamente com as credenciais definidas no `.env`.

---

## 🗄️ Estrutura de Diretórios

```bash
SAP_INSPECOES/
├── inspecoes/
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── media/
├── mock_sap/
│   ├── migrations/
│   ├── __init__.py
│   ├── apps.py
│   ├── urls.py
│   └── views.py
├── sap_inspecoes/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── .env
├── .env-sample
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── manage.py
├── README.md
└── requirements.txt
```

---

## 🐞 Possíveis Melhorias Futuras

- ✅ Autenticação de usuários via JWT
- ✅ Filtros por data, técnico, tipo de equipamento
- ✅ Admin customizado para gestão das inspeções
- ✅ Exportação de relatórios em PDF ou Excel

---

## 🧑‍💻 Autor

> Desenvolvido por Luma Rodrigues dos Santos Leiros  
> Email: rdsluma@gmail.com
> GitHub: [https://github.com/lumarodrigues](https://github.com/lumarodrigues)

