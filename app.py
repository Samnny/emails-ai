import os
import google.generativeai as genai
import json
import PyPDF2
import magic
from flask import Flask, request, jsonify, render_template
from dotenv import load_dotenv

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Configurar a API do Gemini
try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    print(f"Erro ao configurar a API do Gemini: {e}")
    # Em um app real, você poderia ter um tratamento mais robusto aqui
    model = None

# Configurar o aplicativo Flask
app = Flask(__name__)

# Dica de Mestre: Criar um prompt bem estruturado é a chave para obter boas respostas da IA.
# Pedimos a resposta em formato JSON para facilitar o processamento no backend.
PROMPT_TEMPLATE = """
Analise o seguinte texto de um e-mail e retorne uma análise em formato JSON.
O JSON deve ter duas chaves: "classificacao" e "sugestao_resposta".

1.  **classificacao**: Classifique o e-mail como "Produtivo" ou "Improdutivo".
    - "Produtivo": E-mails que exigem uma ação, resposta específica, contêm solicitações, dúvidas ou atualizações importantes.
    - "Improdutivo": E-mails que não precisam de ação imediata, como felicitações, agradecimentos genéricos ou spam.

2.  **sugestao_resposta**: Com base na classificação, sugira uma resposta adequada.
    - Para e-mails "Produtivos", crie uma resposta cordial e profissional que indique que a solicitação está sendo analisada.
    - Para e-mails "Improdutivos", sugira uma resposta curta e amigável, como um simples agradecimento.

Texto do E-mail:
---
{email_text}
---

Retorne APENAS o objeto JSON, sem nenhum texto ou formatação adicional.
"""

def extract_text_from_pdf(file_stream):
    """Extrai texto de um arquivo PDF."""
    try:
        pdf_reader = PyPDF2.PdfReader(file_stream)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Erro ao ler PDF: {e}")
        return None

@app.route('/')
def index():
    """Renderiza a página inicial."""
    return render_template('index.html')

@app.route('/processar', methods=['POST'])
def processar_email():
    """Processa o texto do e-mail ou arquivo enviado."""
    if not model:
        return jsonify({"error": "A API do Gemini não foi configurada corretamente."}), 500

    email_text = ""
    # Verifica se um arquivo foi enviado
    if 'email_file' in request.files and request.files['email_file'].filename != '':
        file = request.files['email_file']
        
        # Identifica o tipo do arquivo de forma segura
        mime_type = magic.from_buffer(file.read(2048), mime=True)
        file.seek(0) # Retorna o cursor para o início do arquivo

        if mime_type == 'text/plain':
            email_text = file.read().decode('utf-8')
        elif mime_type == 'application/pdf':
            email_text = extract_text_from_pdf(file)
            if email_text is None:
                return jsonify({"error": "Não foi possível extrair texto do arquivo PDF."}), 400
        else:
            return jsonify({"error": "Formato de arquivo não suportado. Use .txt ou .pdf."}), 400
    else:
        # Se não houver arquivo, usa o texto da área de texto
        email_text = request.form.get('email_text', '')

    if not email_text.strip():
        return jsonify({"error": "Nenhum texto de e-mail fornecido."}), 400

    try:
        # Formata o prompt com o texto do e-mail
        prompt = PROMPT_TEMPLATE.format(email_text=email_text)
        
        # Chama a API do Gemini
        response = model.generate_content(prompt)
        
        # Limpa e converte a resposta para JSON
        # A API pode retornar o JSON dentro de um bloco de código markdown (```json ... ```)
        cleaned_response = response.text.strip().replace("```json", "").replace("```", "")
        result_json = json.loads(cleaned_response)

        return jsonify(result_json)

    except Exception as e:
        print(f"Erro durante o processamento da IA: {e}")
        return jsonify({"error": f"Ocorreu um erro ao processar a solicitação com a IA. Detalhes: {e}"}), 500

if __name__ == '__main__':
    app.run(debug=True)