# Python SMTP Debugging Server Setup and Email Authentication Overview

## Overview

This guide explains how to set up a local SMTP debugging server using Python’s built-in `smtpd` module. It also covers
how real-world mail servers protect against email spoofing with SPF, DKIM, and DMARC.

---

## 1. Requirements

- **Python 3.10 or 3.11**
  > ⚠️ Note: The `smtpd` module is deprecated and will be removed in Python 3.12.
- **Terminal/Shell access**

---

## 2. Running the SMTP Debugging Server

Start the server with:

```python3 -m smtpd -n -c DebuggingServer localhost:1025```

- `-n`: Runs in non-daemon mode (useful for debugging).
- `-c DebuggingServer`: Uses the built-in debugging server class.
- `localhost:1025`: Listens on port 1025 (change as needed).

All emails sent to this server will be printed to the console and **not** delivered.

---

## 3. Sending Test Emails

You can use any SMTP client to send emails to `localhost:1025`. For example, using `telnet`:

```telnet localhost 1025```

Then, issue SMTP commands (example):

```HELO mycomputer
MAIL FROM:noreply@tiktok.com
RCPT TO:kiunke@realschule-deisenhofen.de
DATA
FROM: "Santa Claus" noreply@tiktok.com
TO: kiunke@realschule-deisenhofen.de
Subject: Phishing Demo

Das ist ein Test!
.
QUIT
```

The server will print:

```---------- MESSAGE FOLLOWS ----------
b'FROM: "Santa Claus" noreply@tiktok.com'
b'TO: kiunke@realschule-deisenhofen.de'
b'Subject: Phishing Demo'
b'X-Peer: 127.0.0.1'
b''
b'Das ist ein Test!'
------------ END MESSAGE ------------
```

---

## 4. How Real Mail Servers Prevent Spoofing

### SPF (Sender Policy Framework)

- **Purpose:** Specifies which mail servers are allowed to send email for your domain.
- **How:** Receiving servers check the sender's IP against the domain's SPF DNS record.
- **Effect:** Unauthorized servers are flagged or rejected.

### DKIM (DomainKeys Identified Mail)

- **Purpose:** Cryptographically signs outgoing emails to verify authenticity and integrity.
- **How:** Emails are signed with a private key; recipients use a public key in DNS to verify.
- **Effect:** Ensures the message was not altered and is from the claimed domain.

### DMARC (Domain-based Message Authentication, Reporting, and Conformance)

- **Purpose:** Tells receiving servers how to handle emails that fail SPF or DKIM checks.
- **How:** Domain owners publish a DMARC policy in DNS (e.g., reject, quarantine, or none).
- **Effect:** Helps enforce domain protection and provides reporting on spoofing attempts.

---

## 5. Summary Table

| Mechanism | What It Does                           | How It Works                               |
|-----------|----------------------------------------|--------------------------------------------|
| **SPF**   | Authorizes sending servers             | Checks sender IP against SPF DNS record    |
| **DKIM**  | Verifies message authenticity          | Signs emails; recipients verify via DNS    |
| **DMARC** | Sets handling policy for failed checks | Publishes policy in DNS; enables reporting |

---

## 6. References

- [Python smtpd documentation](https://docs.python.org/3/library/smtpd.html)
- [SPF Project](https://www.openspf.org/)
- [DKIM.org](https://dkim.org/)
- [DMARC.org](https://dmarc.org/)

---

**Note:**  
The Python `smtpd` module is deprecated. For newer Python versions, consider using [
`aiosmtpd`](https://aiosmtpd.readthedocs.io/) as a modern alternative.
