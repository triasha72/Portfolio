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
- **IntegrityBench** keeps its three-way candidate blocked after a 59.32%
  ToxicChat false-acceptance result. A separate BeaverTails-only training run
  cuts held-out false acceptance to 18.79%, but raises false rejection to
  16.43% and cannot escalate uncertain cases.
- **EdgeGenBench** now leads with its public NASA DASHlink flight-anomaly track.
  The generated aircraft-design surrogate remains useful deployment evidence,
  but it is no longer presented as measured-aircraft model accuracy.
- **AeroSynth-Eval** includes a ten-seed AGDD transfer study and 1,735
  GenAI-Bench preference votes. It now has a verified acquisition path for
  DLR's MIT-licensed 6,000+ image aircraft-dent dataset; no DLR model result is
  claimed until its archive and splits are audited.
- **AeroRAG-X** evaluates retrieval on QASPER and SciFact human annotations,
  audits 20,283 public TREC RAG relevance judgments and 2,840 citation-support
  judgments, and rejects 200/200 deliberately wrong NASA source IDs. The
  50-case aerospace author audit is still pending.
- **Atlanta Mobility Resilience** now materializes 50 Census tract origins from
  2024 ACS five-year estimates, representing an estimated 216,659 residents.
  Its research config also uses 101 mapped hospitals, clinics, fire stations,
  and shelters. ACS uncertainty propagation is implemented; observed travel
  calibration remains open.
- **Surrogate Model Learning** confirms a frozen uncertainty method on 1,030
  public UCI concrete measurements. Test R² is 0.9023, and normalized 90%
  intervals cover 95.83% of the held-out mixture groups.

## How it was built

The portfolio is a static site built with HTML and CSS. It uses no application
framework or build step, which keeps the deployed site small and makes every
page easy to inspect. Shared case-study styling lives in `case-styles.css`, and
project visuals and the downloadable CV live under `assets/`.

The update path from repository evidence to case study and resume is shown in
[the site architecture](docs/architecture.md).

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
