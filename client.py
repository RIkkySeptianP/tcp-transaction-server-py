"""
Simple TCP Transaction Client (Demo)
------------------------------------
Sends a mock transaction request to the demo server and prints the response.

Author: Rikky Septian Prasetiyo
"""

import socket

HOST = "127.0.0.1"
PORT = 9999


def send_transaction(account: str, processing_code: str, amount: str):
    message = f"0200|{account}|{processing_code}|{amount}"

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        client.sendall(message.encode("utf-8"))

        response = client.recv(1024).decode("utf-8")
        print(f"[<] Server response: {response}")


if __name__ == "__main__":
    # Example dummy transaction
    send_transaction(account="1234567890", processing_code="01", amount="150000")
