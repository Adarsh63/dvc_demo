# load the train and test data
# train the algo
# save the metrics, params
import pandas as pd
import os
import argparse
from get_data import read_params
import numpy as np
import sys
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from urllib.parse import urlparse
import joblib
import json
import os
import ast

os.chdir('C:/Users/ADARSH/PycharmProjects/vnvp/mlopss')


def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))

    mae = np.sqrt(mean_absolute_error(actual, pred))

    r2 = r2_score(actual, pred)
    return rmse, mae, r2


def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]
    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]
    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep=",")
    test = pd.read_csv(test_data_path, sep=",")

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target, axis=1)
    test_x = test.drop(target, axis=1)

    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    lr.fit(train_x, train_y)

    predicted_qualities = lr.predict(test_x)
    (rmse,mae,r2)= eval_metrics(test_y, predicted_qualities)
    print("Elasticnet model (alpha=%f, l1_ratio=%f):" % (alpha, l1_ratio))
    print("  RMSE: %s" % rmse)
    print("  MAE: %s" % mae)
    print("  R2: %s" % r2)
    # then will be two files scores_file and params_file then we need to update in params.yaml file with path
    scores_file = config["reports"]["scores"]
    params_file = config["reports"]["params"]
    with open(scores_file, "w") as f:
        scores = {
            "rmse": rmse,
            "mae": mae,
            "r2": r2
        }
        json.dump(scores, f, indent=4)
    with open(params_file, "w") as f:
        params = {
            'alpha': alpha,
            "l1_ratio": l1_ratio,
        }
        json.dump(params, f, indent=4)

    os.makedirs(model_dir, exist_ok=True)
    model_path = os.path.join(model_dir, "model.joblib")
    joblib.dump(lr, model_path)


# will create a main file
if __name__ == "__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="C:/Users/ADARSH/PycharmProjects/vnvp/mlopss/params.yaml")
    parsed_arg = args.parse_args()
    train_and_evaluate(config_path=parsed_arg.config)
