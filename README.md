# Optimus GPT Chatbot

A simple Python Flask chatbot that learns from user inputs.  
It responds to user messages from a JSON-based database and can be trained with new responses.

## Features

- Interactive chatbot UI with HTML, CSS, and JavaScript
- JSON-based training data storage
- Dynamic learning: prompts the user for correct responses when it doesn't know
- Responsive and dark-themed design

## Project Structure

chatbot_project/
│
├─ main.py # Flask backend
├─ training_data.json # Chatbot training data # only a sample is provided
├─ requirements.txt # Python dependencies
├─ .gitignore
├─ README.md
│
├─ static/
│ ├─ styles.css # Chat UI styling
│ └─ script.js # Chat UI JavaScript
│
└─ templates/
└─ index.html # Main HTML page

## Setup

1. **Clone the repository**

git clone <repo-url>
cd chatbot_project

2. **Create a virtual environment**

python -m venv .venv

3. **Activate the virtual environment**

Windows (PowerShell):

.venv\Scripts\Activate.ps1

macOS/Linux:

source .venv/bin/activate

4. **Install dependencies**

pip install -r requirements.txt

5. **Run the chatbot**

python main.py

6. **Open the chatbot in your browser**

http://127.0.0.1:5000

Usage:
Type a message in the input box and press Enter or click Send

If the bot doesn't understand a message, it will prompt you to train it with the correct response

Training data is saved to training_data.json for future interactions

Notes
This project is intended for local use.
To access the chatbot from other devices, consider using tools like Ngrok or deploying on hosting platforms such as Render.

License
This project is open-source and available under the MIT License.

