from scapy.all import *
import os
from time import sleep

def scan(ip, port):
    if port > 65535 or port < 1:
        print("Intervalo de portas invalido!")
        return
    if "." not in ip or len(ip) < 7 or len(ip) > 15:
        print("Seu endereco IP esta incorreto")
        return
    resposta = sr1(IP(dst=ip)/ICMP(), timeout=2, verbose=False)
    if resposta:
        print(f"Resposta recebida de : {resposta.src}")
        print("Escaneando endereco IP...")
        sleep(2)
    else:
        print("Sem resposta (Timeout)")
    for i in range(1, port, 1): 
        pacote = sr1(IP(dst=ip)/TCP(dport=i, flags="S"), timeout=2, verbose=0)
        if pacote is None:
            print(f"Porta {i}: Filtrada (sem resposta)")
        elif pacote.haslayer(TCP):
            if pacote.getlayer(TCP).flags == 0x12:
                print(f"Porta {i}: Aberta")
    print("Escaneamento finalizado!")
           
while True:
    resp = str(input("Bem-vindo ao Port Scan. O que gostaria de fazer? [E]ntrar [S]air: "))
    if resp in "Ee":
        endereco = str(input("Digite o endereco IP do alvo: "))
        portas = int(input("Escolha o intervalo de portas escaneadas(padrao 1024): "))
        scan(endereco, portas)
    elif resp in "Ss":
        break
    else:
        print("Opcao invalida.")
os.system('exit')
