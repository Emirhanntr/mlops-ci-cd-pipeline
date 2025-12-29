import time
import requests

BASE_URL = "http://localhost:8000"

def wait_for_health(timeout_sec: int = 20) -> bool:
    start = time.time()
    while time.time() - start < timeout_sec:
        try:
            r = requests.get(f"{BASE_URL}/health", timeout=2)
            if r.status_code == 200:
                return True
        except Exception:
            time.sleep(1)
    return False

def main():
    if not wait_for_health():
        raise SystemExit("Smoke test failed: service not healthy in time")

    r = requests.post(f"{BASE_URL}/predict", json={"user_id": "user_123"}, timeout=5)
    if r.status_code != 200:
        raise SystemExit(f"Smoke test failed: /predict returned {r.status_code}")

    data = r.json()
    if "prediction" not in data:
        raise SystemExit("Smoke test failed: prediction missing")

    print("Smoke test passed ✅")

if __name__ == "__main__":
    main()
