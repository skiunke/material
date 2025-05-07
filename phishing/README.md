# 🎣 Phishing Example

This repository demonstrates a **phishing attack** scenario for educational and security awareness purposes. It
includes:

- A **fake email template** mimicking a password-reset workflow
- A **frontend** served via Python’s HTTP server
- A **backend** managed with Docker Compose

---

> **⚠️ WARNING:**  
> This project is for **educational, ethical hacking, and security awareness training only.**  
> **Do not use for malicious purposes.**

---

## 🚀 Quick Start

### Frontend

```bash
# /phishing
python3 -m http.server
```

*Hosts the frontend at [http://localhost:8000](http://localhost:8000)*

### Backend

```bash
# /phishing
docker compose up
```

*Starts the backend to capture submissions*

---

## 📝 Usage

1. Open your browser and navigate to:  
   `http://localhost:8000/reset-password-reminder-tiktok.html`
2. When a form is submitted, the data will be stored in `phishing/data.json`.

---

**Report issues** via GitHub or contact the maintainers for ethical use guidance.  
Always obtain **explicit consent** before testing on networks or users.
