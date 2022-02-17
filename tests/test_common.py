"""Unit tests for Common functions used ."""
from unittest import TestCase

from src.common import get_report_score


REPORT_TEST_DATA = [{
    "report": {
        "ScoreBlock": {
            "Delphi": [{"Score": 100}]
        }
    }
},{
    "report": {
        "ScoreBlock": {
            "Delphi": [{"Score": "200"}]
        }
    }
},{
    "report": {
        "ScoreBlock": {
            "Delphi": [{"Score": "string"}]
        }
    }
},{
    "report": {
        "ScoreBlock": {
            "Delphi": []
        }
    }
},{
    "report": {
        "ScoreBlock": {
            "": ""
        }
    }
}]

REPORT_EXPECTED_RESULTS = [100, 200, None, None, None]


class BaseCommonFunctionTests(TestCase):
    """
    Test common functions used.
    """

    def test_get_report_score(self) -> None:
        """Test get_report_score with edge cases."""


        for i, report in enumerate(REPORT_TEST_DATA):
            self.assertEquals(get_report_score(report), REPORT_EXPECTED_RESULTS[i])
