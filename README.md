# Triasha Sarkar — machine learning portfolio

This repository contains the portfolio site I use to explain my machine
learning work through problems, decisions, experiments, and results. The site
focuses on scientific machine learning, retrieval and ranking, recommendation
systems, GenAI evaluation, distributed training, high-throughput LLM serving,
and model deployment.

The experience section and downloadable CV include my work as a **Machine
Learning Engineer at Rolls-Royce from July 2023 to April 2025**. I entered
Georgia Tech's Aerospace Engineering PhD program, transitioned to the MS, and
completed the degree in August 2026.

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
  AirfRANS interpolation test meshes per treatment. No architecture wins every
  field and force metric; Reynolds/AoA OOD and uncertainty runs remain pending.
- **IntegrityBench** evaluates a validation-thresholded candidate on 97,320
  public Civil Comments, then tests the frozen model on 2,802 human-annotated
  ToxicChat prompts. False acceptance rises to 59.32% under that shift, so the
  release remains blocked.
- **EdgeGenBench** now leads with its public NASA DASHlink flight-anomaly track.
  The generated aircraft-design surrogate remains useful deployment evidence,
  but it is no longer presented as measured-aircraft model accuracy.
- **AeroSynth-Eval** includes a ten-seed transfer study on public AGDD images
  and a separate set of 1,735 GenAI-Bench human preference votes. The votes
  support evaluator development, not aircraft-inspection claims.
- **AeroRAG-X** adds a QASPER retrieval baseline over 888 questions with human
  evidence spans. Evidence recall@10 is 76.24%; the result covers retrieval on
  NLP papers, not NASA answer generation.
- **Atlanta Mobility Resilience** now materializes 50 Census tract origins from
  2024 ACS five-year estimates, representing an estimated 216,659 residents.
  Essential destinations and observed-trip calibration remain open.

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
