import unittest
import pandas as pd
from regression_model import model_evaluation, save_model

TEST_DATA = pd.read_csv("../data/df_example.csv")
MODEL_NAME_1 = "linear"
MODEL_NAME_2 = "lasso"
MODEL_NAME_3 = "ridge"
MODEL_NAME_4 = "tree"
MODEL_NAME_5 = "random forest"
FOLD_NUM = 10
NEW_MODEL = "lrm"
PATH = "saved_model.pkl"


class ModelTest(unittest.TestCase):

    def test_model(self):
        model_evaluation(MODEL_NAME_1, TEST_DATA, FOLD_NUM)
        model_evaluation(MODEL_NAME_2, TEST_DATA, FOLD_NUM)
        model_evaluation(MODEL_NAME_3, TEST_DATA, FOLD_NUM)
        model_evaluation(MODEL_NAME_4, TEST_DATA, FOLD_NUM)
        model_evaluation(MODEL_NAME_5, TEST_DATA, FOLD_NUM)

    def test_save_model(self):
        model_1 = model_evaluation(MODEL_NAME_1, TEST_DATA, FOLD_NUM)
        save_model(model_1, NEW_MODEL, PATH)
