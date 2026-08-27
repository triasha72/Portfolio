# Triasha Sarkar — machine learning portfolio

This repository contains the portfolio site I use to explain my machine
learning work through problems, decisions, experiments, and results. The site
focuses on scientific machine learning, retrieval and ranking, recommendation
systems, GenAI evaluation, distributed training, high-throughput LLM serving,
and model deployment.

The experience section and downloadable CV include my work as a **Machine
Learning Engineer at Rolls-Royce India from July 2023 to April 2025**.

## Why the site is structured as case studies

A project card or technology list does not explain why a model was chosen, what
failed, or how a result was measured. Each case study therefore follows the same
basic story:

1. the problem and its constraints;
2. the approach and the reason behind it;
3. the evaluation or engineering evidence;
4. the result, including negative findings; and
5. the limits of what the project establishes.

The homepage introduces the common thread across the work. Separate pages cover
AIRFAANS, AeroRAG-X, IntegrityBench, NewsLens, EdgeGenBench, AeroSynth-Eval,
rocket-motor failure detection, equity backtesting, Atlanta mobility resilience,
and GREEN TEA.

## Current evidence highlights

- **AIRFAANS** now reports a matched three-seed comparison of a pointwise MLP,
  MeshGraphNet-style GNN, and point neural operator across all 200 official
  AirfRANS interpolation test meshes per treatment. Reynolds/AoA OOD,
  scarce-data, UQ, and active-learning studies remain pending.
- **EdgeGenBench** now extends the measured ONNX/Core ML/Qualcomm QNN work with
  native C++, Android Kotlin/JNI, physical-device reference captures,
  self-describing evidence export, 16 KiB validation, and checksum-bound release
  evidence. Reference-backend Android measurements are kept separate from QNN
  profile claims.
- **AeroRAG-X** continues to distinguish implemented distributed-training and
  serving infrastructure from CUDA benchmark results that have not yet been
  executed.

## How it was built

The portfolio is a static site built with HTML and CSS. It uses no application
framework or build step, which keeps the deployed site small and makes every
page easy to inspect. Shared case-study styling lives in `case-styles.css`, and
project visuals and the downloadable CV live under `assets/`.

## Run locally

```bash
python3 -m http.server 8000
```

Open `http://localhost:8000` in a browser. Serving the files over HTTP avoids
browser restrictions that can appear when pages are opened directly from disk.

## Evidence boundary

The portfolio summarizes results from the linked repositories. The repositories,
frozen reports, tests, and source code remain the evidence of record. The site
does not turn planned work into completed work or present synthetic fixtures as
human, production, device, or safety evidence.
