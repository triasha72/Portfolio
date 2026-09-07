"""Build a concise one-page ML Engineer resume for the portfolio."""

from __future__ import annotations

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "assets" / "Triasha_Sarkar_One_Page_ML_Resume.pdf"
FONT_DIR = Path("/System/Library/Fonts/Supplemental")


def fonts() -> tuple[str, str]:
    regular = FONT_DIR / "Arial.ttf"
    bold = FONT_DIR / "Arial Bold.ttf"
    if regular.exists() and bold.exists():
        pdfmetrics.registerFont(TTFont("OnePage", regular))
        pdfmetrics.registerFont(TTFont("OnePage-Bold", bold))
        return "OnePage", "OnePage-Bold"
    return "Helvetica", "Helvetica-Bold"


def build() -> None:
    regular, bold = fonts()
    navy, teal, muted = colors.HexColor("#0B2830"), colors.HexColor("#147D75"), colors.HexColor("#44565B")
    styles = getSampleStyleSheet()
    name = ParagraphStyle("Name", parent=styles["Normal"], fontName=bold, fontSize=21, leading=23, alignment=TA_CENTER, textColor=navy, spaceAfter=2)
    contact = ParagraphStyle("Contact", parent=styles["Normal"], fontName=regular, fontSize=8.1, leading=9.8, alignment=TA_CENTER, textColor=muted, spaceAfter=7)
    summary = ParagraphStyle("Summary", parent=styles["Normal"], fontName=regular, fontSize=9, leading=11.4, textColor=navy, spaceAfter=6)
    section = ParagraphStyle("Section", parent=styles["Heading2"], fontName=bold, fontSize=9.4, leading=11.4, textColor=teal, spaceBefore=6, spaceAfter=3)
    role = ParagraphStyle("Role", parent=styles["Normal"], fontName=bold, fontSize=8.7, leading=10.7, textColor=navy, spaceBefore=2.4, spaceAfter=1.4)
    body = ParagraphStyle("Body", parent=styles["Normal"], fontName=regular, fontSize=8.5, leading=10.7, textColor=navy, spaceAfter=1.8)
    bullet = ParagraphStyle("Bullet", parent=body, leftIndent=8, firstLineIndent=-6, bulletIndent=0, spaceAfter=1.5)
    doc = SimpleDocTemplate(str(OUTPUT), pagesize=letter, leftMargin=.58*inch, rightMargin=.58*inch, topMargin=.34*inch, bottomMargin=.33*inch, title="Triasha Sarkar One-Page ML Resume", author="Triasha Sarkar")
    story = [
        Paragraph("TRIASHA SARKAR", name),
        Paragraph("Atlanta, GA | +1 (404) 948-8761 | tsarkar34@gatech.edu | linkedin.com/in/triasha-sarkar | github.com/triasha72 | triasha72.github.io/Portfolio", contact),
        Paragraph("Machine Learning Engineer with experience in scientific ML, model evaluation, retrieval, time-series data, and ML systems. Aerospace background in simulation, uncertainty, and engineering problems.", summary),
        Paragraph("EXPERIENCE", section),
        Paragraph("Graduate Research Assistant | Georgia Tech ASDL | May 2025 – Aug 2026", role),
        Paragraph("Built ML workflows for simulation reliability, airline-safety retrieval, and sustainable aviation; documented assumptions and results for faculty and sponsors.", bullet, bulletText="•"),
        Paragraph("Machine Learning Engineer | Rolls-Royce | Jul 2023 – Apr 2025", role),
        Paragraph("Built Python workflows for engine diagnostics, anomaly detection, predictive maintenance, and mixed-frequency sensor data; reviewed findings with lifecycle engineers.", bullet, bulletText="•"),
        Paragraph("Data Science Intern | Rolls-Royce DataLabs | May 2021 – Jul 2021", role),
        Paragraph("Cleaned aircraft-engine sensor data, built features, and compared prediction and anomaly-detection models for engineering review.", bullet, bulletText="•"),
        Paragraph("PROJECTS", section),
        Paragraph("AIRFAANS | CFD surrogates | Jan 2026 – Apr 2026", role),
        Paragraph("Compared an MLP, MeshGraphNet-style GNN, and point neural operator on 200 AirfRANS meshes per model across three seeds; kept OOD and uncertainty work explicitly pending.", bullet, bulletText="•"),
        Paragraph("EdgeGenBench | Flight-anomaly ML and ONNX", role),
        Paragraph("Evaluated NASA DASHlink data on 17,780 held-out aircraft approaches; 0.738 macro F1 missed the release target, while ONNX consistency stayed above 99.55% under tested sensor corruptions.", bullet, bulletText="•"),
        Paragraph("NewsLens | Recommendation and real-time search", role),
        Paragraph("Built a leakage-aware news recommender and Go, Kafka, PostgreSQL, and FastAPI ingestion path; NDCG@10 0.3664 and sampled index-freshness p95 79 ms.", bullet, bulletText="•"),
        Paragraph("Surrogate Model Learning | Reliability under design shift", role),
        Paragraph("Used grouped splits and uncertainty checks on public engineering data; airfoil GP reached R² 0.8145, while nominal 90% intervals lost coverage under design shift.", bullet, bulletText="•"),
        Paragraph("Other ML projects | IntegrityBench | AeroRAG-X | AeroSynth-Eval | Equity Backtest", role),
        Paragraph("Built evaluation and release controls for changing moderation policies; source-grounded NASA technical-report retrieval; synthetic inspection-image evaluation; and a walk-forward equity-signal backtest.", bullet, bulletText="•"),
        Paragraph("Georgia Tech ASDL projects | Rocket-Motor Failure Detection | GREEN TEA and Project EAGLE | HERO", role),
        Paragraph("Worked on silent-failure detection in simulation, sustainable-aviation modeling, and source-aware retrieval for airline safety.", bullet, bulletText="•"),
        Paragraph("EARLIER AEROSPACE PROJECTS", section),
        Paragraph("Supersonic Business Jets and Noise Mitigation (Cranfield) | Bird-Strike Impact Analysis (SRM) | Ornithopter Aerodynamics (SRM)", role),
        Paragraph("Studied geometry and noise trade-offs for supersonic aircraft; used ANSYS to compare nose-cone materials for bird-strike impact; used CFD to examine ornithopter wing area and load factor.", bullet, bulletText="•"),
        Paragraph("EDUCATION & SKILLS", section),
        Paragraph("MS Aerospace Engineering, Georgia Tech (2026) | MSc Aerospace Vehicle Design, Cranfield (2023) | B.Tech Aerospace Engineering, SRM (2021)", body),
        Paragraph("Python, PyTorch, PyTorch Geometric, scikit-learn, GNNs, surrogate modeling, uncertainty quantification, SQL, FastAPI, Docker, Kubernetes, Kafka, PostgreSQL, ONNX", body),
        Paragraph("LEADERSHIP", section),
        Paragraph("Graduate Chair, Women of Aeronautics and Astronautics, Georgia Tech | Aaruush organizing team (Jul 2019 – Sep 2019) and SRM hackathon participant (Sep 2019)", body),
        Spacer(1, 1),
    ]
    doc.build(story)


if __name__ == "__main__":
    build()
