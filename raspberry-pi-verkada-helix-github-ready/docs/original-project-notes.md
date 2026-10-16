# Source-archive notes

## Raspberry Pi Project.zip
- `ir_sensor_trigger.py`: GPIO17 IR detection with a printed message; placeholder for Helix trigger.
- `Helix_Train/verkada_integration/sensor_trigger.py`: GPIO17 sensor + GPIO27 LED; calls `send_event(...)` in another module, though the referenced function was not consistently present across versions.
- Other scripts: event sending, token refresh, Flask/Tkinter UI experiments, simulation, user exports.

## New York Security Summit (sandbox).zip
- `helix_train/helix_event.py`: video-tagging event request construction.
- `helix_train/simulate_sensor.py`: manually triggered train-pass events.
- `helix_train/token_manager.py`: authentication/token caching implementation.
- `helix_train/usergen/webapp.py`: separate form-driven Helix events, not an IR sensor path.
- `helix_train/trainpass/sensor_handler.py`: empty placeholder in archive.

## Consolidation decisions

The new `src/sensor.py` and `src/helix.py` are **clean illustrative adaptations** of the physical GPIO and event-sender ideas, not an assertion that these precise files were previously running together. Original code with hardcoded tokens, identifiers, user exports, or local setup artifacts is intentionally omitted. Dry-run is default. Live mode is an unverified example.
