# read params
# read process
# return dataframe
import os

import pandas as pd
import yaml
import argparse


def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config


# create one function which will get the data , and thn we need to pass the config path
def get_data(config_path):
    config = read_params(config_path)
    data_path = config['data_source']["s3_source"]
    df = pd.read_csv(data_path,sep=",",encoding='utf-8')
    print(df.head())


if __name__ == "__main__":  # create a main this will work as entrenc point for project
    args = argparse.ArgumentParser()  # call the argparse for parsing the params data
    args.add_argument("--config", default="C:/Users/ADARSH/PycharmProjects/vnvp/mlopss/params.yaml")  # add to config file
    parsed_args = args.parse_args()  # here the data will pars
    get_data(config_path=parsed_args.config)  # after creating def function mention here , get data method

