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
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

Install dependencies once we finalize `requirements.txt` / `pyproject.toml`.

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

## 5) Hard Constraints to Track

- Non-invasive EEG has low signal-to-noise and low text bitrate.
- Reliable text generation requires personalization and repeated calibration.
- Multimodal fusion improves robustness (EEG + EMG/ECG-like channels + context).

