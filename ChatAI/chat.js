function sendMessage() {
    const userInput = document.getElementById("user-input").value;
    const chatBox = document.getElementById("chat-box");

    // Display user input in the chat box
    const userInputDiv = document.createElement("div");
    userInputDiv.className = "user-input";
    userInputDiv.textContent = "You: " + userInput;
    chatBox.appendChild(userInputDiv);

    // Send user input to the Flask backend and get a response
    fetch("/get_response", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        },
        body: "user_input=" + encodeURIComponent(userInput)
    })
    .then(response => response.text())
    .then(botResponse => {
        const botResponseDiv = document.createElement("div");
        botResponseDiv.className = "bot-response";
        botResponseDiv.textContent = "Bot: " + botResponse;
        chatBox.appendChild(botResponseDiv);
        chatBox.scrollTop = chatBox.scrollHeight; // Auto-scroll to the bottom of the chat
    });

    // Clear the input field
    document.getElementById("user-input").value = "";
}