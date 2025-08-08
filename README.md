# WhaleRush: Minimal Public Demo

This repository contains a **public, stripped-down demonstration** of the signal engine.  
It showcases the core logic for detecting "whale" cluster buys on the Ethereum network and printing formatted alerts.  
All business, monetization, advanced analytics, or paid functionality is omitted.

Check out WhaleRush on X: ```@whalerushpro```

---

## What Does This Demo Do?

- **Reads a list of "whale" wallets** (addresses, anonymized or fake for demo).
- **Loads a sample of ERC-20 transfer logs** (fake or testnet; no live chain queries).
- **Finds any token bought by 3+ different whales within a 24-hour window.**
- **Prints a formatted alert to the console** (no Telegram/webhook, no keys required).

---

## How to Run the Demo

1. **Clone this repo:**
    ```bash
    git clone https://github.com/yourusername/whalerush-demo.git
    cd whalerush-demo
    ```

2. **Install Python 3.8+** (no third-party dependencies required).

3. **Prepare your demo data:**
    - `wallets_demo.json`  
      A JSON list of lowercase wallet addresses:
      ```json
      [
        "0x1234abcd...",
        "0x5678efgh...",
        "0x9abcdeff..."
      ]
      ```
    - `sample_logs_demo.json`  
      A JSON list of ERC-20 transfer logs (see template below).

4. **Run the script:**
    ```bash
    python main.py
    ```

---

## File Descriptions

| File                 | Description                                  |
|----------------------|----------------------------------------------|
| `main.py`            | The minimal demo script (see code comments)  |
| `wallets_demo.json`  | List of whale addresses (lowercase)          |
| `sample_logs_demo.json` | Sample ERC-20 logs (see template below)   |
| `README.md`          | You’re reading it                            |

---

## Sample `sample_logs_demo.json` Format

```json
[
  {
    "address": "0x0000000000000000000000000000000000000001",
    "to": "0x1234abcd...",
    "timestamp": 1721340000,
    "symbol": "DEMO",
    "price": 0.00123
  },
  {
    "address": "0x0000000000000000000000000000000000000001",
    "to": "0x5678efgh...",
    "timestamp": 1721341000,
    "symbol": "DEMO",
    "price": 0.00123
  },
  {
    "address": "0x0000000000000000000000000000000000000001",
    "to": "0x9abcdeff...",
    "timestamp": 1721341200,
    "symbol": "DEMO",
    "price": 0.00123
  }
]
```
- address: Token contract address (string, lowercase)

- to: Whale wallet address (string, lowercase, must match a wallet in wallets_demo.json)

- timestamp: Unix epoch (integer; UTC)

- symbol (optional): Token symbol (string)

- price (optional): Token price at buy (float)

---
## FAQ
Q: Is this a working signal bot? <br>
A: No, it’s a public sample loosely based on the production version for portfolio purposes only.

Q: Where’s the business logic, real alerts, or paid features?<br>
A: If you want more, contact me.

Q: Can I use this for production?<br>
A: No. This is demo code, not meant for live deployment.

---
## License
MIT License (No commercial use without written permission).
