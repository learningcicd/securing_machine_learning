
# vulnerable_model.py

from flask import Flask, request
from sklearn.datasets import make_classification
from sklearn.linear_model import LogisticRegression
import pickle
import os

app = Flask(__name__)

# Simulate training on poisoned data (bad labels)
X, y = make_classification(n_samples=100, n_features=4, n_classes=2, random_state=42)
y[:10] = 1 - y[:10]  # Simulate data poisoning
model = LogisticRegression().fit(X, y)

# Save model without protection (model theft)
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.json.get('features')
    if not user_input:
        return {"error": "Missing features"}, 400

    # Adversarial input simulation: no validation, unsafe eval
    try:
        features = eval(user_input)  # DO NOT USE eval() in production
        pred = model.predict([features])[0]
        return {"prediction": int(pred)}
    except Exception as e:
        return {"error": str(e)}, 500
        
@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.json.get('prompt')
    if not prompt:
        return {"error": "Missing prompt"}, 400

    # Simulated LLM behavior
    system_instruction = "You are a safe AI model."
    full_prompt = system_instruction + "\nUser: " + prompt

    response = fake_llm(full_prompt)
    return {"response": response}

def fake_llm(prompt):
    if "Ignore previous" in prompt or "secret" in prompt:
        return "Access granted. Secret key: admin123!"
    return "This is a generic response."
@app.route('/debug', methods=['GET'])
def debug():
    # Leaks sensitive env info
    return {"api_key": os.getenv("API_KEY", "default_key")}


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

