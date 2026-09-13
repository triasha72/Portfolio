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
    return f'<link href="https://github.com/triasha72/{repository}" color="#0000FF"><u>{label}</u></link>'


def build() -> None:
    regular, bold = _fonts()
    black = colors.black
    styles = getSampleStyleSheet()
    name = ParagraphStyle(
        "Name", parent=styles["Normal"], fontName=bold, fontSize=22,
        leading=24, alignment=TA_CENTER, textColor=black, spaceAfter=3,
    )
    contact = ParagraphStyle(
        "Contact", parent=styles["Normal"], fontName=regular, fontSize=8.2,
        leading=10.8, alignment=TA_CENTER, textColor=black, spaceAfter=9,
    )
    summary = ParagraphStyle(
        "Summary", parent=styles["Normal"], fontName=regular, fontSize=9,
        leading=12.4, textColor=black, spaceAfter=8,
    )
    section = ParagraphStyle(
        "Section", parent=styles["Heading2"], fontName=bold, fontSize=9.2,
        leading=11.5, textColor=black, spaceBefore=7, spaceAfter=4,
        borderWidth=0, borderPadding=0, borderBottomWidth=0.7,
        borderBottomColor=black, borderBottomPadding=2,
    )
    role = ParagraphStyle(
        "Role", parent=styles["Normal"], fontName=bold, fontSize=8.7,
        leading=11.2, textColor=black, spaceBefore=4, spaceAfter=2,
        keepWithNext=True,
    )
    body = ParagraphStyle(
        "Body", parent=styles["Normal"], fontName=regular, fontSize=8.5,
        leading=11.8, textColor=black, spaceAfter=3,
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
            'Atlanta, GA | +1 (404) 948-8761 | <link href="mailto:tsarkar34@gatech.edu" color="#0000FF"><u>tsarkar34@gatech.edu</u></link><br/>'
            '<link href="https://www.linkedin.com/in/triasha-sarkar/" color="#0000FF"><u>linkedin.com/in/triasha-sarkar</u></link> | '
            '<link href="https://github.com/triasha72" color="#0000FF"><u>github.com/triasha72</u></link> | '
            '<link href="https://triasha72.github.io/Portfolio/" color="#0000FF"><u>triasha72.github.io/Portfolio</u></link>', contact,
        ),
        Paragraph(
            "Machine Learning Engineer with experience in scientific ML, model evaluation, retrieval, "
            "time-series data, and ML systems. Background in aerospace engineering, simulation, and uncertainty.", summary,
        ),
        Paragraph("<u>PROFESSIONAL EXPERIENCE</u>", section),
        Paragraph("Graduate Research Assistant under Prof. Dimitri Mavris | Georgia Tech ASDL | May 2025 – Aug 2026", role),
        Paragraph("Built and tested Python models for projects in simulation, airline safety, and sustainable aviation; shared reproducible analyses with faculty and sponsors.", bullet, bulletText="•"),
        Paragraph("Reviewed assumptions and limits with aerospace experts and documented each workflow so other researchers could rerun it.", bullet, bulletText="•"),
        Paragraph("Machine Learning Engineer | Rolls-Royce | Jul 2023 – Apr 2025", role),
        Paragraph("Developed Python pipelines to flag unusual engine behavior, support maintenance planning, and combine sensor streams sampled at different rates.", bullet, bulletText="•"),
        Paragraph("Mapped certification requirements to data and model checks, then reviewed results with lifecycle engineers before use.", bullet, bulletText="•"),
        Paragraph("Data Science Intern | Rolls-Royce DataLabs | May 2021 – Jul 2021", role),
        Paragraph("Cleaned aircraft-engine sensor data, built features, and compared prediction and anomaly models; summarized recurring failure patterns for engineers.", bullet, bulletText="•"),
        Paragraph("<u>TECHNICAL PROJECTS</u>", section),
        KeepTogether([
            Paragraph(f"{edgegenbench} | Real-flight ML and on-device inference | Aug 2026 – Present", role),
            Paragraph("Trained a flight-anomaly model on NASA DASHlink recordings and tested it on 17,780 approaches from held-out aircraft. Its 0.738 macro F1 missed the release target.", bullet, bulletText="•"),
            Paragraph("Exported the model to ONNX and tested corrupted sensor inputs; prediction agreement stayed above 99.55% across the tested cases.", bullet, bulletText="•"),
        ]),
        Paragraph(f"{integritybench} | Moderation evaluation and release controls | Aug 2026 – Present", role),
        Paragraph("Built controlled evaluation and release checks for changing moderation policies, keeping separate candidates and frozen benchmark results distinct from deployment claims.", bullet, bulletText="•"),
        Paragraph(f"{aerosynth} | Synthetic inspection-image evaluation | Aug 2026 – Present", role),
        Paragraph("Evaluated synthetic aircraft-inspection image data with reproducible splits; reported where results were strong, limited, or still pending validation.", bullet, bulletText="•"),
        KeepTogether([
            Paragraph(f"{newslens} | Recommendation and real-time search | Jul 2026 – Present", role),
            Paragraph("Used chronological splits to keep future clicks out of training. The recommender scored 0.366 NDCG@10, but the uncertainty interval still included no improvement.", bullet, bulletText="•"),
            Paragraph("Built a Go, Kafka, PostgreSQL, and FastAPI ingestion path for new articles. In a 500-event run, publish p99 was 44 ms and search freshness p95 was 79 ms.", bullet, bulletText="•"),
        ]),
        Paragraph(f"{equity} | Walk-forward signal evaluation | Jul 2026 – Present", role),
        Paragraph("Built a cross-sectional equity-signal backtest with trading costs and safeguards against common look-ahead and selection biases.", bullet, bulletText="•"),
        Paragraph("Atlanta Mobility Resilience Digital Twin | Independent project | 2026 – Present", role),
        Paragraph("Built an OSMnx and MARTA GTFS graph-analysis workflow covering 50 Census-tract origins, 101 essential-service destinations, and 216,659 estimated residents; the planned accessibility validation cycle is still pending.", bullet, bulletText="•"),
        Paragraph("Silent Failure Detection in Rocket-Motor Simulations | AE8900 Special Problems Coursework | May 2026 – Jul 2026", role),
        Paragraph("Traced silent failures in a 15,120-case rocket-motor study to an uncapped convergence loop; a leakage-safe classifier reached 96.8% accuracy on unseen geometries.", bullet, bulletText="•"),
        Paragraph(f"{surrogate} | Reliability under design shift | Feb 2026 – Present", role),
        Paragraph("Evaluated Gaussian-process and conventional surrogates on public airfoil, energy, and concrete data using grouped splits, multi-seed analysis, split-conformal intervals, and distance-to-training-domain guards.", bullet, bulletText="•"),
        Paragraph("An airfoil Gaussian process reached R² 0.8145 on a physically grouped split; a 10-seed mean of 0.8662 ± 0.0680 exposed split sensitivity. Nominal 90% intervals did not retain 90% coverage under design shift.", bullet, bulletText="•"),
        Paragraph(f"{airfaans} | Extension of AE6394 Coursework Project | Jan 2026 – Apr 2026", role),
        Paragraph("Compared an MLP, MeshGraphNet-style GNN, and point neural operator across three matched seeds and 200 AirfRANS interpolation meshes per model; MeshGraphNet had the lowest mean field and drag error.", bullet, bulletText="•"),
        Paragraph("Used simulation-level splits and train-only normalization; matched OOD, uncertainty, and active-learning studies are in progress, with no results reported yet.", bullet, bulletText="•"),
        Paragraph(f"{aerorag} | Independent extension of Project HERO | Retrieval, evaluation, and ML systems | Oct 2025 – Present", role),
        Paragraph("Extended Project HERO independently into a technical-knowledge system over 3,233 NASA report sections using hybrid retrieval, reranking, evidence checks, controlled citations, and containerized FastAPI services; retained negative experimental findings rather than claiming every change helped.", bullet, bulletText="•"),
        Paragraph("Project EAGLE | RIC Enterprise-sponsored Vehicle Grand Challenge | Georgia Tech ASDL | Sep 2025 – Present", role),
        Paragraph("Developed sizing and synthesis tooling, passenger layout, AutoCAD cabin geometry, and requirements for the Eco-friendly Airborne Global Luxury Ekranoplan.", bullet, bulletText="•"),
        Paragraph("Project GREEN TEA | U.S. Endowment-sponsored Systems of Systems Grand Challenge | Georgia Tech ASDL | Sep 2025 – Present", role),
        Paragraph("Developed a techno-economic framework for forest-residue sustainable aviation fuel and bioenergy, including jobs, CO2 impacts, a GREET surrogate, and forest-health modeling.", bullet, bulletText="•"),
        Paragraph("Project HERO | Delta Air Lines-sponsored source-aware retrieval for airline safety | Georgia Tech ASDL | May 2025 – Aug 2026", role),
        Paragraph("Developed source-aware retrieval and evaluation methods for airline-safety analysis.", bullet, bulletText="•"),
        Paragraph("Supersonic Business Jets and Noise Mitigation | Sponsored by Rolls-Royce, Seneca, and DLR | Cranfield University | Sep 2022 – Feb 2023", role),
        Paragraph("Studied geometry, noise mitigation, high-speed aerodynamics, and design trade-offs.", body),
        Paragraph("Thermal System Design Engineer Group Project | Sponsored by GKN Aerospace | Cranfield University | Sep 2022 – Feb 2023", role),
        Paragraph("Worked in a multidisciplinary team on thermal-system architecture, requirements, sizing, and design trade-offs for an aerospace application.", body),
        Paragraph("Bird-Strike Impact Analysis | SRM Institute of Science and Technology | Jun 2020 – Jun 2021", role),
        Paragraph("Used ANSYS to compare aircraft nose-cone material choices for bird-strike impact.", body),
        Paragraph("Ornithopter Aerodynamics | SRM Institute of Science and Technology | Sep 2019 – May 2020", role),
        Paragraph("Used CFD to examine ornithopter wing area and load factor.", body),
        Paragraph("<u>TECHNICAL SKILLS</u>", section),
        Paragraph("<b>ML and scientific ML:</b> PyTorch, PyTorch Geometric, scikit-learn, graph neural networks, neural operators, surrogate modeling, uncertainty quantification, Transformers, RAG, BM25, dense retrieval, reranking", body),
        Paragraph("<b>Systems:</b> Python, Go, SQL, Kafka, FastAPI, Docker, Kubernetes, GitHub Actions, PostgreSQL/pgvector, Prometheus, OpenTelemetry, ONNX, Core ML, Qualcomm QNN", body),
        Paragraph("<b>Scientific computing:</b> NumPy, SciPy, pandas, CFD meshes, NetworkX, OSMnx, statistical inference, design of experiments", body),
        Spacer(1, 5),
        Paragraph("<u>LEADERSHIP AND HACKATHONS</u>", section),
        Paragraph("Graduate Chair | Women of Aeronautics and Astronautics, Georgia Tech | Aug 2025 – Aug 2026", bullet, bulletText="•"),
        Paragraph("Organising Team Member | Aarush Hackathon Event, SRM University | Jun 2019 – Jul 2019", bullet, bulletText="•"),
        Paragraph("Student Volunteer | Aarush, SRM University | Aug 2018 – Jan 2019", bullet, bulletText="•"),
        Paragraph("Team Participant | 36-Hour SRM Hackathon, SRM University | Sep 2019", bullet, bulletText="•"),
        Paragraph("Worked in a five-member team on a sustainable urban-transport concept for densely populated Indian cities, comparing travel time, fuel use, cost, and CO2 emissions.", bullet, bulletText="•"),
        Paragraph("<u>EDUCATION</u>", section),
        Paragraph("M.S., Aerospace Engineering | Georgia Institute of Technology, Atlanta, GA | Aug 2026", role),
        Paragraph("GPA: 3.7/4.0", body),
        Paragraph("M.Sc., Aerospace Vehicle Design | Cranfield University, United Kingdom | Feb 2023", role),
        Paragraph("GPA: 3.6/4.0 | First Class Honours | Thesis: geometry optimization under FAA constraints", body),
        Paragraph("B.Tech., Aerospace Engineering | SRM Institute of Science and Technology, India | Jun 2021", role),
        Paragraph("GPA: 3.8/4.0 | First Class Honours", body),
        Spacer(1, 3),
    ]
    doc.build(story)


if __name__ == "__main__":
    build()
