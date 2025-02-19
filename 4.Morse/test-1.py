import morse
import unittest

class TestMorseAssignmentOne(unittest.TestCase):

    def test_e(self):
        self.assertEqual(morse.encode_single("E")
                         , "."
                         , "E should be ."
                         )

    def test_upper_and_lower_case(self):
        self.assertEqual(morse.encode_single("L")
                         , morse.encode_single("l")
                         , "Both upper and lower case should work the same"
                         )

    def test_q(self):
        self.assertEqual(morse.encode_single("Q")
                         , "."
                         , "Q should be '--.-'"
                         )

if __name__ == '__main__':
    unittest.main()
