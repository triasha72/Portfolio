"""Build the portfolio resume from the same claims used on the site."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
from reportlab.platypus import PageBreak, Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "Triasha_Sarkar_CV.pdf"
FONT_DIR = Path("/System/Library/Fonts/Supplemental")


def _fonts() -> tuple[str, str]:
    regular = FONT_DIR / "Arial.ttf"
    bold = FONT_DIR / "Arial Bold.ttf"
    if regular.exists() and bold.exists():
        pdfmetrics.registerFont(TTFont("Resume", regular))
        pdfmetrics.registerFont(TTFont("Resume-Bold", bold))
        return "Resume", "Resume-Bold"
    return "Helvetica", "Helvetica-Bold"


def build() -> None:
    regular, bold = _fonts()
    navy = colors.HexColor("#0B2830")
    teal = colors.HexColor("#147D75")
    muted = colors.HexColor("#44565B")
    styles = getSampleStyleSheet()
    name = ParagraphStyle(
        "Name", parent=styles["Normal"], fontName=bold, fontSize=22,
        leading=24, alignment=TA_CENTER, textColor=navy, spaceAfter=3,
    )
    contact = ParagraphStyle(
        "Contact", parent=styles["Normal"], fontName=regular, fontSize=8.2,
        leading=10.2, alignment=TA_CENTER, textColor=muted, spaceAfter=7,
    )
    summary = ParagraphStyle(
        "Summary", parent=styles["Normal"], fontName=regular, fontSize=8.7,
        leading=11.2, textColor=navy, spaceAfter=6,
    )
    section = ParagraphStyle(
        "Section", parent=styles["Heading2"], fontName=bold, fontSize=9.2,
        leading=11, textColor=teal, spaceBefore=5, spaceAfter=3,
        borderWidth=0, borderPadding=0,
    )
    role = ParagraphStyle(
        "Role", parent=styles["Normal"], fontName=bold, fontSize=8.5,
        leading=10.2, textColor=navy, spaceBefore=2, spaceAfter=1,
    )
    body = ParagraphStyle(
        "Body", parent=styles["Normal"], fontName=regular, fontSize=8.2,
        leading=10.4, textColor=navy, spaceAfter=2,
    )
    bullet = ParagraphStyle(
        "Bullet", parent=body, leftIndent=9, firstLineIndent=-7,
        bulletIndent=0, spaceAfter=1.5,
    )

    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=letter, rightMargin=0.55 * inch,
        leftMargin=0.55 * inch, topMargin=0.38 * inch, bottomMargin=0.38 * inch,
        title="Triasha Sarkar Resume", author="Triasha Sarkar",
    )
    story = [
        Paragraph("TRIASHA SARKAR", name),
        Paragraph(
            "Atlanta, GA | +1 (404) 948-8761 | tsarkar34@gatech.edu<br/>"
            "linkedin.com/in/triasha-sarkar | github.com/triasha72 | "
            "triasha72.github.io/Portfolio", contact,
        ),
        Paragraph(
            "Machine Learning Engineer and Georgia Tech aerospace MS graduate who builds "
            "dependable systems from data and experiments through deployment. Experience "
            "spans retrieval and ranking, scientific ML, evaluation, distributed training, "
            "and high-throughput serving.", summary,
        ),
        Paragraph("EDUCATION", section),
        Paragraph("MS, Aerospace Engineering | Georgia Institute of Technology, Atlanta, GA | Aug 2026", role),
        Paragraph("Entered PhD program; transitioned to MS and completed the degree in Aug 2026", body),
        Paragraph("MSc, Aerospace Vehicle Design | Cranfield University, United Kingdom | Feb 2023", role),
        Paragraph("First Class Honours | Thesis on geometry optimization under FAA constraints", body),
        Paragraph("B.Tech, Aerospace Engineering | SRM Institute of Science and Technology, India | Jun 2021", role),
        Paragraph("First Class Honours", body),
        Paragraph("TECHNICAL SKILLS", section),
        Paragraph("<b>ML and GenAI:</b> PyTorch, scikit-learn, Transformers, PEFT/LoRA, RAG, BM25, dense retrieval, reranking, recommender systems, uncertainty estimation", body),
        Paragraph("<b>Systems:</b> Python, Go, SQL, Kafka, FastAPI, Docker, Kubernetes, GitHub Actions, PostgreSQL/pgvector, Prometheus, OpenTelemetry, ONNX, Core ML, Qualcomm QNN", body),
        Paragraph("<b>Scientific computing:</b> NumPy, SciPy, pandas, NetworkX, OSMnx, statistical inference, design of experiments, surrogate modeling", body),
        Paragraph("PROFESSIONAL EXPERIENCE", section),
        Paragraph("Graduate Research Assistant under Prof. Dimitri Mavris | Georgia Tech ASDL | May 2025 - Aug 2026", role),
        Paragraph("Took simulation, safety, and sustainability questions from data review and model design through tested analysis, with reproducible evidence for faculty and sponsors.", bullet, bulletText="•"),
        Paragraph("Checked assumptions with domain experts, documented limitations, and delivered models and workflows that others could rerun and use.", bullet, bulletText="•"),
        Paragraph("Machine Learning Engineer | Rolls-Royce | Jul 2023 - Apr 2025", role),
        Paragraph("Built Python workflows for diagnostics, anomaly detection, predictive maintenance, and mixed-frequency time series from multivariate engine data.", bullet, bulletText="•"),
        Paragraph("Turned certification requirements into traceable analyses and model checks, reviewing each result with lifecycle engineers before use.", bullet, bulletText="•"),
        Paragraph("Data Science Intern | Rolls-Royce DataLabs | May - Jul 2021", role),
        Paragraph("Cleaned aircraft-engine sensor data, designed features, and compared predictive and anomaly-detection models to identify recurring failure patterns.", bullet, bulletText="•"),
        Paragraph("SELECTED TECHNICAL PROJECTS", section),
        Paragraph("AeroRAG-X | Retrieval, post-training, and ML systems | 2025 - Present", role),
        Paragraph("Built hybrid retrieval, reranking, pgvector search, evidence gating, and citation controls over 3,233 source-preserving NASA NTRS chunks.", bullet, bulletText="•"),
        Paragraph("On 888 QASPER questions with human evidence spans, a frozen TF-IDF baseline reached 76.24% evidence recall@10. This is retrieval evidence on NLP papers, not NASA answer generation.", bullet, bulletText="•"),
        Paragraph("IntegrityBench | Moderation evaluation and release controls | Aug 2026 - Present", role),
        Paragraph("Trained a Civil Comments candidate with validation-only safety thresholds, then tested it without retraining on 2,802 human-annotated ToxicChat prompts.", bullet, bulletText="•"),
        Paragraph("False acceptance rose from 1.84% on Civil Comments to 59.32% on ToxicChat, so the release remains blocked rather than presented as a general moderation model.", bullet, bulletText="•"),
        Paragraph("NewsLens | Recommendation and real-time search | Jul - Aug 2026", role),
        Paragraph("Reached NDCG@10 of 0.366 with leakage-safe MIND evaluation; the one-time holdout interval included zero.", bullet, bulletText="•"),
        Paragraph("Built a Go, Kafka, PostgreSQL, and FastAPI article path; a 500-event local run measured 44 ms publish p99, 79 ms freshness p95, and 5.7 s partition recovery.", bullet, bulletText="•"),
        PageBreak(),
        Paragraph("TRIASHA SARKAR | SELECTED PROJECTS", section),
        Paragraph("EdgeGenBench | Real-flight ML and on-device inference | Aug 2026 - Present", role),
        Paragraph("A NASA DASHlink anomaly model reached 0.7380 macro F1 on 17,780 aircraft-disjoint approaches and remained blocked by release gates.", bullet, bulletText="•"),
        Paragraph("ONNX prediction consistency stayed above 99.55% under tested sensor corruptions; generated aircraft-design data is labeled separately as deployment evidence.", bullet, bulletText="•"),
        Paragraph("AeroSynth-Eval | Multimodal AI evaluation | Aug 2026 - Present", role),
        Paragraph("On public AGDD aircraft images, mixed training raised mean macro F1 from 0.3881 to 0.4419 but reduced crack recall from 0.4000 to 0.3167.", bullet, bulletText="•"),
        Paragraph("Materialized 1,735 GenAI-Bench human preference votes into prompt-grouped train, validation, and held-out partitions for general image-evaluator development, not aircraft-inspection validation.", bullet, bulletText="•"),
        Paragraph("Surrogate Model Learning | Real-data reliability studies | Aug 2026 - Present", role),
        Paragraph("Built grouped-split UCI airfoil and building-load experiments with seed sensitivity, extrapolation checks, and conformal intervals.", bullet, bulletText="•"),
        Paragraph("A normalized conformal diagnostic reached 87.93% and 87.07% coverage against a 90% target; it remains a retrospective finding pending untouched-data confirmation.", bullet, bulletText="•"),
        Paragraph("Atlanta Mobility Resilience Digital Twin | 2026 - Present", role),
        Paragraph("Built an OSMnx and NetworkX road-disruption simulator, then added 50 Census tract origins from 2024 ACS estimates representing an estimated 216,659 residents.", bullet, bulletText="•"),
        Paragraph("Retained ACS margins of error and source hashes. Essential destinations and observed traffic calibration remain open.", bullet, bulletText="•"),
        Paragraph("Silent Failure Detection in Rocket-Motor Simulations | Georgia Tech ASDL | May - Jul 2026", role),
        Paragraph("Audited 15,120 simulations, built a leakage-safe classifier with 96.8% unseen-geometry accuracy, and traced silent failures to an uncapped convergence loop.", bullet, bulletText="•"),
        Paragraph("HERO | Source-aware retrieval for airline safety | Georgia Tech ASDL | 2025 - 2026", role),
        Paragraph("Worked on retrieval and evaluation methods that keep generated safety answers tied to technical sources analysts can review.", bullet, bulletText="•"),
        Paragraph("GREEN TEA and Project EAGLE | Sustainable aviation modeling | Sep 2025 - Apr 2026", role),
        Paragraph("Built surrogate, uncertainty, demand, and life-cycle models for alternative-fuel and transport studies; the GREEN TEA model remains in sponsor use.", bullet, bulletText="•"),
        Paragraph("Equity Backtest | Walk-forward signal evaluation | Jul 2026", role),
        Paragraph("Built an expanding-window backtest with transaction costs and retained every specification tested; the apparent momentum edge disappeared after costs and missed the preregistered significance threshold.", bullet, bulletText="•"),
        Paragraph("LEADERSHIP", section),
        Paragraph("Graduate Chair | Women of Aeronautics and Astronautics, Georgia Tech | 2025 - 2026", body),
        Spacer(1, 3),
    ]
    doc.build(story)


if __name__ == "__main__":
    build()
