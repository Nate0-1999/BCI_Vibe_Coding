# Architecture: Multimodal Silent Text System

## High-Level Pipeline

1. Acquisition
- Ingest synchronized signals from available sensors.
- Primary start: Ganglion channels (configured for EEG, EMG/ECG-like capture as available).

2. Preprocessing
- Bandpass/notch filtering.
- Artifact handling (blink/motion/noise flags).
- Windowing with overlap for realtime inference.

3. Representation
- Handcrafted and/or learned embeddings:
  - Bandpower and spectral features
  - Temporal CNN/RNN/Transformer embeddings

4. Decoder
- Neural model predicts latent intent/state probabilities.
- Optional CTC/sequence models for time-aligned decoding.

5. Text Generator
- Combine decoder posteriors with text prior.
- Produce text hypotheses with confidence.
- Use correction loop for rapid refinement.

6. Action Layer
- Convert accepted text to editor/system actions.
- Safety policies block high-risk actions unless explicit confirmation.

## Why This Structure

- Keeps hardware complexity isolated from modeling.
- Allows gradual upgrades from baseline classifiers to sequence decoders.
- Supports fusion of new sensors without rewriting downstream systems.

## Core Technical Risk

The highest risk is decoding high-entropy free text from low-SNR non-invasive signals. Mitigation:
- Start with robust latent-state decoding.
- Use strong language priors and personalization.
- Focus early demos on short, high-value coding utterances.

