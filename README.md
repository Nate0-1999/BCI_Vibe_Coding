# BCI Silent Vibe Coding

Goal: build a local, multimodal biosignal stack that can turn non-speech body/brain signals into text and computer control.

Current hardware target:
- OpenBCI Ganglion (macOS)

Core principles:
- Maximize input bandwidth from body signals (EEG, EMG/ECG where possible).
- Keep acquisition, decoding, and action layers separate.
- Design for realtime latency and safety from day one.
- Be honest about constraints: free-form text directly from non-invasive EEG is a long-horizon goal.

## Repo Layout

- `docs/SETUP_MACOS.md`: software bring-up and first connection steps.
- `docs/ROADMAP.md`: phased plan from first stream to silent coding demo.
- `docs/ARCHITECTURE.md`: system design for multimodal decoding.
- `docs/QUESTIONS.md`: open decisions to lock before implementation.
- `src/bci`: signal acquisition, preprocessing, feature extraction, models, realtime loop.
- `src/control`: action mapping and safety gates.
- `src/ui`: live dashboard and operator tooling.
- `data`: raw/labeled/processed signals and trained models.
- `experiments`: model research scripts/notebooks.
- `tests`: unit/integration/realtime smoke tests.

## Immediate Next Steps

1. Complete `docs/SETUP_MACOS.md` bring-up.
2. Verify Ganglion stream quality and write Session 001 raw capture.
3. Build baseline decoder that maps biosignal windows to low-level latent intents.
4. Add text generation layer that converts intents to text with language-model assistance.

