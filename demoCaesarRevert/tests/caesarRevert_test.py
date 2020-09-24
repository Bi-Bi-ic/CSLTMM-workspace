import unittest
import os, sys
lib_path = os.path.abspath(os.path.join('./demoCaesarRevert'))
sys.path.append(lib_path)
import caesarRevert as w2

class TestWork2(unittest.TestCase):
    def test_isRevertedString(self):
        s = "I Love VN"
        excepted = "NV evoL I"

        result = w2.revertString(s)

        self.assertEqual(excepted, result, "Revert String Got Problem")

    def test_isFormatted(self):
        s = "I Love VN @  "
        excepted = "ilovevn@"

        result = w2.stringFormatted(s)

        self.assertEqual(excepted, result, "String Formatted Got Problem")

    def test_isEncrypted(self):
        s = "iamgroot@"
        distance = 4

        excepted = "Dxssvkqem"
        result = w2.encrypt(distance,s)

        self.assertEqual(excepted, result, "Encrypted Got Error")

    def test_isDecrypted(self):
        s = "Dxssvkqem"
        distance = 4

        excepted = "iamgroot@"
        result = w2.decrypt(distance,s)

        self.assertEqual(excepted, result, "Decrypted Got Error")


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestWork2)
    unittest.TextTestRunner(verbosity=2).run(suite)