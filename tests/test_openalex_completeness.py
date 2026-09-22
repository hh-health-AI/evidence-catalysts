import contextlib
import io
import json
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import openalex_kol as oa


class OpenAlexTests(unittest.TestCase):
    def invoke(self, pages, cap=2):
        out = io.StringIO()
        with patch.object(oa, "get", side_effect=pages), \
             patch.object(sys, "argv", ["oa", "--concept", "test", "--max-works", str(cap)]), \
             contextlib.redirect_stdout(out):
            try:
                oa.main()
            except SystemExit:
                self.assertEqual(out.getvalue(), "")
                raise
        return json.loads(out.getvalue())

    def test_capped_query_has_no_trend(self):
        with self.assertRaises(SystemExit):
            self.invoke([{"meta": {"count": 3}, "results": []}])

    def test_missing_count_fails(self):
        with self.assertRaises(SystemExit):
            self.invoke([{"results": []}])

    def test_complete_query(self):
        result = self.invoke([{"meta": {"count": 1}, "results": [{"id": "W1", "publication_year": 2025}]}])
        self.assertEqual(result["coverage"], {"matched": 1, "fetched": 1, "truncated": False})

    def test_duplicate_works_fail(self):
        with self.assertRaises(SystemExit):
            self.invoke([{"meta": {"count": 2, "next_cursor": "next"}, "results": [{"id": "W1"}]},
                         {"meta": {"count": 2}, "results": [{"id": "W1"}]}])

    def test_early_cursor_exhaustion_fails(self):
        with self.assertRaises(SystemExit):
            self.invoke([{"meta": {"count": 2}, "results": [{"id": "W1"}]}])


if __name__ == "__main__":
    unittest.main()
