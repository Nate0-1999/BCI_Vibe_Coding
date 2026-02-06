# Roadmap: From Signals to Silent Coding

## Phase 0: Device Bring-Up (Week 1)

Exit criteria:
- Stable Ganglion connection on macOS.
- Stream visible in GUI and basic Python ingestion script.
- One clean raw recording session saved with metadata.

Deliverables:
- I/O adapter skeleton in `src/bci/io`.
- Session capture script (to be added).
- Reproducible session naming convention.

## Phase 1: Labeling + Baselines (Week 1-2)

Exit criteria:
- Repeatable labeling protocol.
- Baseline models for detectable states (rest, clench, blink, imagined movement).
- Offline metrics and confusion matrices.

Deliverables:
- Windowing + filters in `src/bci/preprocess`.
- Feature extraction in `src/bci/features`.
- Baseline training/eval code in `src/bci/models`.

## Phase 2: Realtime Decoder (Week 2-4)

Exit criteria:
- Realtime inference loop <250 ms end-to-end lag.
- Confidence scores + uncertainty handling.
- Safe, constrained control outputs.

Deliverables:
- Online loop in `src/bci/realtime`.
- Action and safety policy in `src/control`.
- Live confidence dashboard in `src/ui`.

## Phase 3: Text Pathway (Week 4+)

Target:
- Move from coarse intents to text generation.

Approach:
- Decode latent intent/state from biosignals.
- Use language prior + beam search to propose text.
- User-specific adaptation continuously updates decoder.

Reality check:
- Open-ended text purely from EEG is not near-term reliable.
- Practical route: multimodal signals + language model + aggressive personalization.

## Phase 4: Silent Vibe Coding Demo

Definition of done:
- User can produce short coding instructions or edits without speaking.
- System provides confidence + correction loop.
- Demo includes error recovery and operator safety fallback.

