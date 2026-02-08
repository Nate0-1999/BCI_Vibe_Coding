# Alpha Sprint Plan (Parallel Worktrees + Teammate Agents)

## Mission

Ship a working alpha for silent vibe coding on macOS using OpenBCI Ganglion, targeting text output without speech.

## Alpha Definition (What "working" means)

By alpha, the system can:
- Stream biosignals reliably from Ganglion.
- Run realtime decoding loop with confidence scoring.
- Produce short coding text utterances from non-speech signals via a multimodal decoder + language prior.
- Insert accepted text into a coding workflow (terminal first, VS Code second).

Alpha metrics:
- Acquisition uptime: >= 95% during 30-minute sessions.
- Realtime latency: <= 250 ms p95 from window close to decoded output.
- Phrase-level accuracy: >= 70% top-1, >= 90% top-3 on a fixed alpha phrase set.
- Safety: no unconfirmed high-risk actions.

## Locked Decisions

- Platform: macOS.
- Board: OpenBCI Ganglion.
- Product direction: maximize body/brain inputs, text output first.
- Model strategy: neural decoder with personalization, not static binary controls.

## Risk-Adjusted Scope for Alpha

To move fast without faking capability:
- Decoder output is a constrained "coding utterance vocabulary" at alpha (not fully open unconstrained text yet).
- Text generation layer expands decoder intent into natural coding text.
- Continuous calibration/personal adaptation is part of normal usage.

## Worktree + Branch Topology

Create isolated worktrees so teammate agents can run in parallel:

```bash
git fetch origin main
git worktree add .worktrees/wt-acq -b codex/acq origin/main
git worktree add .worktrees/wt-data -b codex/data-protocol origin/main
git worktree add .worktrees/wt-signal -b codex/signal-models origin/main
git worktree add .worktrees/wt-realtime -b codex/realtime-runtime origin/main
git worktree add .worktrees/wt-text -b codex/text-decoder origin/main
git worktree add .worktrees/wt-product -b codex/product-integration origin/main
```

Integration branch:
- `codex/integration-alpha` (rebased daily onto `main`, receives merged feature branches).

## Teammate Agent Plan (Parallel Tracks)

## Agent A: Acquisition + Device Reliability (`codex/acq`)

Deliverables:
- `src/bci/io/ganglion_stream.py`
- `src/bci/io/session_recorder.py`
- Session metadata schema + hardware config capture
- CLI: `python -m bci.io.session_recorder --session session_001`

Acceptance:
- 30-minute stable capture, no stream crashes.
- Raw files + metadata written to `data/raw`.

## Agent B: Labeling Protocol + Dataset Ops (`codex/data-protocol`)

Deliverables:
- `docs/LABELING_PROTOCOL.md`
- `src/bci/labels/protocol_runner.py` (timed prompts + event markers)
- `src/bci/labels/dataset_index.py` (session manifest)

Acceptance:
- Reproducible session structure.
- At least 5 clean labeled sessions for first training run.

## Agent C: Signal Processing + Baselines (`codex/signal-models`)

Deliverables:
- Filters/windowing in `src/bci/preprocess`
- Feature extraction in `src/bci/features`
- Baseline neural/classical trainers in `src/bci/models/train_baseline.py`
- Eval report generator with confusion matrix + top-k stats

Acceptance:
- Offline benchmark reproducible from raw labeled sessions.
- Baseline meets >= 60% top-1 on alpha phrase classes.

## Agent D: Realtime Runtime + Confidence/Safety (`codex/realtime-runtime`)

Deliverables:
- `src/bci/realtime/online_inference.py`
- Confidence calibration + abstain policy
- `src/control/safety/policy.py`

Acceptance:
- End-to-end loop <= 250 ms p95 on local machine.
- Low-confidence outputs held for confirm/correction.

## Agent E: Text Decoder + Language Prior (`codex/text-decoder`)

Deliverables:
- Intent-to-text composer (`src/bci/models/text_decoder.py`)
- Candidate ranking with language prior
- Correction loop API (accept/reject/next-best)

Acceptance:
- Top-3 phrase recovery >= 90% on held-out alpha set.
- Produces text snippets useful for coding prompts/edits.

## Agent F: Product Integration + Demo UX (`codex/product-integration`)

Deliverables:
- Terminal-first text injector + log view
- VS Code integration spike (optional within alpha window)
- Lightweight live dashboard in `src/ui`

Acceptance:
- Live demo path from biosignal -> decoded text -> editor insertion.
- Demo script documented and repeatable.

## Sprint Sequence (Fastest Path)

## Sprint 0 (Days 1-2): Bring-Up Gate

Parallel:
- A sets up stream + recorder.
- B finalizes protocol and phrase taxonomy.

Gate G0:
- First clean recorded + labeled session exists.

## Sprint 1 (Days 3-5): Baseline Training Gate

Parallel:
- B runs repeated sessions.
- C builds preprocess + baseline trainer.

Gate G1:
- Baseline model trains end-to-end and produces eval report.

## Sprint 2 (Days 6-8): Realtime Gate

Parallel:
- D builds realtime inference and safety policy.
- C improves model robustness from new sessions.

Gate G2:
- Realtime loop stable at latency target with confidence/abstain.

## Sprint 3 (Days 9-12): Text Pathway Gate

Parallel:
- E builds language-prior text decoder.
- F builds terminal integration + dashboard.

Gate G3:
- Silent text demo works on constrained alpha phrase set.

## Sprint 4 (Days 13-14): Hardening + Demo

Parallel:
- All agents: bugfix + reliability passes.
- F runs scripted demo rehearsal and capture.

Gate G4 (Alpha):
- End-to-end demo repeatable in one command sequence.

## Merge Cadence

- Each agent opens PR to `codex/integration-alpha` at least once daily.
- Integration owner runs smoke tests after each merge batch.
- Rebase feature branches from `main` every morning.
- Merge `codex/integration-alpha` to `main` only at gate completion.

## Required Artifacts Per Gate

- G0: raw data + metadata + labeled event log.
- G1: training script + metrics report.
- G2: latency and reliability report.
- G3: text quality report + correction-loop behavior.
- G4: recorded demo runbook and acceptance checklist.

## Immediate Next Actions (Today)

1. Confirm exact sensor inventory and channel placement plan.
2. Start Agent A + B worktrees first (they unlock everyone else).
3. Record Session 001 and Session 002 with protocol runner.
4. Kick off Agent C baseline trainer as soon as first two sessions land.

