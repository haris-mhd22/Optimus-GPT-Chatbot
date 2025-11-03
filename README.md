🤖 Optimus GPT Chatbot

A simple Python Flask chatbot that learns from user inputs.
It responds to messages from a JSON-based database and can be trained dynamically with new responses.

🌟 Features:
🗨️ Interactive chatbot UI with HTML, CSS, and JavaScript
📁 JSON-based training data storage
🧠 Dynamic learning — prompts the user for correct responses when it doesn't know
🌙 Responsive dark-themed design

⚙️ Setup
1️⃣ Clone the repository
git clone <your-repo-link>
cd chatbot_project

2️⃣ Create a virtual environment
python -m venv .venv

3️⃣ Activate the virtual environment

Windows (PowerShell):
.venv\Scripts\Activate.ps1

macOS/Linux:
source .venv/bin/activate

4️⃣ Install dependencies
pip install -r requirements.txt

5️⃣ Run the chatbot
python main.py

6️⃣ Open in browser
Go to:
👉 http://127.0.0.1:5000

💬 Usage
Type a message in the chat input box and press Enter or click Send.
If the bot doesn’t understand a message, it will ask you to train it with the correct response.
All learned data is saved in training_data.json for future use.

📝 Notes
This project is intended for local use.
To make it accessible from other devices, consider using tools like Ngrok or deploy it on platforms such as Render or Railway.

📜 License
This project is open-source and available under the MIT License.
