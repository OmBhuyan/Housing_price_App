import argparse
import logging
import os

import joblib
import numpy as np
import pandas as pd
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


def load_housing_data(housing_path):
    """
    Use to load data from the csv file.

    Parameters
    ----------
    housing_path : str
        Path of the csv file.

    Returns
    -------
    DataFrame or TextParser
        A comma-separated values (csv) file is returned as two-dimensional
        data structure with labeled axes.

    """
    csv_path = housing_path
    return pd.read_csv(csv_path)


def eval_model(model, data):
    """
    Function to evaluate the trained model on the processed test data.

    Parameters
    ----------
    model_path : str
        Stored model path.
    data_path : str
        Processed test data path.

    Returns
    -------
    rmse : float
        Root mean square error for the model.
    mae : float
        Mean absolute error for the model.
    r2 : float
        R2 socre of the model.
    """

    # logger.info("Loading model...")
    # model = joblib.load(model_path)
    # logger.info("Loading model complete.")

    # logger.info("Loading test data..")
    test_data = data  # load_housing_data(data_path)
    # logger.info("Loading data complete.")

    housing_prepared_test = test_data.drop("median_house_value", axis=1)
    test_actual = test_data["median_house_value"]
    pred = model.predict(housing_prepared_test)
    rmse = np.sqrt(mean_squared_error(test_actual, pred))
    mae = mean_absolute_error(test_actual, pred)
    r2 = r2_score(test_actual, pred)
    # logger.info("Model performance : ")
    # logger.info("RMSE :%s", rmse)
    # logger.info("MAE :%s", mae)
    # logger.info("R2 :%s", r2)
    return rmse, mae, r2
