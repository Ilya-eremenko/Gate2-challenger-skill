from __future__ import annotations

from pathlib import Path
import xml.etree.ElementTree as ET
import zipfile


TEXT_SUFFIXES = {".md", ".txt", ".csv"}
WORD_SUFFIXES = {".docx", ".dotx"}


def read_document(path: Path) -> str:
    path = Path(path)
    suffix = path.suffix.lower()
    if suffix in TEXT_SUFFIXES:
        return path.read_text(encoding="utf-8")
    if suffix in WORD_SUFFIXES:
        return _read_word_document(path)
    raise ValueError(f"Unsupported document type: {path}")


def _read_word_document(path: Path) -> str:
    try:
        with zipfile.ZipFile(path) as archive:
            xml_bytes = archive.read("word/document.xml")
    except KeyError as exc:
        raise ValueError(f"Word document has no word/document.xml: {path}") from exc
    except zipfile.BadZipFile as exc:
        raise ValueError(f"Word document is not a valid zip archive: {path}") from exc

    root = ET.fromstring(xml_bytes)
    namespace = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main"}
    paragraphs: list[str] = []
    for paragraph in root.findall(".//w:p", namespace):
        parts = [
            node.text
            for node in paragraph.findall(".//w:t", namespace)
            if node.text is not None
        ]
        if parts:
            paragraphs.append("".join(parts))
    return "\n\n".join(paragraphs)
