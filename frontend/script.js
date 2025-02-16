async function sendMessage() {
    let input = document.getElementById("userInput").value;
    let chatBody = document.getElementById("chatBody");

    // Display the user's message
    chatBody.innerHTML += "<p><strong>You:</strong> " + input + "</p>";
    document.getElementById("userInput").value = "";

    try {
        // Send the user's message to the backend API
        const response = await fetch('http://127.0.0.1:5000/chat', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ message: input })
        });

        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();

        // Display the response from the API
        chatBody.innerHTML += "<p><strong>SanaBot:</strong> " + data.bot_response + "</p>";
    } catch (error) {
        // Display the error message
        chatBody.innerHTML += "<p><strong>SanaBot:</strong> Error: " + error.message + "</p>";
    }

    // Scroll to the bottom of the chat
    chatBody.scrollTop = chatBody.scrollHeight;
}