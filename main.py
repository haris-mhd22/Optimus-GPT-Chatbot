import json
import logging
from flask import Flask, render_template, request, jsonify, session
import random
from uuid import uuid4

app = Flask(__name__, static_folder='static')
app.secret_key = "super-secret-key"  # required for session tracking

EXIT_COMMAND = 'exit'
TRAINING_FILE = "training_data.json"

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# In-memory state for pending training (for each user session)
pending_training = {}

def load_json(file_path):
    try:
        with open(file_path) as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError) as e:
        logging.error(f"Error loading {file_path}: {e}")
        return []

def save_json(file_path, data):
    try:
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)
    except IOError as e:
        logging.error(f"Error writing to {file_path}: {e}")

def load_training_data():
    return load_json(TRAINING_FILE)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_input = request.json.get('user_input', '').strip()
    session_id = session.get('id')

    if not session_id:
        session['id'] = str(uuid4())
        session_id = session['id']

    training_data = load_training_data()

    # --- Handle ongoing training conversation ---
    if session_id in pending_training:
        state = pending_training[session_id]
        stage = state['stage']

        if stage == 'confirm':
            if user_input.lower() in ['yes', 'y']:
                pending_training[session_id]['stage'] = 'awaiting_response'
                return jsonify({
                    "bot_response": f"Okay! What should I reply when someone says '{state['question']}'?"
                })
            else:
                del pending_training[session_id]
                return jsonify({"bot_response": "No problem! Let’s keep chatting 😊"})

        elif stage == 'awaiting_response':
            new_entry = {"input": state['question'], "response": user_input}
            training_data.append(new_entry)
            save_json(TRAINING_FILE, training_data)
            del pending_training[session_id]
            return jsonify({"bot_response": "Thanks! I’ve learned a new response 🤖"})

    # --- Normal chatbot response ---
    responses = [d["response"] for d in training_data if d["input"].lower() in user_input.lower()]
    if responses:
        return jsonify({"bot_response": random.choice(responses)})

    # --- Unknown input: ask if user wants to teach ---
    pending_training[session_id] = {"stage": "confirm", "question": user_input}
    return jsonify({
        "bot_response": f"I don’t know how to respond to '{user_input}'. Would you like to teach me? (yes/no)"
    })

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
