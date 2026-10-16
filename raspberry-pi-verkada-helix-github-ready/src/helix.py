"""Illustrative Helix event sender based on the original Summit demo."""
import os
import time
import requests

API_URL = "https://api.verkada.com/cameras/v1/video_tagging/event"

def send_event(attributes=None, dry_run=True):
    """Build event; only transmit when explicitly enabled and configured."""
    attributes = attributes or {"event_type": "Train_Pass", "location": "IR checkpoint"}
    payload = {
        "camera_id": os.getenv("VERKADA_CAMERA_ID", "DEMO_CAMERA_ID"),
        "event_type_uid": os.getenv("VERKADA_EVENT_TYPE_UID", "DEMO_EVENT_TYPE_UID"),
        "time_ms": int(time.time() * 1000),
        "flagged": False,
        "attributes": {str(k): str(v) for k,v in attributes.items()},
    }
    if dry_run:
        print("DRY RUN — Helix event payload:", payload)
        return payload
    token = os.environ["VERKADA_AUTH_TOKEN"]
    response = requests.post(API_URL, json=payload,
                             headers={"x-verkada-auth": token, "Content-Type": "application/json"},
                             timeout=15)
    response.raise_for_status()
    return response.json() if response.content else {"status": response.status_code}
