"""Test event creation without hardware, API credentials, or network calls."""
from src.helix import send_event

if __name__ == "__main__":
    send_event({"event_type": "Train_Pass", "location": "Demo track", "source": "simulated_IR"})
