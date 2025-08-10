"""
WhaleRush Demo
----------------------

This public/demo version of WhaleRush showcases the core whale signal logic:
- Reads a list of "whale" wallets from file
- Scans a sample of ERC-20 transfer logs (or fake/test logs)
- Clusters tokens bought by 3 or more different whales within a 24-hour period
- Prints formatted alerts to the console

For education, showcase, and career demonstration only.
Production, monetization, live infra, ROI, and proprietary alpha are omitted.
"""

import json
import time
from datetime import datetime, timedelta

# ===== CONFIG & DEMO FILES =====
WALLET_LIST = "wallets_demo.json"   # List of "whale" addresses (fake or real, all lowercased)
TRANSFER_LOGS = "sample_logs_demo.json"  # Sample ERC-20 logs, not live RPC

# ===== UTILITY FUNCTIONS =====

def load_json(filepath):
    """Load a JSON file as Python object, or return an empty list."""
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return []

def clean_symbol(symbol):
    """Clean up token symbol (fallback if not available)."""
    if not symbol:
        return "TOKEN"
    return symbol.replace("\u0000", "").strip().upper()

def time_ago(ts):
    """Return human-readable 'X min/hours ago' for an epoch timestamp."""
    delta = datetime.utcnow() - datetime.utcfromtimestamp(ts)
    if delta.days > 0:
        return f"{delta.days}d ago"
    elif delta.seconds > 3600:
        return f"{delta.seconds // 3600}h ago"
    elif delta.seconds > 60:
        return f"{delta.seconds // 60}m ago"
    else:
        return "just now"

# ===== MAIN ALERT LOGIC =====

def run_whalerush_demo():
    """
    Core demo logic:
    1. Loads whale list and transfer logs.
    2. Scans logs for whale ERC-20 token buys.
    3. For any token bought by 3+ unique whales in 24h, print alert to console.
    """

    # --- 1. Load Data ---
    whales = set(addr.lower() for addr in load_json(WALLET_LIST))
    logs = load_json(TRANSFER_LOGS)
    if not whales or not logs:
        print("Demo data missing! Ensure wallets_demo.json and sample_logs_demo.json are present.")
        return

    # --- 2. Scan Logs and Cluster by Token ---
    token_events = {}
    now = int(time.time())
    window = 24 * 3600  # 24h window for clustering

    for log in logs:
        # Expect log['address'] (token), log['to'] (recipient), log['timestamp'] (epoch)
        token = log.get("address", "").lower()
        to = log.get("to", "").lower()
        ts = log.get("timestamp", now)
        # Only count as "whale buy" if recipient is in whales
        if to in whales:
            token_events.setdefault(token, []).append({
                "wallet": to,
                "timestamp": ts
            })

    # --- 3. Find Clusters & Print Alerts ---
    for token, events in token_events.items():
        # Sort events by time
        events.sort(key=lambda x: x["timestamp"])
        # Look for clusters of >=3 whales within 24h
        cluster = []
        for i in range(len(events)):
            cluster = [events[i]]
            for j in range(i + 1, len(events)):
                if events[j]["timestamp"] - events[i]["timestamp"] <= window:
                    cluster.append(events[j])
                else:
                    break
            if len(set(e["wallet"] for e in cluster)) >= 3:
                break
        else:
            continue  # No valid cluster found

        # For demo, use fake or sample token metadata
        symbol = clean_symbol(log.get("symbol", "DEMO"))
        price = log.get("price", 0.00123)
        cluster_time = datetime.utcfromtimestamp(cluster[0]["timestamp"]).strftime("%H:%M UTC")
        timeago = time_ago(cluster[0]["timestamp"])

        # Format and print alert
        print(f"""
${symbol} bought by {len(set(e['wallet'] for e in cluster))} whales
First Entry: {cluster_time} ({timeago})
Price Entry: ${price:.6f}

(Vol/score/links omitted in public demo)
""")

if __name__ == "__main__":
    run_whalerush_demo()
