# 🔍 Port Scanner em Python

Uma ferramenta de linha de comando escrita em Python que realiza varredura de portas TCP em um endereço IP alvo, utilizando pacotes ICMP e TCP SYN via Scapy.

---

## 📋 Funcionalidades

- 📡 **Verificação de host** — envia um ping ICMP antes de escanear para confirmar se o alvo está ativo
- 🔓 **Detecção de portas abertas** — envia pacotes TCP SYN e interpreta as respostas
- 🚫 **Detecção de portas filtradas** — identifica portas sem resposta (timeout)
- ✅ **Validação de entrada** — verifica se o IP e o intervalo de portas informados são válidos

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Descrição |
|---|---|
| **Python 3** | Linguagem principal |
| **Scapy** | Criação e envio de pacotes de rede (ICMP, TCP) |

---

## ⚙️ Pré-requisitos

```bash
pip install scapy
```

> ⚠️ O script utiliza pacotes raw (TCP SYN), por isso precisa ser executado com **privilégios de root/administrador**.

---

## 🚀 Como executar

```bash
sudo python3 PortScan.py
```

O programa exibirá um menu interativo:

```
Bem-vindo ao Port Scan. O que gostaria de fazer? [E]ntrar [S]air:
```

Escolha **E** para iniciar, informe o IP do alvo e o intervalo de portas desejado.

---

## 📤 Exemplo de saída

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

## 🗂️ Estrutura do projeto

```
.
├── PortScan.py    # Código-fonte principal
└── README.md      # Documentação
```

---

## ⚠️ Avisos

- Use esta ferramenta **apenas em redes e dispositivos que você tem autorização** para testar. Varredura não autorizada é ilegal em muitos países.
- O script requer **permissão de root** para enviar pacotes raw.
- A técnica utilizada é **TCP SYN scan (half-open scan)** — a conexão não é completada, apenas a resposta SYN-ACK é verificada.

---

## 📄 Licença

Este projeto está licenciado sob a [MIT License](LICENSE).
