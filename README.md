# Raspberry Pi IR Sensor → Verkada Helix

**Physical sensor events translated into searchable video context.**  
An experimental integration developed around a **New York Security Summit demonstration**: detect an object passing an infrared (IR) sensor connected to a Raspberry Pi, then create a corresponding **Verkada Helix video-tagging event** associated with a camera.

> **Portfolio prototype, not a production integration.** The two source archives included both physical GPIO experiments and a separate, more developed software/event demo. This repository brings the ideas together into one coherent illustration. The combined code has **not** been validated end-to-end against physical hardware or a live Verkada organization.

## The idea

A video camera can show *what* happened, but a physical sensor can supply the precise moment an external action occurred. In the original **train-pass demonstration**, an IR sensor positioned beside a model track detected a passing object. A Raspberry Pi read the sensor's GPIO signal and the application was intended to send an event into Verkada Helix, linking external sensor data with relevant camera footage.

**Conceptual flow**

```text
Model train / object crosses IR beam
                │
                ▼
       IR sensor detects event
                │ GPIO17 (BCM)
                ▼
          Raspberry Pi
                │ Python, timestamp, metadata
                ▼
        Helix event payload
                │ Verkada API (configured only)
                ▼
  Verkada Command / camera video context
```

## Why this is interesting

The exercise explores a broader commercial and technical question: **How can simple third-party sensors make existing video systems more useful without replacing the cameras or infrastructure?** A train passing a checkpoint is a tangible demo; similar event correlation could be applied to equipment cycles, access points, industrial processes, or other observable physical events. Those are possible applications, **not validated deployments**.

## What's in this repository

| Path | Purpose |
| --- | --- |
| `src/sensor.py` | GPIO input monitor, edge detection, debounce/cooldown and event trigger |
| `src/helix.py` | Illustrative Helix event payload construction and optional API request |
| `examples/simulate_event.py` | Demonstrate event generation without Raspberry Pi hardware |
| `docs/original-project-notes.md` | Origin, source-archive comparison and design caveats |
| `.env.example` | Names of configuration values, with no secrets |

## Try the simulation (no credentials needed)

```bash
python -m pip install -r requirements.txt
python -m examples.simulate_event
```

The default path **prints** a representative Helix event payload. It does **not** call Verkada.

## Raspberry Pi mode (experimental)

Wire an IR sensor's digital output to **BCM GPIO17** (physical pin 11), with appropriate power and ground. **Check the sensor's voltage and the Pi's 3.3 V GPIO tolerance before connecting hardware.** The original script assumed that a HIGH input means detection; some sensors invert this behavior.

```bash
# Install RPi.GPIO on a supported Raspberry Pi setup
python -m src.sensor
```

This mode also defaults to dry run. For an explicitly configured live test, supply the environment variables in `.env.example` securely and run `python -m src.sensor --live`. The correct authentication mechanism, event schema, and permissions must be verified against current Verkada documentation; this is not a claim that the legacy API example is currently supported.

## Original development and scope

The source material came from two overlapping archives: **Raspberry Pi Project** (GPIO and sensor experiments) and **New York Security Summit (sandbox)** (Helix event generation, token handling, simulation and a separate web form). The archives also contained abandoned iterations, private identifiers, token caches, exported user records and virtual environments. Those materials are deliberately **not republished**.

This version captures the core **IR sensor → Raspberry Pi → Helix event** story, rather than pretending that the different archival branches formed one previously tested application. The separate user-submitted event form from the Summit archive is described in the project notes but not included in the primary flow.

## Limitations

- No live Verkada API, Raspberry Pi, or IR sensor validation performed for this consolidated edition.
- Actual sensor polarity, wiring, API credentials, event type, and camera association require configuration.
- Uses basic rising-edge and cooldown logic; production hardware should account for noisy signals, retries, queuing, and outages.
- No measured reliability or business outcomes are claimed.
- **Never commit API keys, session tokens, real user exports, or device identifiers.** Rotate any previously active credentials contained in the original archives.

## Context

A small hands-on integration project demonstrating how to bridge **physical devices, APIs, automation, and operational use cases**. It is included here as a portfolio example of technical curiosity and practical prototyping—not a production product.
