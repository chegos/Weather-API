# 🌦️ Weather API com Cache (Flask + Redis)

Uma API REST desenvolvida em Python que fornece dados climáticos em tempo real utilizando uma API externa, com implementação de cache em memória usando Redis para melhorar performance e reduzir chamadas externas.

---

## 🚀 Tecnologias utilizadas

* **Python**
* **Flask**
* **Requests**
* **Redis**
* **Python-dotenv**

---

## 📌 Funcionalidades

* 🔎 Consulta de clima por cidade
* 🌐 Integração com API externa (Visual Crossing)
* ⚡ Cache com Redis (expiração automática)
* 🔐 Uso de variáveis de ambiente (.env)
* 🧠 Tratamento de dados da API
* 📊 Retorno de JSON limpo e organizado

---

## 🧠 Como funciona

1. O usuário faz uma requisição para `/weather?city=NomeDaCidade`
2. A API verifica se os dados estão no Redis:

   * ✅ Se estiver → retorna do cache
   * ❌ Se não → busca na API externa
3. Os dados são armazenados no Redis por 12 horas
4. A resposta é retornada ao usuário

---

## 📁 Estrutura do projeto

```
weather-api/
│
├── venv/
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## ⚙️ Instalação e execução

### 1. Clone o repositório

```bash
git clone https://github.com/seu-usuario/weather-api.git
cd weather-api
```

---

### 2. Crie e ative o ambiente virtual

```bash
python -m venv venv
.\venv\Scripts\activate
```

---

### 3. Instale as dependências

```bash
python -m pip install -r requirements.txt
```

---

### 4. Configure as variáveis de ambiente

Crie um arquivo `.env`:

```
WEATHER_API_KEY=sua_chave_aqui
```

---

### 5. Inicie o Redis

Se estiver usando Docker:

```bash
docker run -d -p 6379:6379 redis
```

---

### 6. Execute o projeto

```bash
python app.py
```

---

## 📡 Endpoint

### 🔍 Buscar clima

```
GET /weather?city=NomeDaCidade
```

### 📥 Exemplo:

```
http://127.0.0.1:5000/weather?city=Sao%20Paulo
```

---

## 📊 Exemplo de resposta

```json
{
  "source": "cache",
  "data": {
    "city": "Sao Paulo",
    "temperature": 23.5,
    "condition": "Partially cloudy",
    "humidity": 68.3,
    "wind_speed": 9.6
  }
}
```

---

## ⚡ Cache com Redis

* Dados armazenados por **12 horas**
* Reduz chamadas à API externa
* Melhora performance da aplicação

---

## 🛡️ Boas práticas aplicadas

* Uso de variáveis de ambiente
* Separação de responsabilidades
* Tratamento de erros
* Estrutura simples e escalável

---

## 📈 Melhorias futuras

* 📍 Suporte a múltiplas cidades
* 🌡️ Conversão automática para Celsius
* 🔒 Rate limiting
* 📊 Logs e monitoramento
* ☁️ Deploy em nuvem

---

## 👨‍💻 Autor

Desenvolvido por **Luis Rodrigues**
https://roadmap.sh/projects/weather-api-wrapper-service

---

## ⭐ Contribuição

Sinta-se à vontade para abrir issues ou pull requests!

---

## 📄 Licença

Este projeto está sob a licença MIT.
