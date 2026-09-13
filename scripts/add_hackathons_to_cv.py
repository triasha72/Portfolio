"""Add the verified 2018–2019 hackathon entries to the portfolio CV."""

from __future__ import annotations

from io import BytesIO
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from reportlab.lib.colors import HexColor
from reportlab.lib.pagesizes import letter
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas


ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path("/System/Library/Fonts/Supplemental")


def register_fonts() -> tuple[str, str, str]:
    regular = FONT_DIR / "Arial.ttf"
    bold = FONT_DIR / "Arial Bold.ttf"
    italic = FONT_DIR / "Arial Italic.ttf"
    if regular.exists() and bold.exists() and italic.exists():
        pdfmetrics.registerFont(TTFont("CVArial", regular))
        pdfmetrics.registerFont(TTFont("CVArial-Bold", bold))
        pdfmetrics.registerFont(TTFont("CVArial-Italic", italic))
        return "CVArial", "CVArial-Bold", "CVArial-Italic"
    return "Helvetica", "Helvetica-Bold", "Helvetica-Oblique"


def overlay_page() -> BytesIO:
    regular, bold, italic = register_fonts()
    packet = BytesIO()
    canvas = Canvas(packet, pagesize=letter)
    left, right = 36, 576
    canvas.setFillColor(HexColor("#222222"))
    canvas.setFont(bold, 8.5)
    canvas.drawString(left, 390, "HACKATHONS")
    canvas.setLineWidth(0.6)
    canvas.line(left, 386, right, 386)

    entries = [
        ("Organising Team Member | Aarush Hackathon Event", "SRM University", "Jun 2019 – Jul 2019", 370),
        ("Student Volunteer | Aarush", "SRM University", "Aug 2018 – Jan 2019", 342),
        ("Team Participant | 36-Hour SRM Hackathon", "SRM University", "Sep 2019", 314),
    ]
    for title, affiliation, date, y in entries:
        canvas.setFont(bold, 8.3)
        canvas.drawString(left, y, title)
        canvas.setFont(regular, 8.1)
        canvas.drawRightString(right, y, date)
        canvas.setFont(italic, 8.0)
        canvas.setFillColor(HexColor("#555555"))
        canvas.drawString(left, y - 11, affiliation)
        canvas.setFillColor(HexColor("#222222"))

    canvas.setFont(regular, 7.9)
    canvas.drawString(left + 13, 292, "• Worked in a five-member team on a sustainable urban-transport concept for densely populated Indian cities,")
    canvas.drawString(left + 20, 281, "comparing travel time, fuel use, cost, and CO2 emissions.")
    canvas.save()
    packet.seek(0)
    return packet


def update_pdf(source: Path, destination: Path) -> None:
    reader = PdfReader(source)
    if len(reader.pages) != 2:
        raise ValueError("The CV must remain a two-page document.")
    overlay = PdfReader(overlay_page())
    reader.pages[1].merge_page(overlay.pages[0])
    writer = PdfWriter()
    for page in reader.pages:
        writer.add_page(page)
    with destination.open("wb") as output:
        writer.write(output)


def main() -> None:
    source = ROOT / "Triasha_Sarkar_CV.pdf"
    temporary = ROOT / "Triasha_Sarkar_CV_with_hackathons.pdf"
    update_pdf(source, temporary)
    temporary.replace(source)
    # Both public copies must be byte-identical so the root link and site asset agree.
    (ROOT / "assets" / "Triasha_Sarkar_CV.pdf").write_bytes(source.read_bytes())


if __name__ == "__main__":
    main()
