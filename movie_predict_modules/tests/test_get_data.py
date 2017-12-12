import unittest
from movie_predict_modules import get_data as gd

class FunctionRunTest(unittest.TestCase):
    """Test if functions run succesfully with correct input"""

    def test_get_tmdb_id_list(self):
        gd.get_tmdb_id_list(2011, 2012, 1, 2)

    def test_get_profit(self):
        gd.get_profit(2011, 2012, 1, 2)

    def test_get_info(self):
        gd.get_info(2011, 2012, 1, 2)

    def test_call_data(self):
        gd.call_data(2011, 2012, 1, 2)

    def test_get_cleaned_data(self):
        gd.get_cleaned_data()

if __name__ == '__main__':
    unittest.main()