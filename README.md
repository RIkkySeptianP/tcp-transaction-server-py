# TCP Transaction Server (Demo)

A lightweight demo of a **TCP client-server architecture** for financial-style 
transaction messaging — inspired by the pattern used in real-world systems such as 
**ISO 8583** banking integrations, built with **dummy data only** (no proprietary 
or company-owned code).

This demonstrates the core skills behind my production work: socket programming, 
multithreaded request handling, and structured message parsing.

## Architecture

- `server.py` — TCP server that listens for incoming connections, parses a 
  pipe-delimited transaction message, and returns a JSON response. Handles 
  multiple clients concurrently using threads.
- `client.py` — TCP client that sends a mock transaction request and prints 
  the server's response.

## Message Format (demo)

Request: `MTI|ACCOUNT|PROCESSING_CODE|AMOUNT`

Example: `0200|1234567890|01|150000`

Response (JSON):
```json
{
  "mti": "0210",
  "account": "1234567890",
  "processing_code": "01",
  "amount": "150000",
  "status": "APPROVED",
  "timestamp": "2026-07-19T12:00:00"
}
```

## How to Run

1. Start the server:
   ```
   python server.py
   ```
2. In a separate terminal, run the client:
   ```
   python client.py
   ```
3. You should see the server log the incoming message and the client print 
   the JSON response.

## Tech Stack
- Python 3
- `socket` (TCP/IP)
- `threading` (concurrent connections)
- `json`

## Background

This pattern reflects the architecture behind a production ISO 8583 banking 
integration platform I built and maintained, currently processing ~1,000 
transactions/day.

## Author
Rikky Septian Prasetiyo — Senior Backend Engineer  
[LinkedIn](https://www.linkedin.com/in/rikky-septian-prasetiyo-92a176122/) · rikky.septian.p@gmail.com
