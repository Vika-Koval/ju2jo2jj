import unittest

from rescue import read_file
from rescue import rescue_people


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
# class TestRescuePeople(unittest.TestCase):
#     def test_empty_input(self):
#         # Test case for empty input file
#         smarties = {}
#         limit_iq = 500
#         expected_result = (0, [])
#         self.assertEqual(rescue_people(smarties, limit_iq), expected_result)

#     def test_single_trip(self):
#         # Test case for a single trip
#         smarties = {"Sir Isaac Newton": 195, "Nikola Tesla": 189}
#         limit_iq = 500
#         expected_result = (1, [["Sir Isaac Newton", "Nikola Tesla"]])
#         self.assertEqual(rescue_people(smarties, limit_iq), expected_result)

#     def test_multiple_trips(self):
#         # Test case for multiple trips
#         smarties = {
#             "Steve Jobs": 160,
#             "Albert Einstein": 160,
#             "Sir Isaac Newton": 195,
#             "Nikola Tesla": 189
#         }
#         limit_iq = 500
#         expected_result = (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])
#         self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
#     def test_lexicographical_order(self):
#         # Test case for lexicographical order in the second trip
#         smarties = {
#             "Steve Jobs": 160,
#             "Albert Einstein": 160,
#             "Sir Isaac Newton": 195,
#             "Nikola Tesla": 189
#         }
#         limit_iq = 500
#         expected_result = (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])
#         self.assertEqual(rescue_people(smarties, limit_iq), expected_result)

#     # Add more test cases for edge cases, duplicates, etc. as needed

# class TestReadFile(unittest.TestCase):
#     def test_read_file(self):
#         # Test case for reading file
#         file_path = "test_smart_people.txt"
#         expected_result = {
#             "Steve Jobs": 160,
#             "Albert Einstein": 160,
#             "Sir Isaac Newton": 195,
#             "Nikola Tesla": 189
#         }
#         self.assertEqual(read_file(file_path), expected_result)

# if __name__ == '__main__':
#     unittest.main()
