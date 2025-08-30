document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('email-form');
    const submitBtn = document.getElementById('submit-btn');
    const loadingDiv = document.getElementById('loading');
    const resultContainer = document.getElementById('result-container');
    const errorContainer = document.getElementById('error-container');

    const resultClassificacao = document.getElementById('result-classificacao');
    const resultSugestao = document.getElementById('result-sugestao');
    const errorMessage = document.getElementById('error-message');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();

        // 1. Resetar a interface
        submitBtn.disabled = true;
        submitBtn.textContent = 'Analisando...';
        loadingDiv.classList.remove('hidden');
        resultContainer.classList.add('hidden');
        errorContainer.classList.add('hidden');

        // 2. Coletar dados do formulário
        const formData = new FormData(form);

        try {
            // 3. Enviar para o backend
            const response = await fetch('/processar', {
                method: 'POST',
                body: formData,
            });

            const data = await response.json();

            if (!response.ok) {
                // Se a resposta HTTP não for OK (ex: 400, 500)
                throw new Error(data.error || 'Ocorreu um erro desconhecido.');
            }
            
            // 4. Exibir resultados
            const classificacao = data.classificacao || 'N/A';
            resultClassificacao.textContent = classificacao;
            resultClassificacao.className = ''; // Limpa classes anteriores
            resultClassificacao.classList.add(classificacao.toLowerCase() === 'produtivo' ? 'produtivo' : 'improdutivo');
            
            resultSugestao.textContent = data.sugestao_resposta || 'Nenhuma sugestão disponível.';
            
            resultContainer.classList.remove('hidden');

        } catch (error) {
            // 5. Exibir erros
            errorMessage.textContent = error.message;
            errorContainer.classList.remove('hidden');
            console.error('Erro:', error);
        } finally {
            // 6. Restaurar o botão
            submitBtn.disabled = false;
            submitBtn.textContent = 'Analisar E-mail';
            loadingDiv.classList.add('hidden');
        }
    });
});