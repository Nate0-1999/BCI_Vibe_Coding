# Open Questions to Lock

## Hardware + Signal

- Confirm exact board and accessories (Ganglion + electrode types + any extra sensors).
- Decide initial channel allocation (EEG-only vs mixed EEG/EMG/ECG configuration).
- Define wearable setup for repeatable placements.

## Data + Labeling

- Minimum session length per day.
- Number of sessions per user before first model training.
- Event/intent taxonomy for first text-decoding experiments.

## Modeling

- First baseline model family (classical ML vs deep sequence model).
- Personalization strategy (per-user only vs pooled pretrain + personal fine-tune).
- Online adaptation policy and drift handling.

## Product + UX

- Editor integration target (VS Code first or terminal first).
- Confirmation UX for low-confidence text.
- Safety guardrails for automated command execution.

