# 🔍 Port Scanner in Python

A command-line tool written in Python that performs TCP port scanning on a target IP address, using ICMP and TCP SYN packets via Scapy.

---

## 📋 Features

- 📡 **Host check** — sends an ICMP ping before scanning to confirm whether the target is online
- 🔓 **Open port detection** — sends TCP SYN packets and interprets the responses
- 🚫 **Filtered port detection** — identifies ports with no response (timeout)
- ✅ **Input validation** — checks whether the provided IP address and port range are valid

---

## 🛠️ Technologies Used

| Technology | Description |
|---|---|
| **Python 3** | Main programming language |
| **Scapy** | Network packet crafting and sending (ICMP, TCP) |

---

## ⚙️ Prerequisites

```bash
pip install scapy
```

> ⚠️ This script uses raw packets (TCP SYN), so it must be run with **root/administrator privileges**.

---

## 🚀 How to Run

```bash
sudo python3 PortScan.py
```

The program will display an interactive menu:

```
Bem-vindo ao Port Scan. O que gostaria de fazer? [E]ntrar [S]air:
```

Choose **E** to start, then enter the target IP and the desired port range.

---

## 📤 Sample Output

```
Bem-vindo ao Port Scan. O que gostaria de fazer? [E]ntrar [S]air: E
Digite o endereco IP do alvo: 192.168.1.1
Escolha o intervalo de portas escaneadas(padrao 1024): 1024

Resposta recebida de: 192.168.1.1
Escaneando endereco IP...
Porta 22: Aberta
Porta 80: Aberta
Porta 443: Aberta
Porta 8080: Filtrada (sem resposta)
Escaneamento finalizado!
```

---

## 🗂️ Project Structure

```
.
├── PortScan.py    # Main source file
└── README.md      # Documentation
```

---

## ⚠️ Disclaimer

- Use this tool **only on networks and devices you are authorized to test**. Unauthorized port scanning is illegal in many countries.
- The script requires **root privileges** to send raw packets.
- The technique used is **TCP SYN scan (half-open scan)** — the connection is never completed, only the SYN-ACK response is checked.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
