async function sendMessage() {
    const userInput = document.getElementById('user-input').value;

    if (!userInput) {
        alert('Пожалуйста, введите ваш запрос.');
        return;
    }

    const responseDiv = document.getElementById('response');
    responseDiv.innerHTML = 'Загрузка...';  // Сообщение о загрузке

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ message: userInput })
        });

        const data = await response.json();
        responseDiv.innerHTML = data.reply || 'Нет ответа от API.';
    } catch (error) {
        responseDiv.innerHTML = 'Ошибка: ' + error.message;
    }
}
