async function sendMessage() {
    const userInput = document.getElementById('user-input').value;
    const chatBox = document.getElementById('chat-box');

    // Display user's message
    const userMessage = document.createElement('p');
    userMessage.textContent = 'User: ' + userInput;
    chatBox.appendChild(userMessage);

    // Show loading text
    const loadingMessage = document.createElement('p');
    loadingMessage.textContent = 'LLM: Loading...';
    loadingMessage.id = 'loading';  // Assign an ID for easy removal
    chatBox.appendChild(loadingMessage);

    // Send the message to the server via POST
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: userInput })
    });

    const data = await response.text();  // Get the complete response as text

    // Remove loading text
    document.getElementById('loading').remove();

    // Display the LLM's response
    const llmResponse = document.createElement('p');
    llmResponse.textContent = 'LLM: ' + data.replace(/^data: /, '');  // Clean the "data: " prefix
    chatBox.appendChild(llmResponse);
    chatBox.scrollTop = chatBox.scrollHeight;

    // Clear the input field
    document.getElementById('user-input').value = '';
}
