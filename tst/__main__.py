import sys
import unittest

sys.path.append('../Tsunomaki-Janken-Predictor')

loader = unittest.TestLoader()
testSuite = loader.discover('tst')
testRunner = unittest.TextTestRunner(verbosity=2)
testRunner.run(testSuite)
