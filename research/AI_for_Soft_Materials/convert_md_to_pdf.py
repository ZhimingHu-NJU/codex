#!/usr/bin/env python3
"""Convert the existing AI-for-soft-materials Markdown files to PDF.

Preferred conversion order:
1. Playwright/Chromium (HTML -> print PDF)
2. WeasyPrint (HTML -> PDF)
3. pandoc + xelatex
4. Built-in fallback PDF renderer using a standard CJK Type0 PDF font

The fallback is intentionally self-contained because this environment may not
include pandoc/xelatex/wkhtmltopdf/playwright/weasyprint or installable fonts.
It preserves headings, paragraphs, bullet lists, simple tables and code blocks,
and uses STSong-Light with UniGB-UCS2-H for Chinese text.
"""
from __future__ import annotations

import html
import importlib.util
import os
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from pathlib import Path
from textwrap import wrap

ROOT = Path(__file__).resolve().parent
FILES = [
    "AI_for_Programmable_Soft_Materials_Global_Groups_Report.md",
    "Strategy_AI_Assisted_LCE_and_Soft_Actuators.md",
    "AI_for_Soft_Materials_One_Page_Summary.md",
    "AI_for_Programmable_Soft_Materials_Reading_List.md",
]

FONT_CANDIDATES = [
    "Noto Sans CJK SC",
    "Source Han Sans SC",
    "PingFang SC",
    "Microsoft YaHei",
    "SimSun",
    "Arial Unicode MS",
    "WenQuanYi Zen Hei",
    "DejaVu Sans",
]

CSS = """
@page { size: A4; margin: 18mm 16mm; }
body {
  font-family: "Noto Sans CJK SC", "Source Han Sans SC", "PingFang SC", "Microsoft YaHei", "SimSun", "Arial Unicode MS", sans-serif;
  color: #111827; font-size: 10.5pt; line-height: 1.58;
}
h1 { font-size: 22pt; border-bottom: 2px solid #374151; padding-bottom: 8px; }
h2 { font-size: 16pt; margin-top: 24px; color: #1f2937; }
h3 { font-size: 13pt; margin-top: 18px; color: #374151; }
p, li { orphans: 3; widows: 3; }
a { color: #1d4ed8; text-decoration: none; overflow-wrap: anywhere; }
blockquote { border-left: 4px solid #9ca3af; margin-left: 0; padding: 6px 12px; background: #f9fafb; }
code, pre { font-family: "Noto Sans Mono CJK SC", "Source Han Mono SC", Consolas, monospace; }
pre { white-space: pre-wrap; word-break: break-word; background: #f3f4f6; padding: 8px; border-radius: 4px; }
table { border-collapse: collapse; width: 100%; table-layout: fixed; font-size: 7.2pt; page-break-inside: auto; }
th, td { border: 0.5px solid #9ca3af; padding: 3px 4px; vertical-align: top; overflow-wrap: anywhere; word-break: break-word; }
th { background: #f3f4f6; font-weight: 700; }
"""


def command_exists(name: str) -> bool:
    return shutil.which(name) is not None


def module_exists(name: str) -> bool:
    return importlib.util.find_spec(name) is not None


def detect_chinese_font() -> tuple[bool, str]:
    if not command_exists("fc-match"):
        return False, "fc-match not available"
    for font in FONT_CANDIDATES:
        try:
            out = subprocess.check_output(["fc-match", font], text=True, stderr=subprocess.DEVNULL).strip()
        except Exception:
            continue
        # If a requested CJK font maps to DejaVu, that normally means it is not installed.
        if out and "DejaVu" not in out:
            return True, f"{font} -> {out}"
    try:
        zh = subprocess.check_output(["fc-list", ":lang=zh"], text=True, stderr=subprocess.DEVNULL).strip()
        if zh:
            return True, zh.splitlines()[0]
    except Exception:
        pass
    return False, "No installed CJK font detected by fontconfig; fallback PDF uses standard PDF CJK font STSong-Light."


def inline_md(s: str) -> str:
    s = html.escape(s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', s)
    return s


def md_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    in_ul = False
    in_ol = False
    in_pre = False
    table_buf: list[str] = []

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def flush_table() -> None:
        nonlocal table_buf
        if not table_buf:
            return
        rows = []
        for line in table_buf:
            stripped = line.strip().strip("|")
            cells = [c.strip() for c in stripped.split("|")]
            if all(re.fullmatch(r":?-{2,}:?", c.replace(" ", "")) for c in cells):
                continue
            rows.append(cells)
        if rows:
            out.append("<table>")
            for i, cells in enumerate(rows):
                tag = "th" if i == 0 else "td"
                out.append("<tr>" + "".join(f"<{tag}>" + inline_md(c) + f"</{tag}>" for c in cells) + "</tr>")
            out.append("</table>")
        table_buf = []

    for line in lines:
        if line.strip().startswith("```"):
            flush_table(); close_lists()
            if not in_pre:
                out.append("<pre>")
                in_pre = True
            else:
                out.append("</pre>")
                in_pre = False
            continue
        if in_pre:
            out.append(html.escape(line) + "\n")
            continue
        if "|" in line and line.strip().startswith("|"):
            close_lists(); table_buf.append(line); continue
        flush_table()
        if not line.strip():
            close_lists(); continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            close_lists()
            level = len(m.group(1))
            out.append(f"<h{level}>" + inline_md(m.group(2)) + f"</h{level}>")
            continue
        m = re.match(r"^\s*[-*]\s+(.*)$", line)
        if m:
            if not in_ul:
                close_lists(); out.append("<ul>"); in_ul = True
            out.append("<li>" + inline_md(m.group(1)) + "</li>")
            continue
        m = re.match(r"^\s*\d+[.)]\s+(.*)$", line)
        if m:
            if not in_ol:
                close_lists(); out.append("<ol>"); in_ol = True
            out.append("<li>" + inline_md(m.group(1)) + "</li>")
            continue
        if line.startswith(">"):
            close_lists(); out.append("<blockquote>" + inline_md(line.lstrip("> ")) + "</blockquote>")
        else:
            close_lists(); out.append("<p>" + inline_md(line) + "</p>")
    flush_table(); close_lists()
    if in_pre:
        out.append("</pre>")
    return "<!doctype html><html><head><meta charset='utf-8'><style>" + CSS + "</style></head><body>" + "\n".join(out) + "</body></html>"


def try_playwright(md_path: Path, pdf_path: Path) -> bool:
    if not module_exists("playwright"):
        return False
    try:
        from playwright.sync_api import sync_playwright
        html_text = md_to_html(md_path.read_text(encoding="utf-8"))
        with tempfile.TemporaryDirectory() as td:
            html_path = Path(td) / "doc.html"
            html_path.write_text(html_text, encoding="utf-8")
            with sync_playwright() as p:
                browser = p.chromium.launch()
                page = browser.new_page()
                page.goto(html_path.as_uri(), wait_until="networkidle")
                page.pdf(path=str(pdf_path), format="A4", print_background=True, margin={"top":"18mm","right":"16mm","bottom":"18mm","left":"16mm"})
                browser.close()
        return pdf_path.exists() and pdf_path.stat().st_size > 0
    except Exception as exc:
        print(f"playwright failed for {md_path.name}: {exc}", file=sys.stderr)
        return False


def try_weasyprint(md_path: Path, pdf_path: Path) -> bool:
    if not module_exists("weasyprint"):
        return False
    try:
        from weasyprint import HTML
        HTML(string=md_to_html(md_path.read_text(encoding="utf-8")), base_url=str(ROOT)).write_pdf(str(pdf_path))
        return pdf_path.exists() and pdf_path.stat().st_size > 0
    except Exception as exc:
        print(f"weasyprint failed for {md_path.name}: {exc}", file=sys.stderr)
        return False


def try_pandoc(md_path: Path, pdf_path: Path) -> bool:
    if not (command_exists("pandoc") and command_exists("xelatex")):
        return False
    cmd = [
        "pandoc", str(md_path), "-o", str(pdf_path),
        "--pdf-engine=xelatex",
        "-V", "CJKmainfont=Noto Sans CJK SC",
        "-V", "geometry:margin=18mm",
    ]
    try:
        subprocess.check_call(cmd)
        return pdf_path.exists() and pdf_path.stat().st_size > 0
    except Exception as exc:
        print(f"pandoc failed for {md_path.name}: {exc}", file=sys.stderr)
        return False


@dataclass
class TextLine:
    text: str
    size: float
    kind: str = "normal"


def strip_md(s: str) -> str:
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", s)
    s = re.sub(r"[*_`>#]", "", s)
    return s.strip()


def lines_from_markdown(md: str) -> list[TextLine]:
    result: list[TextLine] = []
    in_code = False
    for raw in md.splitlines():
        line = raw.rstrip()
        if line.strip().startswith("```"):
            in_code = not in_code
            result.append(TextLine("", 9, "code"))
            continue
        if not line.strip():
            result.append(TextLine("", 10)); continue
        if in_code:
            result.append(TextLine(line, 8, "code")); continue
        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            level = len(m.group(1))
            size = {1: 18, 2: 14, 3: 12}.get(level, 10.5)
            result.append(TextLine(strip_md(m.group(2)), size, "heading")); continue
        if line.strip().startswith("|"):
            text = "  |  ".join(c.strip() for c in line.strip().strip("|").split("|"))
            if re.fullmatch(r"[-:|\s]+", line.strip()):
                continue
            result.append(TextLine(strip_md(text), 6.4, "table")); continue
        m = re.match(r"^\s*([-*]|\d+[.)])\s+(.*)$", line)
        if m:
            result.append(TextLine("• " + strip_md(m.group(2)), 9.5, "normal")); continue
        result.append(TextLine(strip_md(line), 9.5, "normal"))
    return result


def pdf_escape_bytes_utf16be(text: str) -> str:
    data = b"\xfe\xff" + text.encode("utf-16-be", errors="replace")
    return "<" + data.hex().upper() + ">"


def ascii_pdf_string(text: str) -> str:
    return "(" + text.replace("\\", "\\\\").replace("(", "\\(").replace(")", "\\)") + ")"


def wrap_cjk(text: str, chars: int) -> list[str]:
    if not text:
        return [""]
    chunks: list[str] = []
    cur = ""
    width = 0.0
    for ch in text:
        w = 1.0 if ord(ch) > 127 else 0.55
        if width + w > chars and cur:
            chunks.append(cur)
            cur = ch
            width = w
        else:
            cur += ch
            width += w
    if cur:
        chunks.append(cur)
    return chunks


def build_minimal_pdf(md_path: Path, pdf_path: Path) -> None:
    md = md_path.read_text(encoding="utf-8")
    logical = lines_from_markdown(md)
    page_w, page_h = 595.28, 841.89
    margin_l, margin_r, margin_t, margin_b = 45, 45, 44, 44
    max_chars_normal = 73
    pages: list[list[tuple[str, float, float, float]]] = []
    current: list[tuple[str, float, float, float]] = []
    y = page_h - margin_t

    def new_page() -> None:
        nonlocal current, y
        if current:
            pages.append(current)
        current = []
        y = page_h - margin_t

    for item in logical:
        if not item.text:
            y -= 8
            if y < margin_b: new_page()
            continue
        chars = max(28, int(max_chars_normal * 9.5 / item.size))
        if item.kind == "table":
            chars = 105
        for part in wrap_cjk(item.text, chars):
            line_h = item.size * (1.45 if item.kind != "heading" else 1.7)
            if y - line_h < margin_b:
                new_page()
            x = margin_l
            if item.kind == "table":
                x = 30
            current.append((part, item.size, x, y))
            y -= line_h
        if item.kind == "heading":
            y -= 3
    if current:
        pages.append(current)

    objects: list[bytes] = []

    def add(obj: str | bytes) -> int:
        if isinstance(obj, str):
            obj = obj.encode("latin-1")
        objects.append(obj)
        return len(objects)

    catalog_id = add("<< /Type /Catalog /Pages 2 0 R >>")
    pages_id = add(b"")
    font_id = add("<< /Type /Font /Subtype /Type0 /BaseFont /STSong-Light /Encoding /UniGB-UCS2-H /DescendantFonts [4 0 R] >>")
    cid_id = add("<< /Type /Font /Subtype /CIDFontType0 /BaseFont /STSong-Light /CIDSystemInfo << /Registry (Adobe) /Ordering (GB1) /Supplement 5 >> /FontDescriptor 5 0 R /DW 1000 >>")
    desc_id = add("<< /Type /FontDescriptor /FontName /STSong-Light /Flags 4 /FontBBox [-260 -200 1000 900] /ItalicAngle 0 /Ascent 880 /Descent -120 /CapHeight 700 /StemV 80 >>")
    page_ids: list[int] = []
    for page_lines in pages:
        stream_parts = ["BT"]
        for text, size, x, yy in page_lines:
            stream_parts.append(f"/F1 {size:.1f} Tf {x:.1f} {yy:.1f} Td {pdf_escape_bytes_utf16be(text)} Tj")
        stream_parts.append("ET")
        stream = "\n".join(stream_parts).encode("latin-1")
        content_id = add(b"<< /Length " + str(len(stream)).encode("ascii") + b" >>\nstream\n" + stream + b"\nendstream")
        page_id = add(f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {page_w:.2f} {page_h:.2f}] /Resources << /Font << /F1 3 0 R >> >> /Contents {content_id} 0 R >>")
        page_ids.append(page_id)
    kids = " ".join(f"{pid} 0 R" for pid in page_ids)
    objects[pages_id - 1] = f"<< /Type /Pages /Kids [{kids}] /Count {len(page_ids)} >>".encode("latin-1")

    out = bytearray(b"%PDF-1.6\n%\xe2\xe3\xcf\xd3\n")
    offsets = [0]
    for i, obj in enumerate(objects, 1):
        offsets.append(len(out))
        out.extend(f"{i} 0 obj\n".encode("ascii"))
        out.extend(obj)
        out.extend(b"\nendobj\n")
    xref = len(out)
    out.extend(f"xref\n0 {len(objects)+1}\n".encode("ascii"))
    out.extend(b"0000000000 65535 f \n")
    for off in offsets[1:]:
        out.extend(f"{off:010d} 00000 n \n".encode("ascii"))
    out.extend(f"trailer\n<< /Size {len(objects)+1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode("ascii"))
    pdf_path.write_bytes(out)


def convert(md_path: Path, pdf_path: Path) -> str:
    if try_playwright(md_path, pdf_path):
        return "playwright/chromium"
    if try_weasyprint(md_path, pdf_path):
        return "weasyprint"
    if try_pandoc(md_path, pdf_path):
        return "pandoc+xelatex"
    build_minimal_pdf(md_path, pdf_path)
    return "built-in CJK PDF fallback"


def main() -> int:
    print("Tool detection:")
    for c in ["python3", "pandoc", "xelatex", "wkhtmltopdf", "weasyprint"]:
        print(f"- {c}: {shutil.which(c) or 'NOT FOUND'}")
    for m in ["playwright", "weasyprint"]:
        print(f"- python module {m}: {'FOUND' if module_exists(m) else 'NOT FOUND'}")
    font_ok, font_msg = detect_chinese_font()
    print(f"- Chinese font detected: {font_ok}; {font_msg}")

    missing = [name for name in FILES if not (ROOT / name).exists()]
    if missing:
        print("Missing Markdown files: " + ", ".join(missing), file=sys.stderr)
        return 1

    print("\nConverting Markdown to PDF:")
    for name in FILES:
        md_path = ROOT / name
        pdf_path = md_path.with_suffix(".pdf")
        method = convert(md_path, pdf_path)
        size = pdf_path.stat().st_size if pdf_path.exists() else 0
        print(f"- {pdf_path.name}: {size} bytes via {method}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
