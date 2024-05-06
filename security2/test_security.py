import unittest

from security import read_file
from security import rescue_people


def setUpModule():
    global smart_people_txt
    smart_people_txt = """\
Steve Jobs: 160
Albert Einstein: 160
Sir Isaac Newton: 195
Nikola Tesla: 189"""

class TestBlackboxAI(unittest.TestCase):

    def test_read_file(self):
        self.assertEqual(read_file('smart_people.txt'),
                         {"Steve Jobs": 160, "Albert Einstein": 160,
                          "Sir Isaac Newton": 195, "Nikola Tesla": 189})

    def test_rescue_people(self):
        smarties = {"Steve Jobs": 160, "Albert Einstein": 160,
                    "Sir Isaac Newton": 195, "Nikola Tesla": 189}
        self.assertEqual(rescue_people(smarties, 500), (2, [["Sir Isaac Newton", "Nikola Tesla"],
                                                            ["Albert Einstein", "Steve Jobs"]]))
        self.assertEqual(rescue_people({}, 500), (0, []))
        self.assertEqual(rescue_people(smarties, 600), (2, [["Sir Isaac Newton", "Nikola Tesla", "Albert Einstein"],
                                                             ["Steve Jobs"]]))
if __name__ == '__main__':
    unittest.main(module=__name__, exit=False)
