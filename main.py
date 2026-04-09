from TestLoader import TestLoader
from TestRunner import TestRunner
from TestLoaderTest import TestLoaderTest

loader = TestLoader()
suite = loader.make_suite(TestLoaderTest)

runner = TestRunner()
runner.run(suite)