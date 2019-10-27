import unittest

from searchyt import searchyt

class TestSearchyt(unittest.TestCase):
    syt = searchyt()

    def test_result(self):
        result = TestSearchyt.syt.search("rick roll")

        self.assertEqual(result[0]["id"], "dQw4w9WgXcQ")
    
    def test_noresult(self):
        result = TestSearchyt.syt.search("vaervvvvvvvvvvvvvvvawedfuihefuiabeyufewf")

        self.assertEqual(len(result), 0)