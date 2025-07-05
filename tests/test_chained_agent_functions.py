import sys
import types
import unittest
from unittest.mock import patch, MagicMock

# Provide a fake dotenv module if not installed
if 'dotenv' not in sys.modules:
    fake_dotenv = types.ModuleType('dotenv')
    fake_dotenv.load_dotenv = lambda *args, **kwargs: None
    sys.modules['dotenv'] = fake_dotenv

import scripts.chained_agent_functions as caf


class TestChainedAgentFunctions(unittest.TestCase):
    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_extract_summary(self, mock_generate):
        mock_generate.return_value = MagicMock(text=" Summary: test summary ")
        result = caf.extract_summary("dummy review")
        self.assertEqual(result, "test summary")
        mock_generate.assert_called_once()

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_formalize_summary(self, mock_generate):
        mock_generate.return_value = MagicMock(text=" Formal Report: test formal ")
        result = caf.formalize_summary("test summary")
        self.assertEqual(result, "test formal")
        mock_generate.assert_called_once()

    @patch('google.generativeai.GenerativeModel.generate_content')
    def test_recommend_action(self, mock_generate):
        mock_generate.return_value = MagicMock(text=" action text ")
        result = caf.recommend_action("formal report")
        self.assertEqual(result, "action text")
        mock_generate.assert_called_once()


if __name__ == '__main__':
    unittest.main()
