import os
import sys
from playwright.sync_api import sync_playwright

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MD_FILE = os.path.join(BASE_DIR, "ai_solopreneur_toolkit_2026.md")
PDF_FILE = os.path.join(BASE_DIR, "ai_solopreneur_toolkit_2026.pdf")

def create_styled_html():
    with open(MD_FILE, "r", encoding="utf-8") as f:
        content = f.read()

    # Convert simple markdown to html
    lines = content.split("\n")
    html_lines = []
    for line in lines:
        if line.startswith("# "):
            html_lines.append(f"<h1 style='color: #0f172a; border-bottom: 2px solid #38bdf8; padding-bottom: 8px; margin-top: 24px;'>{line[2:]}</h1>")
        elif line.startswith("## "):
            html_lines.append(f"<h2 style='color: #1e293b; margin-top: 20px;'>{line[3:]}</h2>")
        elif line.startswith("### "):
            html_lines.append(f"<h3 style='color: #334155; margin-top: 16px;'>{line[4:]}</h3>")
        elif line.startswith("* **") or line.startswith("- **"):
            html_lines.append(f"<li style='margin-bottom: 8px;'>{line[2:]}</li>")
        elif line.startswith("> "):
            html_lines.append(f"<blockquote style='background: #f1f5f9; border-left: 4px solid #38bdf8; padding: 12px 16px; margin: 12px 0; font-style: italic;'>{line[2:]}</blockquote>")
        elif line.strip() == "---":
            html_lines.append("<hr style='border: none; border-top: 1px solid #e2e8f0; margin: 24px 0;'/>")
        elif line.strip():
            html_lines.append(f"<p style='margin-bottom: 12px; line-height: 1.6; color: #475569;'>{line}</p>")

    body_html = "\n".join(html_lines)
    full_html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    max-width: 800px;
    margin: 40px auto;
    padding: 0 20px;
    color: #1e293b;
    background: #ffffff;
  }}
  li strong {{ color: #0f172a; }}
  p strong {{ color: #0f172a; }}
</style>
</head>
<body>
{body_html}
</body>
</html>"""
    return full_html

def generate_pdf():
    html_content = create_styled_html()
    temp_html_path = os.path.join(BASE_DIR, "temp_doc.html")
    with open(temp_html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    print("Dang xuat ban file PDF chuyen nghiep qua Playwright...")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(f"file:///{temp_html_path.replace(os.sep, '/')}")
        page.pdf(
            path=PDF_FILE,
            format="A4",
            margin={"top": "20mm", "bottom": "20mm", "left": "20mm", "right": "20mm"},
            print_background=True
        )
        browser.close()

    if os.path.exists(temp_html_path):
        os.remove(temp_html_path)

    print(f"Xuat ban thanh cong: {PDF_FILE} ({os.path.getsize(PDF_FILE) / 1024:.1f} KB)")

if __name__ == "__main__":
    generate_pdf()
