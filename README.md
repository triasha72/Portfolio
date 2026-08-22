# Triasha Sarkar — machine learning portfolio

This repository contains the portfolio site I use to explain my machine
learning work through problems, decisions, experiments, and results. The site
focuses on retrieval and ranking, recommendation systems, GenAI evaluation,
scientific machine learning, and model deployment.

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
AeroRAG-X, NewsLens, EdgeGenBench, AeroSynth-Eval, rocket-motor failure
detection, equity backtesting, Atlanta mobility resilience, and GREEN TEA.

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
human, production, or safety evidence.
