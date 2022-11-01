from test_6setUpClass import SearchTests
from test_7homepagetests import HomePageTest
import unittest

# get all tests from SearchProductTest and HomePageTest class
search_test= unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests= unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
smoke_tests=unittest.TestSuite([home_page_tests, search_test])

# run the test suite combning home_page_tests and search_test
unittest.TextTestRunner(verbosity=2).run(smoke_tests)


