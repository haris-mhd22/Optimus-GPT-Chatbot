function sendMessage() {
    const inputField = document.getElementById("user-input");
    const userInput = inputField.value.trim();

    if (userInput === "") return;

    // Display user message
    displayMessage("user", userInput);

    // Send to Flask backend
    fetch("/send_message", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ user_input: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        // Display bot message
        displayMessage("bot", data.bot_response);
    })
    .catch(error => {
        console.error("Error sending message:", error);
        displayMessage("bot", "⚠️ There was an error sending your message.");
    });

    // Clear the input field
    inputField.value = "";
}

// Send message when pressing Enter
document.getElementById("user-input").addEventListener("keyup", function(event) {
    if (event.key === "Enter") {
        sendMessage();
    }
});

// Send message on button click
document.getElementById("send-button").addEventListener("click", sendMessage);

function displayMessage(sender, message) {
    const chatBox = document.getElementById("chat-box");
    const messageDiv = document.createElement("div");
    messageDiv.className = sender + "-message";

    const speakerName = sender === "user" ? "You" : "Bot";
    messageDiv.textContent = speakerName + ": " + message;

    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}
