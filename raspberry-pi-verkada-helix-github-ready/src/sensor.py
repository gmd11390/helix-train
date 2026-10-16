"""Raspberry Pi IR GPIO -> Helix event demonstration."""
import argparse
import time
from datetime import datetime, timezone
from src.helix import send_event

def run(pin=17, cooldown=1.0, live=False):
    try:
        import RPi.GPIO as GPIO
    except ImportError as exc:
        raise SystemExit("RPi.GPIO is required for physical sensor mode on a Raspberry Pi") from exc
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.IN)
    print(f"Watching IR sensor on GPIO{pin}; live transmission: {live}")
    last = 0.0
    previous = False
    try:
        while True:
            active = bool(GPIO.input(pin))
            now = time.monotonic()
            if active and not previous and now - last >= cooldown:
                stamp = datetime.now(timezone.utc).isoformat()
                send_event({"event_type": "Train_Pass", "location": "IR checkpoint", "detected_at": stamp}, dry_run=not live)
                last = now
            previous = active
            time.sleep(0.1)
    finally:
        GPIO.cleanup()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--pin", type=int, default=17)
    parser.add_argument("--cooldown", type=float, default=1.0)
    parser.add_argument("--live", action="store_true", help="Send real events; requires credentials")
    args = parser.parse_args()
    run(args.pin, args.cooldown, args.live)
