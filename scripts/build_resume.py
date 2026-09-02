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
from reportlab.platypus import KeepTogether, Paragraph, SimpleDocTemplate, Spacer

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
        leading=10.8, alignment=TA_CENTER, textColor=muted, spaceAfter=9,
    )
    summary = ParagraphStyle(
        "Summary", parent=styles["Normal"], fontName=regular, fontSize=9,
        leading=12.4, textColor=navy, spaceAfter=8,
    )
    section = ParagraphStyle(
        "Section", parent=styles["Heading2"], fontName=bold, fontSize=9.2,
        leading=11.5, textColor=teal, spaceBefore=7, spaceAfter=4,
        borderWidth=0, borderPadding=0,
    )
    role = ParagraphStyle(
        "Role", parent=styles["Normal"], fontName=bold, fontSize=8.7,
        leading=11.2, textColor=navy, spaceBefore=3.2, spaceAfter=2,
        keepWithNext=True,
    )
    body = ParagraphStyle(
        "Body", parent=styles["Normal"], fontName=regular, fontSize=8.5,
        leading=11.8, textColor=navy, spaceAfter=3,
    )
    bullet = ParagraphStyle(
        "Bullet", parent=body, leftIndent=9, firstLineIndent=-7,
        bulletIndent=0, spaceAfter=2.3,
    )

    doc = SimpleDocTemplate(
        str(OUTPUT), pagesize=letter, rightMargin=0.62 * inch,
        leftMargin=0.62 * inch, topMargin=0.42 * inch, bottomMargin=0.42 * inch,
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
            "Machine Learning Engineer with an MS in Aerospace Engineering from Georgia "
            "Tech. Builds and evaluates retrieval, scientific ML, and production systems, "
            "with a focus on measurable results, failure analysis, and deployment.", summary,
        ),
        Paragraph("EDUCATION", section),
        Paragraph("MS, Aerospace Engineering | Georgia Institute of Technology, Atlanta, GA | Aug 2026", role),
        Paragraph("CGPA: 3.7/4.0 | Entered PhD program; transitioned to MS and completed the degree in Aug 2026", body),
        Paragraph("MSc, Aerospace Vehicle Design | Cranfield University, United Kingdom | Feb 2023", role),
        Paragraph("CGPA: 3.6/4.0 | First Class Honours | Thesis on geometry optimization under FAA constraints", body),
        Paragraph("B.Tech, Aerospace Engineering | SRM Institute of Science and Technology, India | Jun 2021", role),
        Paragraph("CGPA: 3.8/4.0 | First Class Honours", body),
        Paragraph("TECHNICAL SKILLS", section),
        Paragraph("<b>ML and GenAI:</b> PyTorch, scikit-learn, Transformers, PEFT/LoRA, RAG, BM25, dense retrieval, reranking, recommender systems, uncertainty estimation", body),
        Paragraph("<b>Systems:</b> Python, Go, SQL, Kafka, FastAPI, Docker, Kubernetes, GitHub Actions, PostgreSQL/pgvector, Prometheus, OpenTelemetry, ONNX, Core ML, Qualcomm QNN", body),
        Paragraph("<b>Scientific computing:</b> NumPy, SciPy, pandas, NetworkX, OSMnx, statistical inference, design of experiments, surrogate modeling", body),
        Paragraph("PROFESSIONAL EXPERIENCE", section),
        Paragraph("Graduate Research Assistant under Prof. Dimitri Mavris | Georgia Tech ASDL | May 2025 - Aug 2026", role),
        Paragraph("Built and tested Python models for projects in simulation, airline safety, and sustainable aviation; shared reproducible analyses with faculty and sponsors.", bullet, bulletText="•"),
        Paragraph("Reviewed assumptions and limits with aerospace experts and documented each workflow so other researchers could rerun it.", bullet, bulletText="•"),
        Paragraph("Machine Learning Engineer | Rolls-Royce | Jul 2023 - Apr 2025", role),
        Paragraph("Developed Python pipelines to flag unusual engine behavior, support maintenance planning, and combine sensor streams sampled at different rates.", bullet, bulletText="•"),
        Paragraph("Mapped certification requirements to data and model checks, then reviewed results with lifecycle engineers before use.", bullet, bulletText="•"),
        Paragraph("Data Science Intern | Rolls-Royce DataLabs | May 2021 - Jul 2021", role),
        Paragraph("Cleaned aircraft-engine sensor data, built features, and compared prediction and anomaly models; summarized recurring failure patterns for engineers.", bullet, bulletText="•"),
        Paragraph("TECHNICAL PROJECTS", section),
        Paragraph("AIRFAANS | Geometry-aware CFD surrogates | Aug 2026", role),
        Paragraph("Benchmarked three neural-network architectures for airflow prediction across three matched runs and 200 official AirfRANS test meshes per model. No architecture led every flow and force metric.", bullet, bulletText="•"),
        Paragraph("AeroRAG-X | Retrieval, post-training, and ML systems | Oct 2025 - Present", role),
        Paragraph("Built a search and RAG system over 3,233 NASA report sections using keyword search, embeddings, reranking, evidence checks, and source-linked citations.", bullet, bulletText="•"),
        Paragraph("Evaluated a frozen search baseline on 888 questions with human-selected evidence; relevant evidence appeared in the top 10 results 76.24% of the time. Answer quality was not part of this test.", bullet, bulletText="•"),
        Paragraph("IntegrityBench | Moderation evaluation and release controls | Aug 2026 - Present", role),
        Paragraph("Trained a content-moderation model on Civil Comments, selected thresholds on validation data, and evaluated the frozen model on 2,802 human-labeled ToxicChat prompts.", bullet, bulletText="•"),
        Paragraph("False acceptance rose from 1.84% to 59.32% on ToxicChat. The release stayed blocked, and the failed transfer result remains reported.", bullet, bulletText="•"),
        KeepTogether([
            Paragraph("NewsLens | Recommendation and real-time search | Jul 2026 - Aug 2026", role),
            Paragraph("Used chronological splits to keep future clicks out of training. The recommender scored 0.366 NDCG@10, but the uncertainty interval still included no improvement.", bullet, bulletText="•"),
            Paragraph("Built a Go, Kafka, PostgreSQL, and FastAPI ingestion path for new articles. In a 500-event run, publish p99 was 44 ms and search freshness p95 was 79 ms.", bullet, bulletText="•"),
        ]),
        Paragraph("EdgeGenBench | Real-flight ML and on-device inference | Aug 2026 - Present", role),
        Paragraph("Trained a flight-anomaly model on NASA DASHlink recordings and tested it on 17,780 approaches from held-out aircraft. Its 0.738 macro F1 missed the release target.", bullet, bulletText="•"),
        Paragraph("Exported the model to ONNX and tested corrupted sensor inputs; prediction agreement stayed above 99.55% across the tested cases.", bullet, bulletText="•"),
        Paragraph("AeroSynth-Eval | Multimodal AI evaluation | Aug 2026 - Present", role),
        Paragraph("Tested generated-image augmentation for aircraft-defect classification. Macro F1 improved from 0.388 to 0.442, but crack recall fell from 40.00% to 31.67%, so the change was rejected.", bullet, bulletText="•"),
        Paragraph("Prepared 1,735 public human preference votes for a general image-quality evaluator; the labels do not validate aircraft inspection.", bullet, bulletText="•"),
        Paragraph("Surrogate Model Learning | Real-data reliability studies | Feb 2026 - Present", role),
        Paragraph("Evaluated surrogate models on public airfoil and building datasets using grouped splits, so related designs could not appear in both training and test data.", bullet, bulletText="•"),
        Paragraph("Added prediction intervals and out-of-domain checks. Coverage reached 87.93% and 87.07%, below the 90% target; validation on new data is still pending.", bullet, bulletText="•"),
        Paragraph("Atlanta Mobility Resilience Digital Twin | Jun 2026 - Present", role),
        Paragraph("Built an Atlanta road-closure simulator using OpenStreetMap and 50 Census tract origins representing an estimated 216,659 residents.", bullet, bulletText="•"),
        Paragraph("Stored Census margins of error and source hashes with each run. Real destinations and traffic calibration are still pending.", bullet, bulletText="•"),
        Paragraph("Silent Failure Detection in Rocket-Motor Simulations | Georgia Tech ASDL | May 2026 - Jul 2026", role),
        Paragraph("Traced silent failures in a 15,120-case rocket-motor study to an uncapped convergence loop; a leakage-safe classifier reached 96.8% accuracy on unseen geometries.", bullet, bulletText="•"),
        Paragraph("HERO | Source-aware retrieval for airline safety | Georgia Tech ASDL | May 2025 - Aug 2026", role),
        Paragraph("Developed retrieval and evaluation methods that link AI-generated airline-safety answers to technical sources analysts can inspect.", bullet, bulletText="•"),
        Paragraph("GREEN TEA and Project EAGLE | Sustainable aviation modeling | Sep 2025 - Apr 2026", role),
        Paragraph("Built surrogate models to speed up sustainability calculations and connected fuel, demand, transport, and life-cycle inputs; GREEN TEA remains in sponsor use.", bullet, bulletText="•"),
        Paragraph("Equity Backtest | Walk-forward signal evaluation | Jul 2026", role),
        Paragraph("Backtested a stock-momentum signal using only data available at each date and included trading costs. The signal disappeared after costs and missed the pre-set significance threshold.", bullet, bulletText="•"),
        Spacer(1, 5),
        Paragraph("LEADERSHIP", section),
        Paragraph("Graduate Chair | Women of Aeronautics and Astronautics, Georgia Tech | Aug 2025 - Aug 2026", body),
        Spacer(1, 3),
    ]
    doc.build(story)


if __name__ == "__main__":
    build()
