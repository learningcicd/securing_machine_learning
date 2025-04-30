# Securing AI/ML

## Insecure By Deisgn

### Vulnerable Flask ML API

This project is an intentionally insecure Flask app exposing a machine learning model with several common security vulnerabilities. It's designed for **educational** and **security testing** purposes only.

## 🚀 Features

- Logistic Regression model trained on synthetic data.
- Chatbot-like `/chat` endpoint simulating prompt injection.
- `/predict` endpoint vulnerable to code injection.
- `/debug` endpoint leaking environment variables.

## ⚠️ Security Vulnerabilities

| Vulnerability         | Description                                                                 |
|-----------------------|-----------------------------------------------------------------------------|
| Data Poisoning        | Labels are flipped intentionally during model training.                    |
| Unsafe Serialization  | Model is saved using `pickle` without encryption or validation.            |
| Eval Injection        | `/predict` endpoint uses `eval()` on user input, allowing code execution.  |
| Prompt Injection      | `/chat` endpoint is vulnerable to prompt injection revealing fake secrets. |
| Info Leakage          | `/debug` endpoint exposes environment variables such as `API_KEY`.         |

❗ Disclaimer
This code is intentionally vulnerable and should not be used in production. Use it strictly for educational or testing purposes in a controlled environment.

