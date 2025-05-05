# 🔐 Machine Learning Security Vulnerabilities Demonstrator (10 Examples)

This project simulates **10 real-world AI/ML security vulnerabilities** in a Python/Flask environment. It's ideal for education, testing, and awareness in secure ML development.

---

## 📚 Vulnerability Overview

| ID  | Vulnerability              | Risk Area             | Description |
|-----|----------------------------|------------------------|-------------|
| 1   | Data Poisoning             | Model Training         | Malicious data injected during training to alter model behavior |
| 2   | Unsafe Serialization       | Model Storage          | Using insecure formats like pickle exposes to RCE |
| 3   | Eval Injection             | Inference API          | Dynamic evaluation of user input allows code execution |
| 4   | Prompt Injection           | LLM Prompting          | User-controlled input alters prompt instructions |
| 5   | Information Leakage        | Debug Interfaces       | Debug routes leak sensitive environment variables |
| 6   | Model Stealing             | Model Exposure         | Repeated queries allow attackers to recreate models |
| 7   | Adversarial Example        | Model Robustness       | Subtle input modifications trigger misclassification |
| 8   | Insecure Feature Store     | Data Supply Chain      | Feature data sourced from untrusted locations |
| 9   | Supply Chain Risk          | Dependencies/Models    | Using tampered models/libraries can introduce backdoors |
| 10  | Exposed Model Endpoint     | Deployment             | Model APIs open to the public without authentication |

---

## 🚀 Quick Start

### Requirements

```bash
pip install flask scikit-learn numpy
```

### Run the CLI Menu

```bash
python3 main.py
```

### Options:
```
1. Data Poisoning
2. Unsafe Serialization
3. Eval Injection
4. Prompt Injection
5. Information Leakage
6. Model Stealing
7. Adversarial Example
8. Insecure Feature Store
9. Supply Chain Risk
10. Exposed Model Endpoint
```

---

## 🧪 Detailed Vulnerability Descriptions

### 1. Data Poisoning
**Description:** Labels or inputs are intentionally flipped or corrupted to degrade performance.
**Impact:** Model misbehaves, misclassifies, or embeds backdoors.
**Fix:** Validate data sources, perform anomaly detection, use robust training.

### 2. Unsafe Serialization
**Description:** Saving models with `pickle` allows code execution if file is tampered.
**Impact:** Remote Code Execution (RCE) if loading compromised pickle files.
**Fix:** Use `joblib`, JSON, or signed formats for model serialization.

### 3. Eval Injection
**Description:** `eval()` used on user input in APIs.
**Impact:** Total server compromise through code execution.
**Fix:** Never use `eval()` on input. Use strict parsing or hard-coded logic.

### 4. Prompt Injection
**Description:** LLM prompt includes user input without sanitization.
**Impact:** Model follows user commands like revealing secrets or breaking instructions.
**Fix:** Use prompt templates and isolate instructions from user input.

### 5. Information Leakage
**Description:** `/debug` route exposes environment variables.
**Impact:** Secret keys, tokens, and system metadata leakage.
**Fix:** Disable debug routes in production. Mask sensitive vars.

### 6. Model Stealing
**Description:** Querying the model repeatedly allows its logic to be reverse engineered.
**Impact:** Intellectual property theft.
**Fix:** Rate limit APIs, add noise to output, watermark predictions.

### 7. Adversarial Example
**Description:** Small, imperceptible changes to inputs mislead the model.
**Impact:** Security-sensitive failures (e.g., object detection).
**Fix:** Use adversarial training, certified defenses, input sanitization.

### 8. Insecure Feature Store
**Description:** Pulling features from unauthenticated or tampered sources.
**Impact:** Poisoned features degrade model accuracy.
**Fix:** Secure connections, verify data source integrity.

### 9. Supply Chain Risk
**Description:** Malicious models or dependencies are injected into the project.
**Impact:** Full system compromise via fake packages or backdoored models.
**Fix:** Verify hashes, use SBOMs, and secure registries.

### 10. Exposed Model Endpoint
**Description:** No auth required to hit prediction APIs.
**Impact:** Unauthorized use, DoS, scraping, abuse.
**Fix:** Use API gateways, authentication, and IP whitelisting.

---

## 🛡️ How to Secure Your ML Pipeline

| Risk Area        | Best Practices |
|------------------|----------------|
| Training         | Monitor data quality, use robust training methods |
| Inference APIs   | Input validation, avoid dynamic code, rate limiting |
| Deployment       | Use containers, restrict network exposure |
| DevOps           | Use CI/CD, lock dependencies, generate SBOM |
| Prompting (LLMs) | Structure prompts, validate input/output rigorously |

---

## 📎 Usage with Docker

```bash
docker build -t ml-vuln-demo .
docker run -it --rm -p 5001:5001 -p 5002:5002 -p 5003:5003 ml-vuln-demo
```

To test an individual Flask vulnerability:
```bash
docker run -it ml-vuln-demo python main.py --eval-server
```

---

## 🧩 References

- [OWASP Top 10 for LLM Apps](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [Adversarial ML Threat Matrix (Microsoft)](https://github.com/Azure/adversarial-ml-threat-matrix)
- [Awesome ML Security](https://github.com/trailofbits/awesome-ml-security)
- [LLM Guard](https://github.com/ProtectAI/llm-guard)

---

## 📜 License

MIT — Use for education, training, and secure development advocacy.
