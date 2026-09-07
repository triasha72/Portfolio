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


def github_link(label: str, repository: str) -> str:
    return f'<link href="https://github.com/triasha72/{repository}"><u>{label}</u></link>'


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
    edgegenbench = github_link("EdgeGenBench", "EdgeGenBench")
    integritybench = github_link("IntegrityBench", "IntegrityBench")
    aerosynth = github_link("AeroSynth-Eval", "AeroSynth-Eval")
    newslens = github_link("NewsLens", "NewsLens")
    equity = github_link("Equity Backtest", "Equity-Backtest")
    surrogate = github_link("Surrogate Model Learning", "Surrogate-model-learning")
    airfaans = github_link("AIRFAANS", "AIRFAANS")
    aerorag = github_link("AeroRAG-X", "AeroRAG-X")
    story = [
        Paragraph("TRIASHA SARKAR", name),
        Paragraph(
            'Atlanta, GA | +1 (404) 948-8761 | <link href="mailto:tsarkar34@gatech.edu"><u>tsarkar34@gatech.edu</u></link><br/>'
            '<link href="https://www.linkedin.com/in/triasha-sarkar/"><u>linkedin.com/in/triasha-sarkar</u></link> | '
            '<link href="https://github.com/triasha72"><u>github.com/triasha72</u></link> | '
            '<link href="https://triasha72.github.io/Portfolio/"><u>triasha72.github.io/Portfolio</u></link>', contact,
        ),
        Paragraph(
            "Machine Learning Engineer with experience in scientific ML, model evaluation, retrieval, "
            "time-series data, and ML systems. Aerospace background with experience in simulation, "
            "uncertainty, and engineering problems.", summary,
        ),
        Paragraph("PROFESSIONAL EXPERIENCE", section),
        Paragraph("Graduate Research Assistant under Prof. Dimitri Mavris | Georgia Tech ASDL | May 2025 – Aug 2026", role),
        Paragraph("Built and tested Python models for projects in simulation, airline safety, and sustainable aviation; shared reproducible analyses with faculty and sponsors.", bullet, bulletText="•"),
        Paragraph("Reviewed assumptions and limits with aerospace experts and documented each workflow so other researchers could rerun it.", bullet, bulletText="•"),
        Paragraph("Machine Learning Engineer | Rolls-Royce | Jul 2023 – Apr 2025", role),
        Paragraph("Developed Python pipelines to flag unusual engine behavior, support maintenance planning, and combine sensor streams sampled at different rates.", bullet, bulletText="•"),
        Paragraph("Mapped certification requirements to data and model checks, then reviewed results with lifecycle engineers before use.", bullet, bulletText="•"),
        Paragraph("Data Science Intern | Rolls-Royce DataLabs | May 2021 – Jul 2021", role),
        Paragraph("Cleaned aircraft-engine sensor data, built features, and compared prediction and anomaly models; summarized recurring failure patterns for engineers.", bullet, bulletText="•"),
        Paragraph("TECHNICAL PROJECTS", section),
        KeepTogether([
            Paragraph(f"{edgegenbench} | Real-flight ML and on-device inference | Aug 2026 – Present", role),
            Paragraph("Trained a flight-anomaly model on NASA DASHlink recordings and tested it on 17,780 approaches from held-out aircraft. Its 0.738 macro F1 missed the release target.", bullet, bulletText="•"),
            Paragraph("Exported the model to ONNX and tested corrupted sensor inputs; prediction agreement stayed above 99.55% across the tested cases.", bullet, bulletText="•"),
        ]),
        Paragraph(f"{integritybench} | Moderation evaluation and release controls | Aug 2026 – Present", role),
        Paragraph("Built controlled evaluation and release checks for changing moderation policies, keeping separate candidates and frozen benchmark results distinct from deployment claims.", body),
        Paragraph(f"{aerosynth} | Synthetic inspection-image evaluation | Aug 2026 – Present", role),
        Paragraph("Evaluated synthetic aircraft-inspection image data with reproducible splits; reported where results were strong, limited, or still pending validation.", body),
        KeepTogether([
            Paragraph(f"{newslens} | Recommendation and real-time search | Jul 2026 – Present", role),
            Paragraph("Used chronological splits to keep future clicks out of training. The recommender scored 0.366 NDCG@10, but the uncertainty interval still included no improvement.", bullet, bulletText="•"),
            Paragraph("Built a Go, Kafka, PostgreSQL, and FastAPI ingestion path for new articles. In a 500-event run, publish p99 was 44 ms and search freshness p95 was 79 ms.", bullet, bulletText="•"),
        ]),
        Paragraph(f"{equity} | Walk-forward signal evaluation | Jul 2026 – Present", role),
        Paragraph("Built a cross-sectional equity-signal backtest with trading costs and safeguards against common look-ahead and selection biases.", body),
        Paragraph("Silent Failure Detection in Rocket-Motor Simulations | Georgia Tech ASDL | May 2026 – Jul 2026", role),
        Paragraph("Traced silent failures in a 15,120-case rocket-motor study to an uncapped convergence loop; a leakage-safe classifier reached 96.8% accuracy on unseen geometries.", body),
        Paragraph(f"{surrogate} | Reliability under design shift | Feb 2026 – Present", role),
        Paragraph("Evaluated Gaussian-process and conventional surrogates on public airfoil, energy, and concrete data using grouped splits, multi-seed analysis, split-conformal intervals, and distance-to-training-domain guards.", bullet, bulletText="•"),
        Paragraph("An airfoil Gaussian process reached R² 0.8145 on a physically grouped split; a 10-seed mean of 0.8662 ± 0.0680 exposed split sensitivity. Nominal 90% intervals did not retain 90% coverage under design shift.", bullet, bulletText="•"),
        Paragraph(f"{airfaans} | Geometry-aware CFD surrogates | Jan 2026 – Apr 2026", role),
        Paragraph("Compared an MLP, MeshGraphNet-style GNN, and point neural operator across three matched seeds and 200 AirfRANS interpolation meshes per model; MeshGraphNet had the lowest mean field and drag error.", bullet, bulletText="•"),
        Paragraph("Used simulation-level splits and train-only normalization; Reynolds/AoA OOD, uncertainty, and active-learning experiments remain pending.", bullet, bulletText="•"),
        Paragraph(f"{aerorag} | Retrieval, evaluation, and ML systems | Oct 2025 – Present", role),
        Paragraph("Built a technical-knowledge system over 3,233 NASA report sections using hybrid retrieval, reranking, evidence checks, controlled citations, and containerized FastAPI services; retained negative experimental findings rather than claiming every change helped.", bullet, bulletText="•"),
        Paragraph("GREEN TEA and Project EAGLE | Sustainable aviation modeling | Sep 2025 – Apr 2026", role),
        Paragraph("Built surrogate models to speed up sustainability calculations and connected fuel, demand, transport, and life-cycle inputs; GREEN TEA remains in sponsor use.", body),
        Paragraph("HERO | Source-aware retrieval for airline safety | Georgia Tech ASDL | May 2025 – Aug 2026", role),
        Paragraph("Developed source-aware retrieval and evaluation methods for airline-safety analysis.", body),
        Paragraph("Supersonic Business Jets and Noise Mitigation | Cranfield University | Sep 2022 – Feb 2023", role),
        Paragraph("Studied geometry, noise mitigation, high-speed aerodynamics, and design trade-offs.", body),
        Paragraph("Bird-Strike Impact Analysis | SRM Institute of Science and Technology | Jun 2020 – Jun 2021", role),
        Paragraph("Used ANSYS to compare aircraft nose-cone material choices for bird-strike impact.", body),
        Paragraph("Ornithopter Aerodynamics | SRM Institute of Science and Technology | Sep 2019 – May 2020", role),
        Paragraph("Used CFD to examine ornithopter wing area and load factor.", body),
        Paragraph("EDUCATION", section),
        Paragraph("MS, Aerospace Engineering | Georgia Institute of Technology, Atlanta, GA | Aug 2026", role),
        Paragraph("CGPA: 3.7/4.0", body),
        Paragraph("MSc, Aerospace Vehicle Design | Cranfield University, United Kingdom | Feb 2023", role),
        Paragraph("CGPA: 3.6/4.0 | First Class Honours | Thesis on geometry optimization under FAA constraints", body),
        Paragraph("B.Tech, Aerospace Engineering | SRM Institute of Science and Technology, India | Jun 2021", role),
        Paragraph("CGPA: 3.8/4.0 | First Class Honours", body),
        Paragraph("TECHNICAL SKILLS", section),
        Paragraph("<b>ML and scientific ML:</b> PyTorch, PyTorch Geometric, scikit-learn, graph neural networks, neural operators, surrogate modeling, uncertainty quantification, Transformers, RAG, BM25, dense retrieval, reranking", body),
        Paragraph("<b>Systems:</b> Python, Go, SQL, Kafka, FastAPI, Docker, Kubernetes, GitHub Actions, PostgreSQL/pgvector, Prometheus, OpenTelemetry, ONNX, Core ML, Qualcomm QNN", body),
        Paragraph("<b>Scientific computing:</b> NumPy, SciPy, pandas, CFD meshes, NetworkX, OSMnx, statistical inference, design of experiments", body),
        Spacer(1, 5),
        Paragraph("LEADERSHIP", section),
        Paragraph("Graduate Chair | Women of Aeronautics and Astronautics, Georgia Tech | Aug 2025 – Aug 2026", body),
        Paragraph("Organizing Team | Aaruush, SRM Institute of Science and Technology | Jul 2019 – Sep 2019", body),
        Paragraph("Helped organize a campus hackathon, gaining early exposure to collaborative, deadline-driven technical projects and the student developer community.", bullet, bulletText="•"),
        Paragraph("Hackathon Participant | SRM Institute of Science and Technology | Sep 2019", body),
        Paragraph("Worked in a five-member team to plan a sustainable-city modeling project.", bullet, bulletText="•"),
        Spacer(1, 3),
    ]
    doc.build(story)


if __name__ == "__main__":
    build()
