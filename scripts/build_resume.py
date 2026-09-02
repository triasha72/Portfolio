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
            "Machine Learning Engineer and Georgia Tech aerospace MS graduate who builds "
            "dependable systems from data and experiments through deployment. Experience "
            "spans retrieval and ranking, scientific ML, evaluation, distributed training, "
            "and high-throughput serving.", summary,
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
        Paragraph("Turned open questions in simulation, safety, and sustainable aviation into tested Python models and repeatable analyses for faculty and sponsors.", bullet, bulletText="•"),
        Paragraph("Worked with domain experts to check assumptions, explain limitations, and leave behind workflows that other researchers could rerun.", bullet, bulletText="•"),
        Paragraph("Machine Learning Engineer | Rolls-Royce | Jul 2023 - Apr 2025", role),
        Paragraph("Built Python tools that helped engineers find unusual engine behavior, anticipate maintenance needs, and analyze sensors recorded at different rates.", bullet, bulletText="•"),
        Paragraph("Converted certification requirements into traceable model checks, then reviewed the findings with lifecycle engineers before they were used.", bullet, bulletText="•"),
        Paragraph("Data Science Intern | Rolls-Royce DataLabs | May 2021 - Jul 2021", role),
        Paragraph("Prepared aircraft-engine sensor data and compared predictive models to find recurring failure patterns for engineering review.", bullet, bulletText="•"),
        Paragraph("TECHNICAL PROJECTS", section),
        Paragraph("AIRFAANS | Geometry-aware CFD surrogates | Aug 2026", role),
        Paragraph("Tested three neural-network approaches for predicting airflow around aircraft. Across three matched runs and 200 official AirfRANS test meshes per approach, no model was best on every flow and force measure.", bullet, bulletText="•"),
        Paragraph("AeroRAG-X | Retrieval, post-training, and ML systems | Oct 2025 - Present", role),
        Paragraph("Built a technical search and RAG system over 3,233 NASA report sections. It combines keyword and semantic search, reranking, evidence checks, and citations that point back to the source.", bullet, bulletText="•"),
        Paragraph("On 888 research questions with human-selected evidence, a frozen search baseline found relevant evidence in its top 10 results 76.24% of the time. This tests retrieval, not answer quality.", bullet, bulletText="•"),
        Paragraph("IntegrityBench | Moderation evaluation and release controls | Aug 2026 - Present", role),
        Paragraph("Trained a content-moderation model on Civil Comments, chose safety thresholds without using the test set, and then evaluated it unchanged on 2,802 human-labeled ToxicChat prompts.", bullet, bulletText="•"),
        Paragraph("Unsafe content missed by the model rose from 1.84% to 59.32% on the new dataset. I blocked the release and kept the failed transfer test visible.", bullet, bulletText="•"),
        KeepTogether([
            Paragraph("NewsLens | Recommendation and real-time search | Jul 2026 - Aug 2026", role),
            Paragraph("Designed a news recommender with time-based evaluation so future clicks could not leak into training. It scored 0.366 NDCG@10, but the uncertainty interval included no improvement.", bullet, bulletText="•"),
            Paragraph("Implemented a Go, Kafka, PostgreSQL, and FastAPI pipeline for new articles. In a 500-event run, 99% were published within 44 ms and searchable within 79 ms at the 95th percentile.", bullet, bulletText="•"),
        ]),
        Paragraph("EdgeGenBench | Real-flight ML and on-device inference | Aug 2026 - Present", role),
        Paragraph("Trained a flight-anomaly model on NASA DASHlink recordings and tested it on 17,780 approaches from different aircraft. Its 0.738 macro F1 missed the release target, so it remains blocked.", bullet, bulletText="•"),
        Paragraph("Converted the model to ONNX for portable inference and stress-tested damaged sensor inputs; predictions stayed at least 99.55% consistent across the tested cases.", bullet, bulletText="•"),
        Paragraph("AeroSynth-Eval | Multimodal AI evaluation | Aug 2026 - Present", role),
        Paragraph("Tested whether generated images helped an aircraft-defect model. Overall class performance improved from 0.388 to 0.442 macro F1, but crack detection fell from 40.00% to 31.67%, so I did not call it a safety win.", bullet, bulletText="•"),
        Paragraph("Prepared 1,735 public human preference votes for training and evaluating a general image-quality judge. These votes do not validate aircraft inspection.", bullet, bulletText="•"),
        Paragraph("Surrogate Model Learning | Real-data reliability studies | Feb 2026 - Present", role),
        Paragraph("Evaluated surrogate models on public airfoil and building data, keeping related designs in the same split so test results reflected performance on new designs.", bullet, bulletText="•"),
        Paragraph("Added prediction ranges and out-of-domain warnings. Coverage improved to 87.93% and 87.07% but missed the 90% target, so confirmation on new untouched data is still needed.", bullet, bulletText="•"),
        Paragraph("Atlanta Mobility Resilience Digital Twin | Jun 2026 - Present", role),
        Paragraph("Modeled how road closures change travel time across Atlanta, using OpenStreetMap roads and 50 Census tract origins representing an estimated 216,659 residents.", bullet, bulletText="•"),
        Paragraph("Kept Census uncertainty and source records in the data pipeline. Real destinations and observed traffic calibration are the next open pieces.", bullet, bulletText="•"),
        Paragraph("Silent Failure Detection in Rocket-Motor Simulations | Georgia Tech ASDL | May 2026 - Jul 2026", role),
        Paragraph("Found why a 15,120-case rocket-motor study was silently failing: an uncapped convergence loop. A leakage-safe classifier identified failures on unseen geometries with 96.8% accuracy.", bullet, bulletText="•"),
        Paragraph("HERO | Source-aware retrieval for airline safety | Georgia Tech ASDL | May 2025 - Aug 2026", role),
        Paragraph("Developed search and evaluation methods that keep AI-generated airline-safety answers tied to technical sources analysts can inspect.", bullet, bulletText="•"),
        Paragraph("GREEN TEA and Project EAGLE | Sustainable aviation modeling | Sep 2025 - Apr 2026", role),
        Paragraph("Replaced expensive sustainability calculations with faster surrogate models and connected fuel, demand, transport, and life-cycle assumptions; the GREEN TEA model remains in sponsor use.", bullet, bulletText="•"),
        Paragraph("Equity Backtest | Walk-forward signal evaluation | Jul 2026", role),
        Paragraph("Tested a stock-momentum idea using only information available at each date and included trading costs. The apparent advantage disappeared after costs and missed the pre-set significance target.", bullet, bulletText="•"),
        Spacer(1, 5),
        Paragraph("LEADERSHIP", section),
        Paragraph("Graduate Chair | Women of Aeronautics and Astronautics, Georgia Tech | Aug 2025 - Aug 2026", body),
        Spacer(1, 3),
    ]
    doc.build(story)


if __name__ == "__main__":
    build()
