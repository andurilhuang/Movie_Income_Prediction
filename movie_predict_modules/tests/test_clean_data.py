import unittest
from movie_predict_modules import clean_data as cd

class FunctionRunTest(unittest.TestCase):
    """Test if functions run succesfully with correct input"""

    def test_clean_analysis_data()(self):
        cd.clean_analysis_data()

    def test_clean_regression_data()(self):
        cd.clean_regression_data()

if __name__ == '__main__':
    unittest.main()