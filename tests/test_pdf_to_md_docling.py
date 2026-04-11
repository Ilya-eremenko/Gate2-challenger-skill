import importlib.util
import io
import tempfile
import unittest
from contextlib import redirect_stderr
from pathlib import Path
from unittest.mock import patch

from docling_core.types.doc import ImageRefMode


REPO_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = REPO_ROOT / "scripts" / "pdf_to_md_docling.py"


def load_module():
    spec = importlib.util.spec_from_file_location("pdf_to_md_docling", MODULE_PATH)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load module from {MODULE_PATH}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class ResolveOutputPathTests(unittest.TestCase):
    def test_resolve_output_path_adds_numeric_suffix(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp_dir:
            output_dir = Path(tmp_dir)
            (output_dir / "report.md").write_text("first", encoding="utf-8")
            (output_dir / "report1.md").write_text("second", encoding="utf-8")

            resolved = module.resolve_output_path(Path("report.pdf"), output_dir)

        self.assertEqual("report2.md", resolved.name)


class ConvertPdfTests(unittest.TestCase):
    def test_convert_creates_output_dir_and_uses_placeholder_images(self):
        module = load_module()

        with tempfile.TemporaryDirectory() as tmp_dir:
            temp_root = Path(tmp_dir)
            pdf_path = temp_root / "source.pdf"
            pdf_path.write_bytes(b"%PDF-1.4\n")
            output_dir = temp_root / "review-documents"

            captured = {}

            class FakeDocument:
                def save_as_markdown(self, filename, **kwargs):
                    captured["filename"] = Path(filename)
                    captured["kwargs"] = kwargs
                    Path(filename).write_text("# converted\n", encoding="utf-8")

            class FakeConversionResult:
                document = FakeDocument()

            class FakeConverter:
                def convert(self, source):
                    captured["source"] = Path(source)
                    return FakeConversionResult()

            with patch.object(module, "DocumentConverter", FakeConverter):
                output_path = module.convert_pdf_to_markdown(pdf_path, output_dir=output_dir)
                output_dir_exists = output_dir.exists()

        self.assertTrue(output_dir_exists)
        self.assertEqual(pdf_path, captured["source"])
        self.assertEqual(output_path, captured["filename"])
        self.assertEqual(ImageRefMode.PLACEHOLDER, captured["kwargs"]["image_mode"])
        self.assertIsNone(captured["kwargs"]["artifacts_dir"])


class MainTests(unittest.TestCase):
    def test_main_returns_error_for_missing_pdf(self):
        module = load_module()
        stderr = io.StringIO()

        with redirect_stderr(stderr):
            exit_code = module.main(["does-not-exist.pdf"])

        self.assertNotEqual(0, exit_code)
        self.assertIn("PDF file does not exist", stderr.getvalue())


if __name__ == "__main__":
    unittest.main()
