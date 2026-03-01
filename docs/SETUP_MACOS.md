# macOS Setup (Ganglion First Bring-Up)

This is the minimum setup to get from unopened kit to usable streamed data.

## 1) Install OpenBCI GUI

Use OpenBCI GUI first to validate hardware before writing custom code.

What to validate in GUI:
- Board connects reliably.
- Expected sample rate and channels appear.
- Signal quality changes with movement/clench/blink.
- Basic marker/event logging is available.

## 2) Install Python Environment

Recommended stack:
- Python 3.11+
- `brainflow` for board I/O
- `numpy`, `scipy`, `pandas`
- `mne` for EEG analysis
- `scikit-learn`, `pytorch` for models
- `pyqtgraph` or `streamlit` for quick dashboarding

## 3) Project Environment Bootstrap

From repo root:

```bash
./scripts/bootstrap_openbci.sh
```

This script:
- Creates `.venv`
- Installs `requirements-alpha.txt`
- Prints OpenBCI GUI installation steps for the downloaded DMG:
  - `third_party/openbci/openbcigui_v6.0.0-beta.1_macosx.dmg`

## 4) Session 001 Device Check

Record one short session (10-15 minutes):
- 2 min eyes open rest
- 2 min eyes closed rest
- 2 min jaw clench / release intervals
- 2 min blink intervals
- 2 min imagined left/right hand movement

Store as:
- `data/raw/session_001_*`
- metadata in `data/raw/session_001_meta.json`

Quick stream test command:

```bash
.venv/bin/python scripts/quickcheck_ganglion.py --board ganglion_native --mac-address "<YOUR_GANGLION_MAC>" --seconds 10
```

If you are using dongle mode instead of native BLE:

```bash
.venv/bin/python scripts/quickcheck_ganglion.py --board ganglion --serial-port "/dev/cu.usbserial-XXXX" --seconds 10
```

## 5) Hard Constraints to Track

- Non-invasive EEG has low signal-to-noise and low text bitrate.
- Reliable text generation requires personalization and repeated calibration.
- Multimodal fusion improves robustness (EEG + EMG/ECG-like channels + context).
