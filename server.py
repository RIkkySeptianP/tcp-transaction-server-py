"""
Simple TCP Transaction Server (Demo)
------------------------------------
Demonstrates the core architecture pattern used in real-world financial
messaging systems (e.g. ISO 8583-style socket communication), using a
lightweight custom message format and dummy data only.

Author: Rikky Septian Prasetiyo
"""

import socket
import threading
import json
from datetime import datetime, timezone

HOST = "127.0.0.1"
PORT = 9999


def handle_message(raw_message: str) -> dict:
    """Parse an incoming pipe-delimited message and build a response.

    Message format (demo):  MTI|FIELD2|FIELD3|FIELD4
      MTI    -> Message Type Indicator (e.g. "0200" = transaction request)
      FIELD2 -> Account number
      FIELD3 -> Processing code
      FIELD4 -> Amount
    """
    parts = raw_message.strip().split("|")
    if len(parts) < 4:
        return {"mti": "0210", "status": "ERROR", "reason": "Malformed message"}

    mti, account, proc_code, amount = parts[0], parts[1], parts[2], parts[3]

    response = {
        "mti": "0210",  # response MTI
        "account": account,
        "processing_code": proc_code,
        "amount": amount,
        "status": "APPROVED",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    return response


def handle_client(conn: socket.socket, addr):
    print(f"[+] Connection from {addr}")
    with conn:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            raw = data.decode("utf-8")
            print(f"[>] Received: {raw}")

            response = handle_message(raw)
            payload = json.dumps(response)
            conn.sendall(payload.encode("utf-8"))
            print(f"[<] Sent: {payload}")
    print(f"[-] Connection closed: {addr}")


def start_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Server listening on {HOST}:{PORT}")

        while True:
            conn, addr = server.accept()
            thread = threading.Thread(target=handle_client, args=(conn, addr), daemon=True)
            thread.start()


if __name__ == "__main__":
    start_server()
