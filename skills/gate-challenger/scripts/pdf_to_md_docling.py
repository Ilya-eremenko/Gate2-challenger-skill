#!/usr/bin/env python3

import argparse
import sys
from pathlib import Path

from docling.document_converter import DocumentConverter
from docling_core.types.doc import ImageRefMode


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Convert a PDF file to Markdown with Docling."
    )
    parser.add_argument("pdf_path", help="Path to the source PDF file.")
    return parser


def resolve_output_path(pdf_path: Path, output_dir: Path) -> Path:
    base_name = pdf_path.stem
    candidate = output_dir / f"{base_name}.md"
    suffix = 1

    while candidate.exists():
        candidate = output_dir / f"{base_name}{suffix}.md"
        suffix += 1

    return candidate


def default_output_dir(pdf_path: Path) -> Path:
    return pdf_path.parent / "review-documents"


def convert_pdf_to_markdown(pdf_path: Path, output_dir: Path | None = None) -> Path:
    if not pdf_path.exists():
        raise FileNotFoundError(f"PDF file does not exist: {pdf_path}")
    if not pdf_path.is_file():
        raise FileNotFoundError(f"PDF path is not a file: {pdf_path}")

    target_dir = output_dir or default_output_dir(pdf_path)
    target_dir.mkdir(parents=True, exist_ok=True)
    output_path = resolve_output_path(pdf_path, target_dir)

    converter = DocumentConverter()
    result = converter.convert(str(pdf_path))
    result.document.save_as_markdown(
        output_path,
        artifacts_dir=None,
        image_mode=ImageRefMode.PLACEHOLDER,
    )

    return output_path


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        output_path = convert_pdf_to_markdown(Path(args.pdf_path).expanduser().resolve())
    except Exception as exc:
        print(str(exc), file=sys.stderr)
        return 1

    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
