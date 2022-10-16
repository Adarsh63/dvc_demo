# split the raw data
# save it in data/processed folder

import pandas as pd
import os
import argparse
from sklearn.model_selection import train_test_split
from get_data import read_params

def split_and_save(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path =config["split_data"]["train_path"]
    raw_data_path =config["load_data"]["raw_dataset_csv"]
    split_ratio =config["split_data"]["test_size"]
    random_state =config["base"]["random_state"]
    # read the data
    df = pd.read_csv(raw_data_path,sep=",")
    train, test = train_test_split(df, test_size =split_ratio,random_state=random_state)

    train.to_csv(train_data_path,sep=",",encoding='utf-8',index=False)
    test.to_csv(test_data_path,sep=",",encoding='utf-8',index=False)


if __name__ == "__main__":
    # pass the arg function to parse the data
    args = argparse.ArgumentParser()
    # add the argument in args
    args.add_argument("--config",default="C:/Users/ADARSH/PycharmProjects/vnvp/mlopss/params.yaml")
    # then parsee the arge after doint the config chang
    parsed_arg = args.parse_args()
    split_and_save(config_path=parsed_arg.config)
