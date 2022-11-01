from test_6setUpClass import SearchTests
from test_7homepagetests import HomePageTest
import unittest
import HtmlTestRunner
import os

dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
search_test= unittest.TestLoader().loadTestsFromTestCase(SearchTests)
home_page_tests= unittest.TestLoader().loadTestsFromTestCase(HomePageTest)

# create a test suite combining search_test and home_page_test
smoke_tests=unittest.TestSuite([home_page_tests, search_test])

# open the report file
outfile= open(dir + "SmokeTestReport.html", "w")

# configure the html runner option
runner= HtmlTestRunner.HTMLTestRunner(stream= outfile)

# run the suite using HTMLTestRunner
runner.run(smoke_tests)
