document.addEventListener("DOMContentLoaded", function () {
    document.getElementById("chatButton").addEventListener("click", function () {
      let chatWindow = window.open("", "ChatWindow", "width=800,height=600");
      chatWindow.document.write(`
        <html>
        <head>
            <title>SanaBot Chat</title>
            <style>
                body { font-family: Arial, sans-serif; text-align: center; padding: 20px; background: #E6E6FA; }
                .chat-body { height: 400px; overflow-y: auto; border: 1px solid #ddd; padding: 10px; margin-bottom: 10px; background: #FFDDC1; }
                input { width: 70%; padding: 10px; margin-right: 10px; }
                button { background: #9370DB; color: white; padding: 10px; border: none; cursor: pointer; }
                .sana-character { display: block; margin-bottom: 20px; }
            </style>
        </head>
        <body>
            <h2>💬 SanaBot</h2>
            <img src="ellehacksbot.png" alt="SanaBot" width="200">
            <div class="chat-body" id="chatBody">
                <p><strong>SanaBot:</strong> Hello! 😊 How can I assist you today?</p>
            </div>
            <input type="text" id="userInput" placeholder="Type a message..." />
            <button onclick="sendMessage()">Send</button>
  
            <script>
                function sendMessage() {
                    let input = document.getElementById("userInput").value;
                    let chatBody = document.getElementById("chatBody");
                    chatBody.innerHTML += "<p><strong>You:</strong> " + input + "</p>";
                    document.getElementById("userInput").value = "";
                    setTimeout(function () {
                        chatBody.innerHTML += "<p><strong>SanaBot:</strong> You're doing great! Keep going! ✨</p>";
                        chatBody.scrollTop = chatBody.scrollHeight;
                    }, 1000);
                }
            </script>
        </body>
        </html>
      `);
    });
  });
  

