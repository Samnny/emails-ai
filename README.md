# Classificador Inteligente de E-mails 🚀

![Python](https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.0+-black?style=for-the-badge&logo=flask)
![Google Gemini](https://img.shields.io/badge/Google_Gemini-AI-purple?style=for-the-badge&logo=google)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript)

A aplicação web utiliza a API do Google Gemini para classificar e-mails como "Produtivo" ou "Improdutivo" e sugerir respostas automáticas, otimizando o fluxo de trabalho e a gestão de comunicações.

---

## ✨ Visão Geral

O objetivo deste projeto é simular uma solução real para empresas que lidam com um grande volume de e-mails. A aplicação permite que o usuário cole o texto de um e-mail ou faça o upload de um arquivo (.txt ou .pdf) para receber uma análise instantânea, composta por:

* **Classificação Automática:** Identifica se o e-mail requer uma ação (Produtivo) ou não (Improdutivo).
* **Sugestão de Resposta:** Gera um rascunho de resposta apropriado para a categoria do e-mail.

## 🔗 Demonstração Online

**Acesse a aplicação em funcionamento no seguinte link:**

[**https://emails-ai.onrender.com**](https://emails-ai.onrender.com/)  

## 🛠️ Tecnologias Utilizadas

### Backend
* **Python 3.9+**: Linguagem principal de desenvolvimento.
* **Flask**: Micro-framework web para criar a API e servir a aplicação.
* **Google Gemini API**: Modelo de IA para processamento de linguagem natural (classificação e geração de texto).
* **Gunicorn**: Servidor WSGI para o ambiente de produção.

### Frontend
* **HTML5**: Estruturação da página web.
* **CSS3**: Estilização e design responsivo.
* **JavaScript (Vanilla)**: Manipulação do DOM e comunicação assíncrona com o backend (`Fetch API`).

### Deploy
* **Render**: Plataforma de nuvem para hospedagem da aplicação.
* **Git & GitHub**: Para versionamento de código e integração com a plataforma de deploy.

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para configurar e rodar a aplicação em seu ambiente local.

### Pré-requisitos
* [Git](https://git-scm.com/)
* [Python 3.9](https://www.python.org/) ou superior

### Passos para Instalação

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/Samnny/emails-ai.git
    cd emails-ai
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Linux/macOS
    python3 -m venv venv
    source venv/bin/activate

    # Para Windows
    python -m venv venv
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente:**
    * Crie um arquivo chamado `.env` na raiz do projeto.
    * Adicione sua chave da API do Google Gemini a este arquivo:
      ```
      GEMINI_API_KEY="SUA_CHAVE_API_AQUI"
      ```

5.  **Inicie o servidor de desenvolvimento:**
    ```bash
    flask run
    ```

6.  **Acesse a aplicação** no seu navegador em `http://127.0.0.1:5000`.

---

## 📁 Estrutura do Projeto
A estrutura de pastas do projeto foi organizada da seguinte forma para manter o código limpo e modular:

```
├── app.py              # Arquivo principal do Flask (backend)
├── requirements.txt    # Lista de dependências Python
├── Procfile            # Instruções de inicialização para o Render
├── .env                # Arquivo para chaves de API (local, não versionado)
├── .gitignore          # Arquivos e pastas a serem ignorados pelo Git
├── templates/
│   └── index.html      # Estrutura HTML da página principal
└── static/
    ├── style.css       # Folha de estilo
    └── script.js       # Lógica do frontend
```

---

## 👨‍💻 Autor

Desenvolvido por **Samay Pessoa**.

* [![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samay-pessoa/)
